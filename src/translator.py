import transformers
from transformers import pipeline
import logging 
logging.getLogger().setLevel(logging.ERROR)

translator1 = pipeline("translation", model = "Helsinki-NLP/opus-mt-en-hi")
translator2 = pipeline("translation", model = "Helsinki-NLP/opus-mt-en-ur")
def translationHindi(text):
    if not text.strip():
        return"[Empty input]"
    
    result = translator1(text, max_length = 512)
    return result[0]['translation_text']

def translationUrdu(text):
    if not text.strip():
        return"[Empty input]"
    
    result = translator2(text, max_length = 512)
    return result[0]['translation_text']

