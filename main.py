from imageGeneration import generateImages
from utils import tempPost

def testingFunct():
    print('testing function')
    img = generateImages(post=tempPost,comments=[])
    img.show()

def main():
    print('in main')
    testingFunct()

if __name__ == "__main__":
    main()

