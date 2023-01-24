import tkinter

def button_clicked():
#    print("I got clicked")
    user_input = input.get()
    my_label.config(text = f"This was the input: {user_input}")

window = tkinter.Tk()

window.title("My first GUI program")

# minsize guarantees the smallest possible size that accommodates all buttons and stuff
window.minsize(width = 600, height = 500) 

# label
my_label = tkinter.Label(text = "I am a label", font = ("Arial", 24, "bold"))

# label properties can be changed as if they were a dictionary:
my_label["text"] = "New text"
# or also by using the config method:
my_label.config(text = "This new text")
my_label.pack() # pack() is a **layout manager**, it's what actually puts laben in the window.
# pack() puts everything below the previous one (centered by default).
# There are other layout managers: place() puts the widget at given coordinates x, y (starting from top left at 0, 0).
# the other layout manager is grid(). It works by placing things in a row, column grid:
# my_label.grid(row=0, column=0) will be the top-left corner. grid() positions are relative to other widgets in the window.
# pack() cannot be used when grid() was used


# button
   
my_button = tkinter.Button(text = "click me", command = button_clicked)
my_button.pack()

# Entry
input = tkinter.Entry()
input.pack()
# This line of code will be moved **inside** the button_clicked function
# user_input = input.get()


window.mainloop() # keeps the process awake. HAS to be at the very end
