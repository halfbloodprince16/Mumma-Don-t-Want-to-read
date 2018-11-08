# Mumma-Don-t-Want-to-read
Talky pypi implemeted with a frontend using flask to speech the text inserted .

Install from pypi:
	pip install talkey

If you get a talkey.base.TTSError: No supported languages error, it means that you don’t have a supported TTS engine installed. Please see below.

By default it will try to locate and use the local instances of the following TTS engines:

Flite
SVOX Pico
Festival
eSpeak
mbrola via eSpeak
Installing one or more of those engines should allow the libary to function and generate speech.

It also supports the following networked TTS Engines:

MaryTTS (needs hosting)
Google TTS (cloud hosted)


Installing TTS engines

Ubuntu/Debian:
	For festival:
	sudo apt-get install festival
	
	For flite:
	sudo apt-get install flite
	
	For SVOX Pico:
	sudo apt-get install libttspico-utils
	
	For eSpeak:
	sudo apt-get install espeak
	
	For mbrola and en1 voice:
	sudo apt-get install mbrola-en1
