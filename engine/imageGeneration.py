"""
** MODULE NOT USED ***

- This module was written earlier, to generate the images to display from json data.
- But we are now using the screenshots directly, so this module is redundant right now.
- We might update this module and use it in future, if we need custom image generation at some point of time.
"""

from PIL import Image, ImageDraw, ImageFont
from utils import BodyText, Post

class FONTS:
    Large = ImageFont.truetype('fonts\\IBMPlexSans-Medium.ttf', size=20)
    SmallBold = ImageFont.truetype('fonts\\IBMPlexSans-Bold.ttf', size=12)
    SmallMedium = ImageFont.truetype('fonts\\IBMPlexSans-Medium.ttf', size=12)
    SmallNormal = ImageFont.truetype('fonts\\IBMPlexSans-Regular.ttf', size=12)
    Normal = ImageFont.truetype('fonts\\IBMPlexSans-Regular.ttf', size=14)

class COLORS:
    white = (215,218,220,1)
    gray_1 = (129,131,132,1)
    gray_2 = (52,53,54,1)
    gray_3 = (26,26,27,1)

def text_wrap(text, font, max_width):
    """Wrap text base on specified width. 
    This is to enable text of width more than the image width to be display
    nicely.
    @params:
        text: str
            text to wrap
        font: obj
            font of the text
        max_width: int
            width to split the text with
    @return
        lines: list[str]
            list of sub-strings
    """
    lines = []
    
    # If the text width is smaller than the image width, then no need to split
    # just add it to the line list and return
    if (font.getbbox(text)[2] - font.getbbox(text)[0])  <= max_width:
        lines.append(text)
    else:
        #split the line by spaces to get words
        words = text.split(' ')
        i = 0
        # append every word to a line while its width is shorter than the image width
        while i < len(words):
            line = ''
            while i < len(words) and (font.getbbox(line + words[i])[2] - font.getbbox(line + words[i])[0]) <= max_width:
                line = line + words[i]+ " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line)
    return lines

def addTextInImage(image, text,textCoordinates: tuple[int,int],font, color):
    draw = ImageDraw.Draw(image)
    x = textCoordinates[0]
    y = textCoordinates[1]
    draw.text((x, y), text , font=font, fill=color)
    return image

def generateTitle(post:Post, image:Image, opacity = 1):
    """
    @return:
        (image,text)
    """
    convertedOpacity = int(255 * opacity)
    
    #draw top subreddit and username
    topSubreddit = f"r/{post.subreddit}"
    topUsername = f"u/{post.username}"
    image = addTextInImage(image,topSubreddit,(8,8),FONTS.SmallNormal, color=COLORS.white)
    image = addTextInImage(image,topUsername,(8,23),FONTS.SmallNormal, color=COLORS.gray_1)

    #draw title
    # Line height - font size
    bottomPaddingText = 24 - 20

    y = 46
    wrappedTitleTextList = text_wrap(text=post.title, font=FONTS.Large, max_width=572)
    for i in wrappedTitleTextList:
        image = addTextInImage(image, text=i, textCoordinates=(8,y), font=FONTS.Large, color= COLORS.white)
        y = y + 20 + bottomPaddingText
    
    # y = y + bottom padding
    y = y + 8

    width,_ = image.size
    image = image.crop((0,0,width,y))

    return (image,post.title)

def generateBody(bodyText:BodyText, opacity = 1) -> list:
    """
        @return:            
            [(Image,text)]
    """

    image = Image.new(mode="RGB", size=(600,300), color=COLORS.gray_3)

    username = f"u/{bodyText.username}"
    image = addTextInImage(image,username,(8,8),FONTS.SmallNormal, color=COLORS.gray_1)

 # splitting the strings with newline and creating the new list with the newline chars as seperate entries (except first newline)
    # split the texts with newline. 
    # text_wrap for each element of this new list.
    # add all these lists in a new list 
    tempList_1 = []
    temp = bodyText.text.split("\n")
    for j  in temp:
        tempList_1.append(j)

    tempList_2 = []
    for i in tempList_1:
        tempList_2 = tempList_2 + text_wrap(i, FONTS.Normal, max_width=572)

    wrappedBodyTextList = tempList_2

    y = 31

    images = []
    text=""
    for i in wrappedBodyTextList:
        # if y + padding bottom + lineheight
        if y + 8 + 21 > 300:
            images.append((image,text))
            image = False
            text = ""
        
        if not image:
            y = 16
            image = Image.new(mode="RGB", size=(600,300), color=COLORS.gray_3)
            text=""
        text = text + i
        image = addTextInImage(image=image, text=i, textCoordinates=(8,y), font=FONTS.Normal, color=COLORS.white)
        y = y + 21
    
    width,_ = image.size
    if y + 8 <= 300:
        y = y + 8
    image = image.crop((0,0,width,y))
    
    images.append((image,text))
        
    return images

def generateBodyOrComments(post:Post, comments = []):
    """
    @param:
        comments: list[BodyText]
    @return
        images: list[list[(Image,text)]]
            list of list of Image
    """
    images = []
    # images: list(list(Image))
    if comments:
        for i in comments:
            # print(i)
            images.append(generateBody(i))
    else:
        tempBodyText = BodyText(username=post.username,text=post.postText, upvotes=post.upvotes)
        images.append(generateBody(tempBodyText))
    
    return images

def generateImages(post:Post,comments= []):
    image = Image.new(mode="RGB", size=(600,5000), color=COLORS.gray_3)
    image = generateTitle(post=post, image=image)
    bodyImages = generateBodyOrComments(post=post, comments=comments)

    return (image,bodyImages)
    
       