from cgitb import text
from pytesseract import pytesseract
from config import path_to_tesseract
from PIL import Image

pytesseract.tesseract_cmd = path_to_tesseract

def findText(imgPath):
    img = Image.open(imgPath)
    text = pytesseract.image_to_string(img)
    return text