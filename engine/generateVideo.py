import os
from typing import List
from moviepy.editor import AudioFileClip,ImageClip, VideoFileClip,CompositeVideoClip, CompositeAudioClip, concatenate_videoclips
from moviepy.audio.fx.volumex import volumex
from moviepy.audio.fx.audio_normalize import audio_normalize
from audioGeneration import generateAudio
from datetime import datetime
from findText import findText
from tkinter import filedialog
from tkinter import Tk
import random

# CONSTANTS
scrptPath = os.path.realpath(os.path.dirname(__file__))
imageSelectInitialDirectory = scrptPath + "\\%USERPROFILE%\\Downloads"
tempTextFilePath = scrptPath + "\\temp\\texts"
tempAudioFilePath = scrptPath + "\\temp\\audios"
backgroundVideosFilePath = scrptPath + "\\temp\\videos\\bg"
backgroundMusicsFilePath = scrptPath + "\\temp\\bgMusic"



class MusicCategory:
    """
        Class to select music category
    """
    sad = 'sad'
    commentry = 'commentry'
    mystery = 'mystery'

def clearTemp():
    """
        Function to clear the Temp Folders
    """
    tempFilePathList =[
        tempAudioFilePath,
        scrptPath + '\\temp\\clips',
        scrptPath + '\\temp\\images',
        tempTextFilePath
    ]

    for path in tempFilePathList:
            files = os.listdir(path)
            for file in files:
                os.remove(path + "\\" + file)

def loadImages():
    """
        Function to load images. Opens a window to select the images.
    """
    root = Tk()
    root.withdraw()

    root.filename =  filedialog.askopenfilenames(initialdir = imageSelectInitialDirectory,title = "Select file",filetypes = (("jpeg files",["*.jpg","*.jpeg","*.png"]),("all files","*.*")))
    lst = [i for i in root.filename]
    lst.reverse()
    return lst

def saveText(text,fileName):
    """
        Function to save the provided text with given file name as .txt file
    """
    file = open(f"{tempTextFilePath}\\{fileName}.txt","w+")
    file.write(text)
    file.close

def generateTexts(listOfImagePath):
    """
        Function that
        - takes list of Image Paths
        - gets text in each image
        - generates the text files for the images
    """
    index = 0
    imgAndTexts = []
    for i in listOfImagePath:
        text = findText(i)
        imgAndTexts.append((i,text))
        saveText(text,index)
        index = index + 1
    return imgAndTexts

def saveAudio(listOfTexts):
    """
        saves the audio for each text file in the temp text path and saves them in temp audio path
    """
    # listOfTexts = os.listdir(tempTextFilePath)

    index = 0
    for i in listOfTexts:
        # textFile = open(f"{tempTextFilePath}/{index}.txt","r+")
        # text = textFile.read()
        # textFile.close()

        generateAudio(text=i,savePath=f"{tempAudioFilePath}\\{index}.mp3")
        index = index + 1

def selectRandomBg():
    """
        select random video for background
    """
    bgs = os.listdir(backgroundVideosFilePath)
    path = f"{backgroundVideosFilePath}\\{random.choice(bgs)}"
    return VideoFileClip(path)

def selectRandomMusic(type,volume=0.07):
    """
        select random video for background
    """
    path = backgroundMusicsFilePath + '\\' + type
    bgs = os.listdir(path)
    path = path + f"\\{random.choice(bgs)}"
    audiofile =  AudioFileClip(path)
    audiofile = audiofile.fx(audio_normalize)
    audiofile = audiofile.fx(volumex,volume)
    return audiofile

def makeVideo(
    audioVolume = 1, 
    maxVideoLength = 90,
    videoSavePath = "C:\\Users\\Amlan\\Desktop\\reddit-reels",
    bgMusicType = MusicCategory.commentry
    ):

    clearTemp()

    images = loadImages()
    if not images:
        # print("No images selected. Try again")
        return
    
    generateTexts(images)

    inp = input('did you edit the text files?(y)\nothers = no')
    if not (inp == 'y' or inp == 'Y'):
        return

    saveAudio()
    
    audios = os.listdir(tempAudioFilePath)
    audios = [f"{tempAudioFilePath}\\{i}" for i in audios]

    clips = []

    index = 0
    for i in images:
        audio = AudioFileClip(audios[index])
        audio = (
            audio
            .fx(volumex,audioVolume)
        )
        duration = audio.duration + 0.5 if index == 0 else audio.duration
        clip = ImageClip(images[index],duration=duration,).set_audio(audio)
        clip = clip.set_fps(24)
        clips.append(clip)
        index = index + 1

    video = selectRandomBg()
    
    aspectRatio = 9/16 # width/height

    # Crop the bg videos to fit correct aspect ratio
    if video.w/video.h < aspectRatio:
        width = video.w
        height = width/aspectRatio
    else:
        height = video.h
        width = height * aspectRatio
    video = video.crop(x_center=video.w/2,y_center=video.h/2,width=width,height=height)

    # max video length is the smaller of provided maxVideoLength and the bgVideo
    maxLength = video.duration if video.duration < maxVideoLength else maxVideoLength

    mainVidClips =[]

    # start timestamp to add first clip
    start = 0.0
    for i in clips:
        add_val = round(i.duration + 0.3,3)
        if(start + add_val > maxLength):
            break
        i = i.resize(width=width*0.8)
        x = int(width*0.5 - i.w*0.5)
        y = int(height*0.5 -i.h*0.5)
        i = i.set_pos((x,y))
        clp = video.subclip(start,start + add_val)
        clp = CompositeVideoClip([clp,i],use_bgclip=True)
        mainVidClips.append(clp)
        
        if(start + add_val > maxLength):
            break
        start = start + add_val
    
    index = 0

    video = concatenate_videoclips(mainVidClips)

    # crop the video if the bg video is longer than total clips length + 0.3 sec
    duration = maxLength
    if start<maxLength:
        duration = start
        if(video.duration<start):
            duration = video.duration
        video = video.subclip(0,duration)

    now = datetime.now()
    now = now.strftime("%d-%m-%Y-%H-%M-%S")

    if(bgMusicType):
        bgMusic = selectRandomMusic(bgMusicType)
        if bgMusic.duration > duration:
            bgMusic = bgMusic.subclip(0,duration)
        bgAudio = CompositeAudioClip([video.audio,bgMusic])
        video = video.set_audio(bgAudio)

    # export video
    video.write_videofile(f"{videoSavePath}/{now}.mp4",
        fps=24,
        remove_temp=True,
        preset='ultrafast',
        threads = 4,
        )

    clearTemp()

def detectTexts(
    selectedImagesPaths,
    ):
    """
    return -> [(imgPath,text),(imgPath,text),(imgPath,text),...]
    """
    clearTemp()    
    return generateTexts(selectedImagesPaths)

def generateVideo(
    imgAndTexts,
    audioModel,
    audioVolume = 1, 
    maxVideoLength = 90,
    videoSavePath = "C:\\Users\\Amlan\\Desktop\\reddit-reels",
    bgMusicType = MusicCategory.commentry
):
    """
    params:
        imgAndTexts: [(imgPath,text),(imgPath,text),(imgPath,text),...]
    """
    saveAudio([i[1] for i in imgAndTexts])
    
    audios = os.listdir(tempAudioFilePath)
    audios = [f"{tempAudioFilePath}\\{i}" for i in audios]

    clips = []

    index = 0
    for i in imgAndTexts:
        audio = AudioFileClip(audios[index])
        audio = (
            audio
            .fx(volumex,audioVolume)
        )
        duration = audio.duration + 0.5 if index == 0 else audio.duration
        clip = ImageClip(imgAndTexts[index][0],duration=duration,).set_audio(audio)
        clip = clip.set_fps(24)
        clips.append(clip)
        index = index + 1

    video = selectRandomBg()
    
    aspectRatio = 9/16 # width/height

    # Crop the bg videos to fit correct aspect ratio
    if video.w/video.h < aspectRatio:
        width = video.w
        height = width/aspectRatio
    else:
        height = video.h
        width = height * aspectRatio
    video = video.crop(x_center=video.w/2,y_center=video.h/2,width=width,height=height)

    # max video length is the smaller of provided maxVideoLength and the bgVideo
    maxLength = video.duration if video.duration < maxVideoLength else maxVideoLength

    mainVidClips =[]

    # start timestamp to add first clip
    start = 0.0
    for i in clips:
        add_val = round(i.duration + 0.3,3)
        if(start + add_val > maxLength):
            break
        i = i.resize(width=width*0.8)
        x = int(width*0.5 - i.w*0.5)
        y = int(height*0.5 -i.h*0.5)
        i = i.set_pos((x,y))
        clp = video.subclip(start,start + add_val)
        clp = CompositeVideoClip([clp,i],use_bgclip=True)
        mainVidClips.append(clp)
        
        if(start + add_val > maxLength):
            break
        start = start + add_val
    
    index = 0

    video = concatenate_videoclips(mainVidClips)

    # crop the video if the bg video is longer than total clips length + 0.3 sec
    duration = maxLength
    if start<maxLength:
        duration = start
        if(video.duration<start):
            duration = video.duration
        video = video.subclip(0,duration)

    now = datetime.now()
    now = now.strftime("%d-%m-%Y-%H-%M-%S")

    if(bgMusicType):
        bgMusic = selectRandomMusic(bgMusicType)
        if bgMusic.duration > duration:
            bgMusic = bgMusic.subclip(0,duration)
        bgAudio = CompositeAudioClip([video.audio,bgMusic])
        video = video.set_audio(bgAudio)

    # export video
    video.write_videofile(f"{videoSavePath}\\{now}.mp4",
        fps=24,
        remove_temp=True,
        preset='ultrafast',
        threads = 4,
        )

    clearTemp()
