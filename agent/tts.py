import io
from gtts import gTTS


def synthesize(text: str) -> bytes:
    tts = gTTS(text=text, lang="en", slow=False)
    buffer = io.BytesIO()
    tts.write_to_fp(buffer)
    buffer.seek(0)
    return buffer.read()