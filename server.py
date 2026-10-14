"""Flask web server for the Emotion Detection application."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emot_detect():
    """Analyze the emotion of the text passed in the `textToAnalyze` query parameter.

    Returns:
        dict: Scores for anger, disgust, fear, joy and sadness, plus the
            dominant emotion (serialized to JSON by Flask).
        str: An error message if the text is blank or invalid.
    """

    text = request.args.get("textToAnalyze")
    r = emotion_detector(text)

    if r['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    return r

@app.route("/")
def render_index_page():
    """Render the home page (templates/index.html)."""
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
