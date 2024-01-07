# Image Colour Palette Generator

A website that finds the most common colours in an uploaded image.

One of my favourite websites to go to when I'm designing anything is a colour palette website called Flat UI Colors.

https://flatuicolors.com/palette/defo

It's a really simple static website that shows a bunch of colours and their HEX codes. I can copy the HEX codes and use it in my CSS or any design software.

On day 77, you learnt about image processing with NumPy. Using this knowledge and your developer skills (that means Googling), build a website where a user can upload an image and you will tell them what are the top 10 most common colours in that image.

This is a good example of this functionality:

http://www.coolphptools.com/color_extract#demo


# Reflection Time:

This is a place to journal your experience of completing this project. This will help you figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve for the next project? What was your biggest learning from today? What would you do differently if you were to tackle this project again?

## General Approach

+ Read about numpy image processing, because I don't remember a thing!
+ Use flask
    + One route for home and another for results
+ Use OOP as much as possible

# Implementation details

+ This took me a lot of time. I struggled with:
    + numpy: trying to get the frequency of the colors (tuples). I ended up using pandas, which was good to store the hex and string represntations of the RGB colors.
	+ flask - jinja: displaying the dataframe was easy, formatting it was hard.
+ I didn't use OOP, I didn't find how to 🤷🏽‍♂️.

