# Automatic Speech Recogntion (ASR) Module

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This module takes in the user's speech and transcribes it to text using Google Speech Recognition API provided by SpeechRecognition package.

## Requirements:
+ Python 3
+ SpeechRecognition 3.8.1+  
+ PyAudio 0.2.11+  

_**Note:** For more information refer to [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) project page._

## To Run this:
```
python asr.py
```

## Example
```
>>> from asr import listen
>>> listen()

Say something!
Transcribing...
'The quick brown fox jumped over the lazy dog'
```