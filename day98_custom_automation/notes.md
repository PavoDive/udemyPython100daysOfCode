# Custom Automation

Automate some aspect of your life using python.

You've learnt about automation with Python and Selenium. It's your turn to get creative and automate some aspect of your life using what you have learnt.

This could be an aspect of your job, your schoolwork, your home, your chores. Think about your week and everything that you do on a regular basis, when do you feel like a robot? Which jobs do you find tedious and boring? Can it be automated?

Here are some stories for inspiration:

+ Automate an email to your boss to ask for a raise every 3 months. =)
+ Automate your lights so they switch on when your phone is within the radius of your house.
+ Automatically organise the files in your downloads folder based on file type.
+ Automate your gym class bookings.
+ Automate your library book renewals.
+ Automate your job.
+ Automate your home chores.

Personally, I had a job in a hospital where I had to arrange all the doctors' shifts in my department (normal day, long day, night shift). It would depend on when they wanted to take annual leave/vacation and the staffing requirements. It started out in an Excel spreadsheet, by the time I was done with it, it was fully automated with Python and doctors were able to view a live version of the rota to see when they can take time off. The code took an evening to write and it saves me 3 hours per week. (More time to watch Netflix and eat ice cream).

Once you're done with the assignment, let us know what you automated in your life and maybe it will inspire another student!
Preguntas de esta tarea

# Reflection Time:

This is a place to journal your experience of completing this project. This will help you figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve for the next project? What was your biggest learning from today? What would you do differently if you were to tackle this project again?

## General Approach

Every course I give I have to give students a certificate of completion. In the certificate there are some fixed elements, such as the style and text describing the course, but the names, dates and id numbers of students change. That can be quite a chore! I plan to use python to integrate with inkscape and automate it.

Ideas:

+ OOP as much as possible.
+ tkinter for nice UI for taking:
    + filename of names and IDs.
	+ filename of template.
    + X and Y location of Name field.
	+ X and Y location of ID field

## Implementation Details

+ name_position = 567, 267
+ id_position = 567, 399
+ I created a Writer class that does:
    + reads the csv file with names
	+ loads the template (PIL)
	+ draws the name and id to the file
	+ saves the file to the output path
+ I created an App class that:
    + creates the widgets
	+ gets the file paths and output path
	+ instantiates Writer as an attribute
	+ passes the paths and files inputted by user to the Writer instantiation
	+ calls the Writer.write_certificates() method to actually save the images.
+ This was fun and workable!
