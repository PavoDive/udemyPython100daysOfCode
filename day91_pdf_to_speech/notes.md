# Convert PDF to Audiobook

Write a Python script that takes a PDF file and converts it into speech.

Too tired to read? Build a python script that takes a PDF file, identifies the text and converts the text to speech. Effectively creating a free audiobook.

AI text-to-speech has come so far. They can sound more lifelike than a real audiobook.

Using what you've learnt about HTTP requests, APIs and Python scripting, create a program that can convert PDF files to speech.

You right want to choose your own Text-To-Speech (TTS) API. But here are some you can consider:

http://www.ispeech.org/api/#introduction

https://cloud.google.com/text-to-speech/docs/basics

https://aws.amazon.com/polly/
Preguntas de esta tarea

# Reflection Time:

This is a place to journal your experience of completing this project. This will help you figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve for the next project? What was your biggest learning from today? What would you do differently if you were to tackle this project again?

# General Approach

+ Full OO
+ Create a class for OpenAI:
    + Authentication
    + Text to speech
	+ Save to file, provided a filepath
+ Create a class for converting pdf to text, provided a filepath
+ create a class for all the tkinter business:
    + all labels and buttons
    + a button to pick the pdf file. The path will be passed to the pdf instance
	+ Another button to provide a save-as path for the mp3 file.
	
# Implementation Details

+ I wanted to provide the user with a preview of the pdf file, and planned to do so with the tkPDFViewer package. Unfortunately, the package is in alpha stage and doesn't seem to have a method to update the path to the pdf file. I will just cancel that idea and comment out all related code.
+ The app run well when executed line by line, but didn't produce the expected output when run as `python3 main.py`. This was caused by some if statements that were outside of the mainloop. The solution was putting them inside one the of methods of the class.
+ Classes (such as the app) can have atrributes that are **other** classes: that's the way to "communicate" results between them.
+ There are some "obscure" things about tkinter that are very difficult to understand, such as the root.update_idletasks() method, that at first seemed absolutely unnecessary.
+ Overall, this project seemed simple and easy, but I got bogged by the inter-class interactions. I now understand that it shouldn't be difficult!
