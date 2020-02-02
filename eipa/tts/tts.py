#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 00:39:03 2019

@author: Aradhya Deolekar, Reuel D'silva (@reuelrds)
"""

from pathlib import Path
from time import sleep

from gtts import gTTS
import pygame


# TODO: define a function to handle longer text sentences


pygame.mixer.init()
path = str(Path(__file__).parent / "outputs" / "output.mp3")


def play(text):
    """Convert and play a text string.

    Converts the input text to voice using Google Text-to-Speech API and
    plays the output.

    Args:
        text: A String to be converted to Voice.
    """

    output = gTTS(text, lang="en-us", slow=False)
    output.save(path)

    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        sleep(1)


if __name__ == "__main__":
    play("The quick brown fox jumped over the lazy dog.")
