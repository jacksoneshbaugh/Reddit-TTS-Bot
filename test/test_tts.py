import unittest
import os

from reddit_tts_bot import tts
from voicebox.tts.gtts import gTTS
from voicebox.tts.espeakng import ESpeakNG, ESpeakConfig


class TTSTest(unittest.TestCase):
    def test_tts(self):
        tts.tts(gTTS(), "This is a test of Google Translate TTS.", f"{os.getcwd()}{os.sep}tts", "test1")
        assert os.path.isfile(f"{os.getcwd()}{os.sep}tts{os.sep}test1.wav")

        # ESpeakNG must be installed.
        tts.tts(ESpeakNG(), "This is a test of ESpeakNG TTS.", f"{os.getcwd()}{os.sep}tts", "test2")
        assert os.path.isfile(f"{os.getcwd()}{os.sep}tts{os.sep}test2.wav")


if __name__ == '__main__':
    unittest.main()
