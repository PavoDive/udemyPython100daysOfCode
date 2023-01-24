from tkinter import *

def submit():
    result = round(float(user_entry.get()) * 1.609344, 1)
    result_label.config(text = result)



window = Tk()

window.title("Mile to km converter")
window.minsize(width = 200, height = 170)
window.config(padx = 10, pady = 10)

# input box
user_entry = Entry()
user_entry.insert(END, string="0")
user_entry.grid(row = 0, column = 1)



# miles label
miles_label = Label(text = "Miles")
miles_label.grid(row = 0, column = 2)

# is equal to label
is_equal_label = Label(text = "is equal to")
is_equal_label.grid(row = 1, column = 0)

# km label
km_label = Label(text = "km")
km_label.grid(row = 1, column = 2)

# result label
result_label = Label()
result_label.grid(row = 1, column = 1)

# calculate button
calculate_button = Button(text = "Calculate", command = submit)
calculate_button.grid(row = 2, column = 1)


window.mainloop()


