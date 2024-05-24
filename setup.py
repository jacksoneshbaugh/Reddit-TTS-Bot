__author__ = "Jackson Eshbaugh"
__version__ = "05/24/2024"

import os

from setuptools import setup, find_packages

setup(
    name='reddit_tts_bot',
    version='1.0.0',
    packages=find_packages(),
    description='A module that facilitates the creation of short form content from Reddit posts.',
    long_description=open(os.path.dirname(__file__) + os.sep + 'README.md').read(),
    long_description_content_type='text/markdown',
    author='Jackson Eshbaugh',
    author_email='jacksoneshbaugh@gmail.com',
    url='https://github.com/jacksoneshbaugh/reddit-tts-bot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)