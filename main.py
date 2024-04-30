from datetime import datetime
import os
from flask import Flask, jsonify, request
from allosaurus_phoneme_recognizer import allosaurus_phoneme_recognizer
from compress_phonemes import convert_tuple_to_phonemes

app = Flask(__name__)

recognizer = allosaurus_phoneme_recognizer()

@app.route('/recognize_audio', methods=['POST'])
def recognize_phonemes_from_audio():
    audio = request.files['audio']
    audio_path = save_audio(audio)
    phonemes = recognizer.recognize(audio_path)
    phonemes = convert_tuple_to_phonemes(phonemes)
    return jsonify(phonemes)


def save_audio(audio):
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    audio_filename = f"audio_files/audio_{current_datetime}.wav"
    os.makedirs(os.path.dirname(audio_filename), exist_ok=True)
    audio.save(audio_filename)
    return audio_filename

if __name__ == '__main__':
    app.run(debug=False)