# Text to Speech (TTS) Module

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This module takes in the input text and converts it to speech using Google Text-to-Speech API provided by the gTTS library.
The output speech is then played back with the help og pygame library.

## Requirements

+ gTTS 2.1.1+
+ pygame 1.9.6+

## Example
```
>>> from tts import play
>>> play("The quick brown fox jumps over the lazy fox.")
```
