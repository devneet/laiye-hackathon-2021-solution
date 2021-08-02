def translateText(text_to_be_translated,destination_language):

    from googletrans import Translator

    translator = Translator()
    return translator.translate(text_to_be_translated,dest=destination_language).text

def detectLanguage(text_to_be_detected):

    from googletrans import Translator

    translator = Translator()
    return translator.detect(text_to_be_detected).lang