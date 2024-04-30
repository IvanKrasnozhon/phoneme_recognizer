import json


def convert_to_basic_phonemes(input_phonemes):
    # Створення словника відповідностей між вхідними та основними фонемами
    phoneme_mapping = {
        'a': 'aa',
        'aː': 'aa',
        'b': 'PP',
        'd': 'DD',
        'd̠': 'DD',
        'e': 'E',
        'eː': 'E',
        'e̞': 'E',
        'f': 'FF',
        'h': 'CH',
        'i': 'I',
        'iː': 'I',
        'j': 'CH',
        'k': 'kk',
        'kʰ': 'kk',
        'l': 'nn',
        'm': 'PP',
        'n': 'nn',
        'o': 'O',
        'oː': 'O',
        'p': 'PP',
        'pʰ': 'PP',
        'r': 'RR',
        's': 'SS',
        't': 'DD',
        'tʰ': 'DD',
        't̠': 'DD',
        'u': 'U',
        'uː': 'U',
        'v': 'FF',
        'w': 'O',
        'x': 'kk',
        'z': 'SS',
        'æ': 'E',
        'ð': 'TH',
        'øː': 'E',
        'ŋ': 'nn',
        'ɐ': 'AA',
        'ɐː': 'AA',
        'ɑ': 'AA',
        'ɑː': 'AA',
        'ɒ': 'AA',
        'ɒː': 'AA',
        'ɔ': 'O',
        'ɔː': 'O',
        'ɘ': 'E',
        'ə': 'E',
        'əː': 'E',
        'ɛ': 'E',
        'ɛː': 'E',
        'ɜː': 'E',
        'ɡ': 'kk',
        'ɪ': 'I',
        'ɪ̯': 'I',
        'ɯ': 'U',
        'ɵː': 'O',
        'ɹ': 'RR',
        'ɹ̩': 'RR',
        'ɻ': 'RR',
        'ʃ': 'SS',
        'ʉ': 'U',
        'ʉː': 'U',
        'ʊ': 'U',
        'ʌ': 'U',
        'ʍ': 'CH',
        'ʒ': 'SS',
        'ʔ': 'DD',
        'θ': 'TH'
    }

    # Конвертуємо вхідні фонеми
    converted_phonemes = [phoneme_mapping[phoneme] for phoneme in input_phonemes if phoneme in phoneme_mapping]

    return converted_phonemes

def convert_tuple_to_phonemes(input_phonemes):
    print(f"Tuples len: {len(input_phonemes)}")
    
    # Read phoneme mapping from JSON file
    with open('phoneme_mapping.json', 'r', encoding='utf-8') as file:
        phoneme_mapping = json.load(file)


    # Конвертация входных фонем
    converted_phonemes = [phoneme_mapping[phoneme] for _, _, phoneme in input_phonemes if phoneme in phoneme_mapping]

    print(f"Converted phonemes: {len(converted_phonemes)}")
    for i in range(len(input_phonemes)):
        input_phonemes[i] = (input_phonemes[i][0], input_phonemes[i][1], converted_phonemes[i])

    return input_phonemes