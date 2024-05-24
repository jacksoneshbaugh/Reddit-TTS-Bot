# Reddit TTS Bot

Facilitates the creation of a bot that stitches together narratives from Reddit which have been converted to spoken audio and background video with added audio captions—the perfect recipe for some YouTube shorts brain rot.

## Installation

```bash
pip install reddit_tts_bot
```

This module also requires `ffmpeg`, `portaudio`, and `geckodriver` to be installed on your system. You can install them using the following commands:

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

## Usage

You can use the functionality provided by this module in different ways. The process of the creation of a video with a "narrative" (Reddit post) and background video is broken down into steps.

### Step 1: Pull Narratives

Pull narratives from Reddit to make into shorts.

```python
import reddit_tts_bot as rtb

# Pull 3 narratives from any of the subreddits in the (unwritten) list of subreddits `list`.

```

