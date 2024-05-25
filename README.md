# Reddit TTS Bot

Facilitates the creation of a bot that stitches together narratives from Reddit which have been converted to spoken audio and background video with added audio captions—the perfect recipe for some YouTube shorts brain rot.

**Note**: This module was thrown together rather haphazardly and thus is probably not the most efficient or well-organized. Please feel free to contribute to this project to make it better!

------

## Installation

```bash
pip install reddit-tts-bot
```

This module also requires `ffmpeg`, `portaudio`, and `geckodriver` to be installed on your system. Additionally, you'll need Firefox (for the `geckodriver` to work—the coolest part where your browser scrolls all by itself!) You can install them using the following commands:

**Linux**

```bash
sudo apt-get install ffmpeg libportaudio2 geckodriver
```

**Windows (using Chocolatey)**

```bash
choco install ffmpeg portaudio geckodriver
```

**macOS (using Homebrew)**

```bash
brew install ffmpeg portaudio geckodriver
```

These aren't the only package managers available for these operating systems. You can use any package manager you prefer.

-----

## Usage

For a more robust example, check out the driver script I wrote for this module [here](https://github.com/jacksoneshbaugh/brainrot-bot).

You can use the functionality provided by this module in different ways. The process of the creation of a video with a "narrative" (Reddit post) and background video is broken down into steps.

```python
import reddit_tts_bot as rtb

# Step 1: Pull narratives from Reddit
narratives = rtb.narrative.scrape_narratives(3)

# Now, I could do multiple things with the narratives I pulled. If I wanted to convert them to spoken audio, I could do the following:

for narrative in narratives:
    narrative.to_audio("output")

# Or, if I wanted to create a full-blown video with the narrative and background video, I could do the following:

for narrative in narratives:
    rtb.video.add_video_to_narrative(narrative, video_directory="output")

# Now in the "output" directory, I would have the videos with the narratives and background videos stitched together, along with the three WAV files from the previous loop.
```

----------------
## API Reference

### `reddit_tts_bot.narrative`

This module provides the functionality to pull narratives from Reddit. The `narrative` consists of the `Narrative` class and the `scrape_narratives()` function.

#### `narrative.Narrative`

The `Narrative` class represents a narrative that has been pulled from Reddit. It has the following attributes:

- `title`: The title of the Reddit post.
- `text`: The text of the Reddit post.
- `word_count`: The word count of the Reddit post.

Each can be accessed using either dot notation or a getter method.

`Narrative` also contains the `to_audio(file_path, max_words_per_part)` method, which converts the narrative to spoken audio (in WAV format).

##### Parameters:
- `file_path`: The path to save the WAV file to (this is the parent directory).
- `max_words_per_part`: The word limit to split the narrative into multiple parts (default is 140).

##### Returns:
- A list of the names of all the WAV files created (there would be multiple in the case of splitting the narrative into multiple parts due to the specified word limit).

#### `narrative.scrape_narratives(num_narratives, min_word_count=100, locations=["r/tifu", "r/entitledparents", "r/AmItheAsshole"])`

This function scrapes Reddit for narratives to make into shorts. It saves the titles of any unique posts to a file called `narratives.txt` in the current working directory. This is to prevent the same narrative from being pulled multiple times. It returns a list of `Narrative` objects with length equal to the specified number of narratives to pull.

##### Parameters:
- `num_narratives`: The number of narratives to pull from Reddit.
- `min_word_count`: The minimum word count for a narrative to be pulled (default is 100).
- `locations`: A list of subreddits to pull narratives from (default is `["r/tifu", "r/entitledparents", "r/AmItheAsshole"]`).

##### Returns:
- A list of `Narrative` objects.

##### Modifies:
- The `narratives.txt` file in the current working directory.

### `reddit_tts_bot.tts`

This module provides the functionality to convert text to speech. The `tts` module consists of one method, `tts()`.

#### `tts.tts(text, file_path, file_name)`

This function converts text to speech using the Google Translate Text-to-Speech API. It saves the spoken audio to a WAV file.

##### Parameters:
- `text`: The text to convert to speech.
- `file_path`: The path to save the WAV file to (this is the parent directory).
- `file_name`: The name of the WAV file to save the spoken audio to (without the ".wav" extension).

##### Returns:
- `None`

##### Creates:

- A WAV file called "`file_name`.wav" with the spoken audio in the specified directory `file_path`.

### `reddit_tts_bot.video`

This module provides the functionality to synthesize videos. The `video` module consists of three methods: `get_random_video()`, `subtitle_video()`, and `add_video_to_narrative()`.

#### `video.get_random_video()`

This function randomly selects a video from the `videos` directory to use as the background video for the narrative.

##### Important Note:
You **must** have a directory called `videos` in the current working directory with at least one video to use as the background video. Its duration should exceed 1:30, to be safe. The videos should be in a format that `moviepy` can read.

##### Returns:
- The name of the randomly selected video file.

#### `video.subtitle_video(video_file, video_directory)`

This function adds audio captions to the background video using the OpenAI Whisper API. It saves the video with the captions burned into it.

##### Parameters:
- `video_file`: The name of the video file to add captions to.
- `video_directory`: The directory where the video file is located.

##### Returns:
- `None`

##### Creates:
- A video file with the captions burned into it.
- A WAV file with the captions spoken audio (located in ".temp_captions", which is removed after the video is created).

#### `video.add_video_to_narrative(narrative, video_directory = 'output')`

This function stitches the narrative and background video together. It saves the video to the specified directory. It utilizes the other two functions in the `video` module. Since this function uses the previously-discussed `get_random_video()` function, the same warning applies (I'll copy and paste it here for convenience):

##### Important Note:
You **must** have a directory called `videos` in the current working directory with at least one video to use as the background video. Its duration should exceed 1:30, to be safe. The videos should be in a format that `moviepy` can read.

##### Parameters:
- `narrative`: The `Narrative` object to use as the narrative.
- `video_directory`: The directory to save the video to (default is "output").

##### Returns:
- `True` if the video was successfully created, `False` otherwise.

##### Creates:
- A video file with the narrative and background video stitched together (located in .temp_video, which is removed after the video is created).
- A WAV file with the spoken audio of the narrative (located in ".temp_audio", which is removed after the video is created).
- A video file with the captions burned into it, in the specified directory.

## License
This module is licensed under the GPL-3.0 License. You can find the full license [here](LICENSE).

## Contributing
Please feel free to contribute to this project! Fork this repository, make your changes, and submit a pull request. I'll review it as soon as I can.

## Contact
If you have any questions or concerns, please feel free to reach out to me at
[jacksoneshbaugh@gmail.com](mailto:jacksoneshbaugh@gmail.com). You can find my other projects on GitHub at [jacksoneshbaugh](https://github.com/jacksoneshbaugh), and my website is at [jacksoneshbaugh.github.io](https://jacksoneshbaugh.github.io).

Thanks so much! I hope you enjoy using this module as much as I enjoyed creating it.
