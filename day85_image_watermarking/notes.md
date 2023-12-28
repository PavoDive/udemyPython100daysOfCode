# Image Watermarking Desktop app

## Instructions

Using what you have learnt about Tkinter, you will create a desktop application with a Graphical User Interface (GUI) where you can upload an image and use Python to add a watermark logo/text.

Normally, you would have to use an image editing software like Photoshop to add the watermark, but your program is going to do it automatically.

Use case: e.g you want to start posting your photos to Instagram but you want to add your website to all the photos, you can now use your software to add your website/logo automatically to any image.

A similar online service is: https://watermarkly.com/

You might need:

https://pypi.org/project/Pillow/

https://docs.python.org/3/library/tkinter.html

and some Googling.

## Reflection Time:

This is a place to journal your experience of completing this project. This will help you figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve for the next project? What was your biggest learning from today? What would you do differently if you were to tackle this project again?

## General Approach

+ Create a GUI to allow user to upload image
+ Ask user to provide 9 possible points to put the watermark: left-center-right x top-middle-bottom
+ Ask user to provide the watermark text
+ use some sort of imagemagick library (will have to research it) to actually write the watermark
+ Present the user with the preview and ask for any changes
+ Commit the file to disk afetr asking for the path

## Implementation details

+ tkinter is difficult. I struggled a lot trying to get used to the way it works, not all the options and methods seemed intuitive to to me.
+ I also struggled with the appearance of the window, trying to get it decent enough.
+ I used a lot of things trying to make this app a really useful thing, and not only a mere homework.
+ Overall I'm not very satisfied with the appearance of the app, but at this stage I rather learn the code, and when need comes, I'll learn to make it 2pretty".
+ I had to use global variables, which I don't like. It seems another approach would have been using classes, but I wasn't really sure how to approach the problem from an OO perspective.
+ After I finished, I asked GPT to convrt my code to OO, to see the differences. I has to tweak and debug some parts of the code to make it work, which gave me some additional understanding about how it works, and --I think, the confidence to attempt it myself next time.
+ Probably what I struggle the most with OO is visualizing the overall code in the first place, I'll try to work on that, because evidently the OO code is cleaner and seems to be easier to maintain.
