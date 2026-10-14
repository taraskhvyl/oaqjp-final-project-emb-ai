import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    res = requests.post(url, json = payload, headers = headers)
    res = json.loads(res.text)

    predictions = res['emotionPredictions'][0]
    emotions = predictions['emotion']

    dominant_emotion = max(emotions, key = emotions.get)

    final = {
        'dominant_emotion': dominant_emotion
    }

    for key, value in emotions.items():
        final[key] = value

    return final