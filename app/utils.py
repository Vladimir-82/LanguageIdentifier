from gtts import gTTS
from io import BytesIO



def record_track(text: str, lang: str):
    mp3_fp = BytesIO()
    tts = gTTS(text, lang=lang)
    tts.write_to_fp(mp3_fp)
    return mp3_fp


