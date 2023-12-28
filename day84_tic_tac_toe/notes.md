# Instructions

Using what you have learnt about Python programming, you will build a text-based version of the Tic Tac Toe game. The game should be playable in the command line just like the Blackjack game we created on Day 11. It should be a 2-player game, where one person is "X" and the other plays "O".

# Reflection Time:

This is a place to journal your experience of completing this project. This will help you figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve for the next project? What was your biggest learning from today? What would you do differently if you were to tackle this project again?

## General Approach

+ Create a numpy array 3 x 3 filled with " "
+ By turns, ask the player the coordinates of the cell where they want to mark their symbol
    + the symbol is already predefined as X or O to avoid managing more user input
+ check if there's a winner. If not, ask next player
+ check if board is complete, else ask next player

## Implementation notes

+ The overall implementation was easy. As always, 'the devil is in in the details', and managing user input was the most challenging part:
    + what if the user enters a non-valid string?
