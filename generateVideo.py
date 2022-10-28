'''
Steps:
1 Load the images
2 For each image, generate recognised text
3 make a list of tuples of image and its text: [(image,text)]
4 display the image and text for each element of list, give option to edit text, update the list with this new text
    For this, save text files for each photo and use that
5 generate audio for each photo, with text as the given text.
6 Make clips of these image,audio pair
7 Attach these clips in order to the base video
8 DO THIS LATER: add bg music 
9 Export the video
'''

from asyncio.log import logger
from importlib.resources import path
import os
from moviepy.editor import AudioFileClip,ImageClip, VideoFileClip,CompositeVideoClip, CompositeAudioClip, concatenate_videoclips
from moviepy.audio.fx.volumex import volumex
from moviepy.audio.fx.audio_normalize import audio_normalize
from audioGeneration import generateAudio
from datetime import datetime
from findText import findText
from tkinter import filedialog
from tkinter import Tk
import random
import numpy as np
from PIL import Image

class MusicCategory:
    sad = 'sad'
    commentry = 'commentry'
    mystery = 'mystery'

def clearTemp():
    audios = os.listdir('temp/audios')
    for i in audios:
        os.remove(f"temp/audios/{i}")
    clips = os.listdir('temp/clips')
    for i in clips:
        os.remove(f"temp/clips/{i}")
    images = os.listdir('temp/images')
    for i in images:
        os.remove(f"temp/images/{i}")
    texts = os.listdir('temp/texts')
    for i in texts:
        os.remove(f"temp/texts/{i}")


def loadImages():
    root = Tk()
    root.withdraw()

    root.filename =  filedialog.askopenfilenames(initialdir = "%USERPROFILE%\Downloads",title = "Select file",filetypes = (("jpeg files",["*.jpg","*.jpeg","*.png"]),("all files","*.*")))
    lst = [i for i in root.filename]
    lst.reverse()
    # lst = [Image.open(i) for i in lst]
    return lst

def saveText(text,fileName):
    file = open(f"temp/texts/{fileName}.txt","w+")
    file.write(text)
    file.close

def generateTexts(listOfImagePath):
    index = 0
    for i in listOfImagePath:
        text = findText(i)
        saveText(text,index)
        index = index + 1

def saveAudio():
    listOfTexts = os.listdir('temp/texts')

    index = 0
    for i in listOfTexts:
        textFile = open(f"temp/texts/{index}.txt","r+")
        text = textFile.read()
        textFile.close()

        generateAudio(text=text,savePath=f"temp/audios/{index}.mp3")
        index = index + 1

def selectRandomBg():
    bgs = os.listdir('temp/videos/bg')
    path = f"temp/videos/bg/{random.choice(bgs)}"
    return VideoFileClip(path)

def selectRandomMusic(type,volume=0.07):
    path = 'temp/bgMusic/' + type
    bgs = os.listdir(path)
    path = path + f"/{random.choice(bgs)}"
    audiofile =  AudioFileClip(path)
    audiofile = audiofile.fx(audio_normalize)
    audiofile = audiofile.fx(volumex,volume)
    return audiofile

def makeVideo(
    audioVolume = 1, 
    maxVideoLength = 90,
    videoSavePath = 'output/',
    bgMusicType = MusicCategory.commentry
    ):
    print('0')


    clearTemp()

    # inp = input("****************************************\n****************************************\n\nEnter bg music type\n1- Commentry\n2- mystrey\n3- sad \nother- any other\nEnter your choice:")
    print('1')
    # bgMusicType = MusicCategory.sad
    # if inp == 1:
    #     bgMusicType = MusicCategory.commentry
    # if inp == 2:
    #     bgMusicType = MusicCategory.mystery
    # if inp == 3:
    #     bgMusicType = MusicCategory.sad


    images = loadImages()
    if not images:
        print("No images selected. Try again")
        return
    
    print('2')

    generateTexts(images)

    inp = input('did you edit the text files?(y)\nothers = no')
    if not (inp == 'y' or inp == 'Y'):
        return

    saveAudio()
    
    print('3')

    audios = os.listdir('temp/audios')
    audios = [f"temp/audios/{i}" for i in audios]

    clips = []

    index = 0
    for i in images:
        
        audio = AudioFileClip(audios[index])
        audio = (
            audio
            .fx(volumex,audioVolume)
        )
        duration = audio.duration + 0.5 if index == 0 else audio.duration
        # clip = ImageClip(np.array(Image.open(images[index])),duration=duration,).set_audio(audio)
        clip = ImageClip(images[index],duration=duration,).set_audio(audio)
        clip = clip.set_fps(24)
        clips.append(clip)
        index = index + 1

    video = selectRandomBg()
    print('4')
    
    aspectRatio = 9/16 # width/height

    # Crop the bg videos to fit correct aspect ratio
    if video.w/video.h < aspectRatio:
        width = video.w
        height = width/aspectRatio
    else:
        height = video.h
        width = height * aspectRatio
    video = video.crop(x_center=video.w/2,y_center=video.h/2,width=width,height=height)

    # start timestamp to add first clip

    # max video length is the smaller of provided maxVideoLength and the bgVideo
    maxLength = video.duration if video.duration < maxVideoLength else maxVideoLength

    print('5')

    mainVidClips =[]

    start = 0.0
    for i in clips:
        print(f"start before: {start}")
        add_val = i.duration + 0.3
        if(start + add_val > maxLength):
            break
        i = i.resize(width=width*0.8)
        x = int(width*0.5 - i.w*0.5)
        y = int(height*0.5 -i.h*0.5)
        i = i.set_pos((x,y))
        clp = video.subclip(start,add_val)
        clp = CompositeVideoClip([clp,i],use_bgclip=True)
        mainVidClips.append(clp)

        
        if(start + add_val > maxLength):
            break
        start = start + add_val
        print(f"start after: {start}")
    
    print(f"start after: {start}")
    index = 0
    # for i in mainVidClips:
    #     savepath = f"temp/clips/{index}.mp4"
    #     i.write_videofile(savepath,
    #     fps=24,
    #     remove_temp=True,
    #     preset='ultrafast',
    #     threads = 4,
    #     )
    #     index = index + 1
    
    # videoClips = os.listdir('temp/clips/')
    # mainVidClips = [VideoFileClip(f"temp/clips/{i}") for i in videoClips]
    video = concatenate_videoclips(mainVidClips)

    print(f"point 1:\nvideo.duration:{video.duration}\nstart:{start}")
    # crop the video if the bg video is longer than total clips length + 0.3 sec
    duration = maxLength
    if start<maxLength:
        duration = start
        if(video.duration<start):
            duration = video.duration
        video = video.subclip(0,duration)
    
    # video = video.set_duration(duration)
    # current timestamp
    now = datetime.now()
    now = now.strftime("%d-%m-%Y-%H-%M-%S")

    print('6')


    if(bgMusicType):
        bgMusic = selectRandomMusic(bgMusicType)

        if bgMusic.duration > duration:
            bgMusic = bgMusic.subclip(0,duration)

        bgAudio = CompositeAudioClip([video.audio,bgMusic])
        video = video.set_audio(bgAudio)

    print('7')

    # export video
    print(f"point 2:\nvideo.duration:{video.duration}\nstart:{start}")


    video.write_videofile(f"{videoSavePath}/{now}.mp4",
        fps=24,
        remove_temp=True,
        preset='ultrafast',
        threads = 4,
        )
    
    video.close()
    
    clearTemp()



