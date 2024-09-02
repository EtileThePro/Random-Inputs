from gtts import gTTS
import os
import tempfile

def play_tts(message):
    tts = gTTS(message)
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        tts.save(fp.name)
        os.system(f"mpg123 {fp.name}")
        os.remove(fp.name)