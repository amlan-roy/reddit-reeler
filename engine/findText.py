from pytesseract import pytesseract
from config import path_to_tesseract
from PIL import Image

pytesseract.tesseract_cmd = path_to_tesseract

def findText(imgPath):
    """
        findText(): Function to give text from an image

        @parms:
            @imgPath: The path (absolute/relative) of the image file
        @returns:
            @text: Text detected from the image
    """
    img = Image.open(imgPath)
    text = pytesseract.image_to_string(img)
    return text