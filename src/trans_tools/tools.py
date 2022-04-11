
from .arabic import arabic

def transliterate( text):
    
    # detect language
    # TODO
    # lang = detect_lang(text)

    lang = 'ara'

    if lang == 'ara':
        return arabic.transliterate(text)    

    return text