# Instructions

You will use what you've learnt to create a text-based (command line) program that takes any String input and converts it into Morse Code.

You've created plenty of text-based programs in Days 1 -10, so look back at some of those projects if you don't remember what a text-base program looks like.

[Wikipedia Entry for Morse Code](https://en.wikipedia.org/wiki/Morse_code)

The design, functionality, code style is all up to you. You're wearing the big-girl/big-boy pants now. So you get to decide.
Preguntas de esta tarea

## Reflection Time:

This is a place to journal your experience of completing this project. This will help you figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve for the next project? What was your biggest learning from today? What would you do differently if you were to tackle this project again?

# My text (this was copied to the homework box)

## General approach

+ ask the user for the string to convert
+ run a function in which:
    + I will load the morse codes in a pandas dataframe.
    + convert the input text by user to a pandas dataframe (1 column)
    + merge both dataframes, so I'll end with the morse code for the input text
    + convert the morse column to a string y provide it back to the user
+ ask the user if they want to translate another string or exit.

## Implementation notes

+ I was struggling to load the quote character to the csv table and then read it. I opted to read the asterisk symbol instead, and will implement a string replacement that changes all quotes (single and double) to asterisks.
+ I added the deunicode package to convert accented characters to ascii equivalents (the morse for those is complicated and not standardized.
+ It worked nicely and the code is only 37 lines (most of it is the re-implementation of the menu function.
