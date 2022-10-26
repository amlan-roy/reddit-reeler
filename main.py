from audioGeneration import generateAudio, generateAudioForText
from findText import findText
from generateVideo import generateTexts, loadImages, makeVideo, saveAudio
from imageGeneration import generateImages
from utils import tempPost,tempComments

def testingFunct():
    print('testing function')
    img = generateImages(post=tempPost,comments=tempComments)
    title = img[0]
    bodyList = img[1]

    generateAudioForText(title[1],bodyList)

    title[0].save("images/temp/titleImage.jpg")

    if bodyList:
        p=0
        for i in bodyList:
            q=0
            for j in i:
                # j[0].show()
                savePath=f"images/temp/post_no-{p}_{q}.jpg"
                j[0].save(savePath)
                q = q + 1
            p = p + 1

def testFunct2():
    # imgs = loadImages()
    # generateTexts(imgs)

    # inp = input('Please remove unnecessary words from the text files\n\nDid you clean the text files ? (y)\n(press any other key for to exit)')
    # if inp == 'y' or inp =='Y':
    #     saveAudio()
        saveAudio()
        makeVideo(audioVolume=1.5)

def main():
    print('in main')
    testFunct2()

if __name__ == "__main__":
    main()

