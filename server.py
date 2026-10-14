from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detect():
    text = request.args.get("textToAnalyze")
    r = emotion_detector(text)

    if r['dominant_emotion'] is None:
        return 'Invalid text! Please try again!.'

    return r

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == '__main__':  
   app.run()  