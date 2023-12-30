# The Breakout Game

Using Python Turtle, build a clone of the 80s hit game Breakout.

Breakout was a hit game originally coded up by Steve Wozniak before he and Jobs started Apple. It's a simple game that is similar to Pong where you use a ball and paddle to break down a wall. 

[Breakout Wikipedia Page](https://en.wikipedia.org/wiki/Breakout_(video_game))

You can try out the gameplay here:

https://elgoog.im/breakout/

A good starting point is to review the lessons on Day 22 when we built the Pong game. But you will have plenty of things to Google, figure out and struggle through to complete this project. Try to avoid going to a tutorial on how to build breakout, instead spec out the project, figure out how it's going to work. Write down a checklist of todos and draw out a flow chart (if it helps).

# Reflection Time

This is a place to journal your experience of completing this project. This will help you figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve for the next project? What was your biggest learning from today? What would you do differently if you were to tackle this project again?

## General Approach

+ I'll approach this completely from an OO perspective.
+ I'll make the following classes:
    + wall / bricks
	+ ball
	+ paddle
	+ scoreboard
	+ screen: the overall screen of the game
+ Things to be aware of:
    + If the player's paddle misses the ball's rebound, they will lose a turn.
	+ The player has three turns to try to clear two screens of bricks. 
	+ Yellow bricks earn one point each, green bricks earn three points, orange bricks earn five points and the top-level red bricks score seven points each.
	+ The paddle shrinks to one-half its size after the ball has broken through the red row and hit the upper wall. 
	+ Ball speed increases at specific intervals: after four hits, after twelve hits, and after making contact with the orange and red rows. 
	+ It's not stated anywhere, but it seems from the google image breakout game, that the ball randomly bounces with positive or negative incidence angle.

## Implementation Details 

+ I couldn't find how to actually remove a brick (turtle) from the screen upon being impacted by the ball, so I had to use a very dirty trick in the `.kill_brick()` method: sending it to coordinates -1000, -1000. 🤷🏽‍♂️
+ I had forgotten how unresponsive the paddle is, so I increased the number of "lives" to 6.
