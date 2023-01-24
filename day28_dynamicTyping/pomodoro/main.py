from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 # this one is in order to keep track of the check marks and whether it's work or rest
one_check_mark = "✔" 
check_mark = "✔"
timer = None # this is so we can access the variable outside of the count_down function
# ---------------------------- TIMER RESET ------------------------------- # 
# This one is fairly obvious and was easy to code
def reset_timer():
    global check_mark
    global reps
    window.after_cancel(timer)
    timer_label.config(text = "Timer", fg = GREEN)
    canvas.itemconfig(timer_text, text = "00:00")
    check_mark = "✔"
    check_mark_label.config(text = "")
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- #
# this helper function is because I didn't use the modulo as Angela did.
def add_check_mark():
    global check_mark
    check_mark_label.config(text = check_mark)
    check_mark += one_check_mark

# this function wasn't so obvious when Angela introduced it, but it seems
# pretty obvious now that I read it afterwards
def start_timer():
    global reps

    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text = "Long Break", fg = RED)
        add_check_mark()
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text = "Short Break", fg = PINK)
        add_check_mark()
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text = "Work hard!", fg = GREEN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# this is the workhorse in this app. The key thing is how she called
# **recursively** count_down() in the window.after() call. She didn't quite
# explain it, and honestly I still haven't got to grips with that
# recursive call. I understand that it had to be assinged to a variable (timer),
# so that I could be used in the window.after_cancel() call, but back when it
# was done, it was kind of a sorcery.
def count_down(count):
    global timer

    count_minute = floor(count / 60)
    count_seconds = count % 60
    # Angela had a very hacky solution to display the minutes:seconds with padding zeroes
    # and using dynamic typing, but it was too hacky (an if statement changing the number for a string if it was less than 10).
    # I do prefer my solution.
    canvas.itemconfig(timer_text, text = f"{count_minute:02}:{count_seconds:02}") # this is setting the new text to the label
    if count > 0: # this is to avoid it going below 0
        timer = window.after(3, count_down, count - 1) # this method of window is to do fun(args) after miliseconds
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
# All this block is more or less the standard thing with buttons
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

timer_label = Label(text = "Timer", font = (FONT_NAME, 35, "normal"), fg = GREEN, bg = YELLOW)
timer_label.grid(row = 0, column = 1)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_image = PhotoImage(file = "tomato.png") # images should be pre-read
canvas.create_image(100, 112, image = tomato_image)
# The next call is assigned to a variable, so the canvas.itemconfig() call had
# an object to act onto
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)


start_button = Button(text = "Start", command = start_timer)
start_button.grid(row = 2, column = 0)

reset_button = Button(text = "Reset", command = reset_timer)
reset_button.grid(row = 2, column = 2)

check_mark_label = Label(fg = GREEN, bg = YELLOW, font = ("Arial", 27, "bold"))
check_mark_label.grid(row = 3, column = 1)


window.mainloop()
