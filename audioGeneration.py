from gtts import gTTS
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def generateAudioForText(titleText,bodyTexts=[]):
    """
    Deprecated function. Was used for custom Image Generation.
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

def generateAudio(text,savePath,driver='sapi',speed=1.125, voiceModel='male'):
    """
    generateAudio(): Generates and saves audio from the given text to the given path.
    @param:
        @text: Required. The text for which audio is to be generated.
        @savePath: Required. The path where the audio file should be stored.
        @driver: select from gtts and sapi. This specifies the driver to be used to generate text.
                gtts provides a more realistic voice, but can not control the speed. And can not change
                gender. Other options are available only for sapi/
        @speed: Only if driver == sapi. Float. 1 = normal, >1 = fast, <1 = fast
        @voiceModel: Only if driver == sapi. Can select 'male' or 'female'. String.
    """

    if driver.lower() == 'gtts':
        language = 'en'
        myobj = gTTS(text=text, lang=language, slow=False, tld='ca')
        if savePath:
            myobj.save(savePath)
        return myobj

    if driver.lower() == 'sapi':

        if voiceModel.lower() == 'male':
            engine.setProperty('voice', voices[0].id)
        if voiceModel.lower() == 'female':
            engine.setProperty('voice', voices[1].id)

        engine.setProperty('rate', int(200*speed))
        engine.save_to_file(text,savePath)
        engine.runAndWait()
        return savePath
