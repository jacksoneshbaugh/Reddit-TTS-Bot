# TO-DO

- [x] Pull narratives to make into shorts from Reddit.
  - [x] Decide on what qualifies to be pulled into a short.
    - [x] Minimum word count = 100.
  - [x] Decide on a word limit to split into multiple shorts = 140
  - [x] Fix the issue with scraping Reddit
    - It seems that the bot doesn't find all the posts on Reddit. Is there a way to "scroll down" and load more posts?
      - Yes. Simply use Selenium to scroll down the page by executing JavaScript.
  - [x] Add functionality to export the narratives to a WAV file.

- [x] Video synthesis.
  - [x] From the pre-downloaded Minecraft parkour videos and Subway Surfers gameplay videos, randomly select one to use as the background gameplay.
  - [x] Randomly select time congruent to the length of the narrative within the gameplay video.
  - [x] Stitch the narrative and gameplay video together.
  - [x] Fix the cropping code so that the gameplay video is cropped to the correct size.
  - [x] Add audio captions to the gameplay video.
    - [x] Use OpenAI Whisper and moviepy to generate and add captions.
      - [x] Burn captions into the video as text.
- [x] Think about if and how to distribute the Python module separately from the driver code.
- [x] Write the rest of README.md.


- [ ] Add functionality to not split the videos into parts if desired
- [ ] Possibly add a splitter function that generates parts from a full video
