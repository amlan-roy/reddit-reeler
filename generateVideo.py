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

import os
from moviepy.editor import AudioFileClip,ImageClip, VideoFileClip,CompositeVideoClip
from moviepy.audio.fx.volumex import volumex
from audioGeneration import generateAudio
from datetime import datetime
from findText import findText
from tkinter import filedialog
from tkinter import Tk
import random



def loadImages():
    root = Tk()
    root.withdraw()

    root.filename =  filedialog.askopenfilenames(initialdir = "%USERPROFILE%\Downloads",title = "Select file",filetypes = (("jpeg files",["*.jpg","*.jpeg","*.png"]),("all files","*.*")))
    return [i for i in root.filename]

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
    path = f"temp/videos/bg{random.choice(bgs)}"
    return VideoFileClip(path)

def makeVideo(
    audioVolume = 1, 
    maxVideoLength = 90,
    videoSavePath = 'output/'
    ):

    images = loadImages()
    if not images:
        print("No images selected. Try again")
        return
    
    generateTexts(images)
    saveAudio()
    

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

    # start timestamp to add first clip
    start = 0.3

    # max video length is the smaller of provided maxVideoLength and the bgVideo
    maxLength = video.duration if video.duration < maxVideoLength else maxVideoLength

    # make clips for each image and audio pair
    for i in clips:
        i = i.resize(width=width*0.8)
        x = int(width*0.5 - i.w*0.5)
        y = int(height*0.5 -i.h*0.5)
        i = i.set_pos((x,y))
        video = CompositeVideoClip(
            [video,
            i.set_start(start)]
        )
        if(start + i.duration + 0.3 > maxLength):
            break
        start = start + i.duration + 0.3
        # i.close()
    
    # crop the video if the bg video is longer than total clips length + 0.3 sec
    if start<maxLength:
        video = video.subclip(0,start)
    
    # current timestamp
    now = datetime.now()
    now = now.strftime("%d-%m-%Y-%H-%M-%S")

    # export video
    video.write_videofile(f"{videoSavePath}/{now}.mp4",
        fps=24,
        remove_temp=True,
        preset='ultrafast',
        threads = 16,
        )



