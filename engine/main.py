from generateVideo import MusicCategory
import json
import requests

selectedImagesPaths = '["C:\\Users\\Amlan\\Downloads\\3.jpg","C:\\Users\\Amlan\\Downloads\\1.jpg","C:\\Users\\Amlan\\Downloads\\2.jpg"]'

audioModel = 'sapi'
speed = 1.0
voiceModel = 'male'
videoSavePath = "C:\\Users\\Amlan\\Desktop\\reddit-reels"
maxVideoLength = 90
        
def mockSendingReq():
    """
        Temp method used for testing.
        Sends post requests to mock the actual sending of post request.
    """
    headers = {
        'Content-Type': 'application/json'
    }
    # detect text
    detectTextUrl = "http://127.0.0.1:5000/detectText"
    detectTextPayload = {'imgPaths':['C:\\Users\\Amlan\\Downloads\\3.jpg','C:\\Users\\Amlan\\Downloads\\1.jpg','C:\\Users\\Amlan\\Downloads\\2.jpg']}
    detectTextResponse = requests.post(detectTextUrl, headers=headers, data=json.dumps(detectTextPayload))
    
    # generate video
    generateVideoPayload = {
        "imgAndTexts": json.loads(detectTextResponse.text)['data'],
        "audioModel":audioModel,
        "audioVolume":1.5,
        "maxVideoLength":90,
        "videoSavePath":videoSavePath,
        "bgMusicType":MusicCategory.commentry,
    }
    generateVideoUrl = "http://127.0.0.1:5000/generateVideo"
    generateVideoResponse = requests.post(generateVideoUrl, headers=headers, data=json.dumps(generateVideoPayload))

    print(generateVideoResponse.text)

if __name__ == "__main__":
    mockSendingReq()