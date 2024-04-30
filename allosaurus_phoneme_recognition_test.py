import time
from allosaurus.app import read_recognizer, download_model
from argparse import Namespace

model_name = 'eng2102'
audio_file = r"D:\Downloads\ttsmaker-file-2024-4-25-19-20-43.wav"
lang = "eng"

# load your model by the <model name>, will use 'latest' if left empty
# try:
#     model = read_recognizer(model_name)
# except:
#     print(f"Failed to load model ${model_name}. Instead using universal model!")
#     model = read_recognizer()

from tensorflow.python.client import device_lib

device_lib.list_local_devices()

print(len(device_lib.list_local_devices()))

start_time = time.time()

download_model(model_name)
if read_recognizer(model_name) == None:
    download_model(model_name)

model_config = Namespace(model=model_name, device_id=0, lang=lang, approximate=False, prior=None)

model = read_recognizer(inference_config_or_name=model_config)

# run inference on <audio_file> with <lang>, lang will be 'ipa' if left empty
phonemes = model.recognize(audio_file, lang, timestamp=True)

end_time = time.time()
elapsed_time = end_time-start_time
print(f"Elapsed time: {elapsed_time}")

print(phonemes)
