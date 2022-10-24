from audioGeneration import generateAudio, generateAudioForText
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
def main():
    print('in main')
    testingFunct()

if __name__ == "__main__":
    main()

