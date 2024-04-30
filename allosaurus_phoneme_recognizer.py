import time
from allosaurus.app import read_recognizer, download_model
from argparse import Namespace
from tensorflow.python.client import device_lib

class allosaurus_phoneme_recognizer:
    def __init__(self):
        self.model_name = "eng2102"
        self.lang = "eng"
        self.model = ""
        self.load_model()

    def recognize(self, audio_file):
        phonemes = self.model.recognize(audio_file, self.lang, timestamp=True)
        print(phonemes)
        parsed_phonemes = self.parse_string_to_tuples(phonemes)
        return parsed_phonemes

    def load_model(self):
        download_model(self.model_name)
        # if read_recognizer(self.model_name) == None:
        #     download_model(self.model_name)

        model_config = Namespace(model=self.model_name, device_id=0, lang=self.lang, approximate=False, prior=None)

        self.model = read_recognizer(inference_config_or_name=model_config)

    def parse_string_to_tuples(self, input_string):
        lines = input_string.strip().split('\n')
        tuples_list = []
        for line in lines:
            values = line.split()
            if len(values) >= 3:
                tuples_list.append((float(values[0]), float(values[1]), values[2]))
        return tuples_list