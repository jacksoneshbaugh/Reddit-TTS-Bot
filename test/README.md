# Tests

Because of the complex and dynamic nature of this project, the tests I write are not entirely automated. However, I do use these tests to ensure that the project is functioning as expected. I will provide a brief overview of the tests I run and how to run them.

## `test_tts.py`

This test script tests the `reddit_tts_bot.tts` module, which has only one function: `tts()`. This function converts text to speech and saves it as a WAV file. The test script uses the `tts()` function to convert a simple text string to speech and save it as a WAV file. The test script then checks if the WAV file was created successfully. An extra validation that can be performed by the user is to listen to the WAV file and ensure that the spoken audio matches the input text.