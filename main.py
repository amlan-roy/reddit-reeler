from imageGeneration import generateImages
from utils import tempPost,tempComments

def testingFunct():
    print('testing function')
    img = generateImages(post=tempPost,comments=tempComments)
    title = img[0]
    bodyList = img[1]

    title.show()

    if bodyList:
        for i in bodyList:
            for j in i:
                j.show()

def main():
    print('in main')
    testingFunct()

if __name__ == "__main__":
    main()

