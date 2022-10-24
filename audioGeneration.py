from gtts import gTTS
import os

def generateAudioForText(titleText,bodyTexts=[]):
    """
    @param:
        titleText: string
    @return
        bodyTexts: [[(Image,text)]]
    """

    titleSavePath = "audio/temp/titleAudio.mp3"
    titleAudio = generateAudio(titleText,titleSavePath)

    i = 0
    for j in bodyTexts:
        l = 0
        for k in j:
            savePath = f"audio/temp/post_no-{i}_{l}.mp3"
            bodyAudio= generateAudio(k[1],savePath=savePath)
            l=l+1
        i=i+1

def generateAudio(text,savePath=''):
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False, tld='ca')
    if savePath:
        myobj.save(savePath)
    return myobj

