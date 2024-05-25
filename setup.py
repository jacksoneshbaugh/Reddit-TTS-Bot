__author__ = "Jackson Eshbaugh"
__version__ = "05/24/2024"

import os

from setuptools import setup, find_packages

setup(
    name='reddit_tts_bot',
    version='1.0.6',
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
    install_requires=[
        'attrs>=23.2.0',
        'beautifulsoup4>=4.12.3',
        'bs4>=0.0.2',
        'cachetools>=5.3.3',
        'certifi>=2024.2.2',
        'cffi>=1.16.0',
        'charset-normalizer>=3.3.2',
        'click>=8.1.7',
        'decorator>=4.4.2',
        'filelock>=3.14.0',
        'fsspec>=2024.5.0',
        'gTTS>=2.5.1',
        'h11>=0.14.0',
        'idna>=3.7',
        'imageio>=2.34.1',
        'imageio-ffmpeg>=0.4.9',
        'Jinja2>=3.1.4',
        'joblib>=1.4.2',
        'llvmlite>=0.42.0',
        'MarkupSafe>=2.1.5',
        'more-itertools>=10.2.0',
        'moviepy>=1.0.3',
        'mpmath>=1.3.0',
        'networkx>=3.3',
        'nltk>=3.8.1',
        'numba>=0.59.1',
        'numpy>=1.26.4',
        'openai-whisper>=20231117',
        'opencv-python>=4.9.0.80',
        'outcome>=1.3.0.post0',
        'pandas>=2.2.2',
        'pedalboard>=0.9.6',
        'pillow>=10.3.0',
        'proglog>=0.1.10',
        'pycparser>=2.22',
        'pydub>=0.25.1',
        'PySocks>=1.7.1',
        'python-dateutil>=2.9.0.post0',
        'pytz>=2024.1',
        'regex>=2024.5.15',
        'requests>=2.32.2',
        'scipy>=1.13.0',
        'selenium>=4.21.0',
        'six>=1.16.0',
        'sniffio>=1.3.1',
        'sortedcontainers>=2.4.0',
        'sounddevice>=0.4.6',
        'soupsieve>=2.5',
        'sympy>=1.12',
        'tiktoken>=0.7.0',
        'torch>=2.3.0',
        'tqdm>=4.66.4',
        'trio>=0.25.1',
        'trio-websocket>=0.11.1',
        'typing_extensions>=4.11.0',
        'tzdata>=2024.1',
        'urllib3>=2.2.1',
        'voicebox-tts>=0.0.7',
        'wsproto>=1.2.0'
    ],
)
