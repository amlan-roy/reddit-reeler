from flask import Flask, jsonify, request
from generateVideo import detectTexts, generateVideo
import json
import urllib.parse as ulib

app = Flask(__name__)

default_audioModel = 'sapi'
default_speed = 1.0
default_voiceModel = 'male'
default_videoSavePath = "C:\\Users\\Amlan\\Desktop\\reddit-reels"
default_maxVideoLength = 90
default_audioVolume = 1.5

# on the terminal type: http://127.0.0.1:5000/

@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "Connected..."
		return jsonify({'data': data})

@app.route('/detectText', methods = ['POST'])
def foo():
    imgPaths = request.json['imgPaths']
    imgPaths = [ulib.unquote(i) for i in imgPaths]
    imgAndTexts = detectTexts(selectedImagesPaths = imgPaths)

    return jsonify({'data': json.dumps(imgAndTexts)})

@app.route('/generateVideo', methods = ['POST'])
def bar():
    try:
        imgAndTexts = request.json['imgAndTexts']
        audioVolume = request.json['audioVolume']
        maxVideoLength = request.json['maxVideoLength']
        videoSavePath = request.json['videoSavePath']
        bgMusicType = request.json['bgMusicType']
        

        generateVideo(
            imagesAndTexts = imgAndTexts,
            audioVolume=audioVolume,
            maxVideoLength=maxVideoLength,
            videoSavePath=videoSavePath,
            bgMusicType=bgMusicType,
        )
        return default_videoSavePath
    except BaseException as exception:
        return f"Exception Name: {type(exception).__name__}\nException Desc: {exception}"

# driver function
if __name__ == '__main__':
	app.run(debug = True)