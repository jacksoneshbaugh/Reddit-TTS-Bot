__author__ = "Jackson Eshbaugh"
__version__ = "05/26/2024"
"""
This file contains code pertaining to narrative generation for the Reddit TTS Bot (including scraping from Reddit).
"""

import os
import random
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from . import tts


class Narrative:
    """
    This class represents a narrative object, which will eventually be converted to an audio file.

    Attributes:
    text: The text to be spoken
    title: The title of the story
    word_count: The word count of the story
    """

    def __init__(self, text: str, title: str):
        """
        This function initializes a Narrative object.
        :param text: The text to be spoken
        :param title: The title of the story
        """
        self.text = text
        self.title = title
        self.word_count = len(text.split())

    def title(self) -> str:
        """
        This function returns the title of the story.
        :return: The title of the story
        """
        return self.title

    def word_count(self) -> int:
        """
        This function returns the word count of the story.
        :return: The word count of the story
        """
        return self.word_count

    def text(self) -> str:
        """
        This function returns the text of the story.
        :return: The text of the story
        """
        return self.text

    def to_audio(self, file_path: str, max_words_per_part: int = 140) -> list[str]:
        """
        This function converts the text of the story to an audio file.
        :param file_path: The path to save the .wav file (parent directory)
        :return: The name(s) of the .wav file(s)
        """

        if self.word_count > max_words_per_part:
            # Split the story into parts
            parts = []
            words = self.text.split()
            part = ""
            for word in words:
                if len(part.split()) < max_words_per_part:
                    part += word + " "
                else:
                    parts.append(part)
                    part = word + " "
            parts.append(part)

            # Save each part as an audio file
            for i, part in enumerate(parts):
                tts.tts(part, file_path, self.title + " Part " + str(i + 1))
            return [self.title + ' Part ' + str(i + 1) + '.wav' for i in range(len(parts))]
        else:
            tts.tts(self.text, file_path, self.title)
            return [self.title + '.wav']


# Scrape narratives from Reddit

locations: list = ["r/tifu", "r/entitledparents", "r/AmItheAsshole"]

SCROLL_PAUSE_TIME: int = 3


def scrape_narratives(num_narratives: int, min_word_count: int = 100,
                      locations: list = locations) -> list:
    """
    This function scrapes narratives from Reddit.
    :param num_narratives: The number of narratives to scrape
    :param min_word_count: The minimum word count for a post
    :param locations: The locations (subreddits) to scrape from
    :return: A list of Narrative objects
    """

    # Create a file to hold the names of all the narratives ever scraped
    if not os.path.exists("narrative_names.txt"):
        with open("narrative_names.txt", "w") as file:
            file.write("")

    narratives = []

    # Set up the Selenium WebDriver for Firefox
    options = FirefoxOptions()
    options.add_argument("--start-maximized")
    driver: WebDriver = webdriver.Firefox(service=FirefoxService(), options=options)

    try:
        for i in range(num_narratives):
            # Choose a random location to pull stories from
            location = random.choice(locations)

            print("Scraping from " + location)

            # Open the URL
            driver.get(f"https://www.reddit.com/{location}/top/?t=all")

            # Get the articles
            posts: list[WebElement] = driver.find_elements(By.TAG_NAME, 'article')

            # Choose a random post
            post: WebElement = random.choice(posts)

            while post.get_attribute('aria-label').replace(":", "-").replace("/", "-") in open("narrative_names.txt").read():
                # Scroll the page a bit to load more content
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(SCROLL_PAUSE_TIME)
                posts = driver.find_elements(By.TAG_NAME, 'article')
                post = random.choice(posts)

            # Get the title (stored in the aria-label attribute of each post)
            title: str = post.get_attribute("aria-label").replace(":", "-").replace("/", "-")

            # Write the title to the file to keep track of which posts have been scraped
            with open("narrative_names.txt", "a") as file:
                file.write(title + "\n")

            # Get the content: go to the post's page and scrape the content
            post_url: str = post.find_element(By.TAG_NAME, "a").get_attribute("href")
            driver.get(post_url)
            time.sleep(3)  # Wait for the page to load
            post_soup: BeautifulSoup = BeautifulSoup(driver.page_source, "html.parser")
            content_elem = post_soup.select_one('.md.text-14')
            content: str = content_elem.text.strip() if content_elem else ""
            content = content.replace('\n', ' ')

            # Check if the post meets the minimum word count requirement
            if len(content.split()) < min_word_count:
                i -= 1
                continue

            # Add the title to the beginning of the content so that it is spoken
            content = title + ". " + content

            # Create a Narrative object
            narrative = Narrative(content, title)
            narratives.append(narrative)

    finally:
        driver.quit()

    return narratives
