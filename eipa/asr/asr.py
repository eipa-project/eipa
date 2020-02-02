#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:28:01 2019.

@author: Reuel D'silva (@reuelrds)
"""

import speech_recognition as sr


def listen():
    """Transcribes Audio to text.

    The Function takes in the user's speech using the microphone
    and transcribes it to text using Google Speech Recognition API
    provided by SpeechRecognition package.

    Returns:
        transcript: The transcribed text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("\nSay something!")
        audio = r.listen(source)
        print("Transcribing...")

    try:
        transcript = r.recognize_google(audio)
        return transcript

    except sr.UnknownValueError:
        return "Could not understand audio"

    except sr.RequestError as e:
        return """"Could not request results from Google Speech
            Recognition service; {0}""".format(e)


if __name__ == "__main__":
    print(listen())
