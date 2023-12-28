# Typing Speed Test

A Tkinter GUI desktop application that tests your typing speed.

Using Tkinter and what you have learnt about building GUI applications with Python, build a desktop app that assesses your typing speed. Give the user some sample text and detect how many words they can type per minute.

The average typing speed is 40 words per minute. But with practice, you can speed up to 100 words per minute.

You can try out a web version here:

https://typing-speed-test.aoeu.eu/

If you have more time, you can build your typing speed test into a typing trainer, with high scores and more text samples. You can design your program any way you want.
Preguntas de esta tarea

## Reflection Time:

This is a place to journal your experience of completing this project. This will help you figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve for the next project? What was your biggest learning from today? What would you do differently if you were to tackle this project again?

## General Approach

+ I will start OO from the beggining.
    + The class will be Typing and it will inherit from Tk.
	+ The class will have the following attributes:
        + Start time
    + And the following methods:
		+ calculate time.
		+ create widgets.
		+ count words.

## Implementation Details

+ Taking last lesson OO code as a guide, I quickly coded most of the window app. 
+ I plan to calculate the wpm rating as the user types, instead of waiting for them to finish and push a button. I'll research my options and see how that can be done.
+ I think I can do it on the fly by means of a while loop: in which loop I'll get the typed text and lap the timer, so I can get instantaneous readings of the typing speed.
+ I was hitting a wall because I was using time.sleep(). This is what GPT said about: "The issue you're facing is likely due to the fact that time.sleep() is blocking the main event loop of the Tkinter application, preventing it from updating the GUI until the entire restart_test function has completed. Tkinter applications are event-driven, and blocking operations like time.sleep() can interfere with the responsiveness of the GUI. A common approach to handle delays in Tkinter without blocking the event loop is to use the after method, which schedules a function to be called after a given delay."
+ My idea of the while loop didn't actually work, because it clashes with the main loop of Tk. The solution was to use the after method to schedule recursive repetitions of the function.
+ This project was fun, and workable. I'm happy I tried to make it work via an OO approach!
