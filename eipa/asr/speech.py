#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:28:01 2019

@author: reuelrds
"""

import speech_recognition as sr


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("\nSay something!")
        audio = r.listen(source)
        print("Transcribing...")

    try:
        transcript = r.recognize_google(audio)
        print("Transcript: ", transcript)
        return transcript

    except sr.UnknownValueError:
        print("Could not understand audio")
        return "Could not understand audio"

    except sr.RequestError as e:
        print("""Could not request results from Google Speech
                Recognition service; {0}""".format(e))
        return "Could not get results"


if __name__ == "__main__":
    print(listen())
