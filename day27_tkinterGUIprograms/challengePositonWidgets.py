import tkinter

def button1_clicked():
    print("Button was clicked")


def button2_clicked():
    print("new button was clicked")


window = tkinter.Tk()

window.title("My first GUI program")

# minsize guarantees the smallest possible size that accommodates all buttons and stuff
window.minsize(width = 600, height = 500) 

# adding padding to all the widgets in the window:
window.config(padx = 20, pady = 20)

# label
my_label = tkinter.Label(text = "I am a label", font = ("Arial", 24, "bold"))
my_label.grid(row = 0, column = 0)

# it is possible to change the padding of a specific widget:
my_label.config(padx = 50, pady = 50)

# button 1

my_button = tkinter.Button(text = "click me", command = button1_clicked)
my_button.grid(row = 1, column = 1)

# button 2
new_button = tkinter.Button(text = "Another button", command = button2_clicked)
new_button.grid(row = 0, column = 2)

# Entry
input = tkinter.Entry()
input.grid(row = 2, column = 3)



window.mainloop() # keeps the process awake. HAS to be at the very end
