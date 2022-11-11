import sys
from generateVideo import MusicCategory, detectTexts, makeVideo, generateVideo
import json

selectedImagesPaths = '["C:\\Users\\Amlan\\Downloads\\3.jpg","C:\\Users\\Amlan\\Downloads\\1.jpg","C:\\Users\\Amlan\\Downloads\\2.jpg"]'

audioModel = 'sapi'
speed = 1.0
voiceModel = 'male'
videoSavePath = "C:\\Users\\Amlan\\Desktop\\reddit-reels"
maxVideoLength = 90
        
def main():
    imgAndTexts = detectTexts(
        selectedImagesPaths = selectedImagesPaths,
        )
    generateVideo(
        imgAndTexts = imgAndTexts,
        audioModel = audioModel,
        audioVolume=1.5,
        maxVideoLength=90,
        videoSavePath=videoSavePath,
        bgMusicType=MusicCategory.commentry,
    )


def textDetection():
    #  cmdLineArgument = "['C:\\Users\\Amlan\\Downloads\\3.jpg','C:\\Users\\Amlan\\Downloads\\1.jpg','C:\\Users\\Amlan\\Downloads\\2.jpg']"

    imgPaths = sys.argv[1]
 
    print(imgPaths)
    if not imgPaths:
        imgPaths = selectedImagesPaths
    
    # cleaning the input string and converting it into list of strings
    imgPaths = imgPaths.replace('[','')
    imgPaths = imgPaths.replace(']','')
    imgPaths = imgPaths.replace('"','')
    imgPaths = imgPaths.replace("'","")
    imgPaths = imgPaths.split(",")
    imgPaths = [i for i in imgPaths if i]
    
    # imgPaths = imgPaths.decode('string_escape')

    # imgPaths = json.loads(imgPaths)
    for i in imgPaths:
        print(type(i))
    print(imgPaths)

    imgAndTexts = detectTexts(
        selectedImagesPaths = imgPaths,
        )
    print(str(imgAndTexts))

def videoGeneration():

    #  cmdLineArgument = "['C:\\Users\\Amlan\\Downloads\\3.jpg','C:\\Users\\Amlan\\Downloads\\1.jpg','C:\\Users\\Amlan\\Downloads\\2.jpg']"

    """[{"imgPath": "C:\\Users\\Amlan\\Downloads\\3.jpg","text": "I was pissed. I told her what my boundaries are and if my brother is invited then I will not pay my part of the wedding. She became angry and told me its time to let go of the past. I told her its not her call to make. We argued some more and she told me! am making her wedding about myself. I told her I will probably not even attend so it will be all about her. She left crying."},{"imgPath": "C:\\Users\\Amlan\\Downloads\\3.jpg","text": "I"m 46M, my brother 48M. When I was 20, my then girlfriend cheated with my brother. I was heartbroken and pissed. I told him he is no longer my brother. Despite my request, my family didnt cut him off, so I told them that I will never again be in the same place as he is. If they wish to invite both, then they should just invite him as I am the one giving ultimate."},{"imgPath": "C:\\Users\\Amlan\\Downloads\\3.jpg","text": "My daughter is getting married in spring next year. In our culture both parents are paying for the wedding, 50/50. Unexpectedly, my daughter sat me down and told me that she will be inviting my brother and his family(he married my cheating ex). Apparently, she was seeing them for the last 4 years and built a relationship behind my back. She even wants her cousin to be some kind of flower girl."}]
    """

    imgAndTexts = sys.argv[1]
    print(imgAndTexts)

    imgAndTexts = json.loads(imgAndTexts)

    print(type(imgAndTexts))
    print(imgAndTexts)
    
    generateVideo(
        imgAndTexts = imgAndTexts,
        audioModel = audioModel,
        audioVolume=1.5,
        maxVideoLength=90,
        videoSavePath=videoSavePath,
        bgMusicType=MusicCategory.commentry,
    )

if __name__ == "__main__":
    # textDetection()
    videoGeneration()