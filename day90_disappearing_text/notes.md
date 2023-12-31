# Disappearing Text Writing App

A writing app where if you stop typing, your work will disappear.

For most writers, a big problem is writing block. Where you can't think of what to write and you can't write anything.

One of the most interesting solutions to this is a web app called The Most Dangerous Writing App, an online text editor where if you stop writing, all your progress will be lost.

A timer will count down and when the website detects the user has not written anything in the last 5/10 seconds, it will delete all the text they've written so far.

Try it out here:

https://www.squibler.io/dangerous-writing-prompt-app

You are going to build a desktop app that has similar functionality. The design is up to you, but it should allow a user to type and if they stop for more than 5 seconds, it should delete everything they've written so far.
Preguntas de esta tarea

# Reflection Time:

This is a place to journal your experience of completing this project. This will help you figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve for the next project? What was your biggest learning from today? What would you do differently if you were to tackle this project again?

## General Approach

+ Use tkinter Text widget `.get()` method and replace "previous" get with new one after comparing them, if they are different. If they are the same, trigger an `after(5000)` method in which a new comparisson is done. If there are no changes, a clearing command is issued over the text field.

## Implementation notes

+ I just realized there's an `edit_modified()` method for the Text widget. I could have used it to avoid comparing the texts, which is basically a poor re-implementation of the function. But the best code is the one that works 😉.
+ I completed this project with little effort, taking as reference the OO solutions to the image watermarking app and to the typing speed app of previous lessons.
