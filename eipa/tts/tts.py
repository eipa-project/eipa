"""
Created on Sat Nov  2 00:39:03 2019

@author: reuelrds
"""

from pathlib import Path
from time import sleep

from gtts import gTTS
import pygame


# TODO: define a function to handle longer text sentences


pygame.mixer.init()
path = str(Path(__file__).parent / "outputs" / "output.mp3")


def play(text):

    output = gTTS(text, lang="en-us", slow=False)
    output.save(path)

    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        sleep(1)


if __name__ == "__main__":
    play("The quick brown fox jumped over the lazy dog.")
