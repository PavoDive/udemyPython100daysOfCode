import tkinter as tk
import time
from tkinter import filedialog

class DisappearingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Disappearing Text App")
        self.root.geometry("850x650")
        self.input_text = ""
        self.equal_text = False
        self.last_change = time.time()
        self.create_widgets()

    def create_widgets(self):
        # warning label
        self.warning_label = tk.Label(self.root, text = "You better keep writing!")
        self.warning_label.grid(row = 0, column = 0, columnspan = 2)

        # accept risk button
        self.accept_button = tk.Button(self.root, text = "I understand the risks", command = self.start_typing)
        self.accept_button.grid(row = 1, column = 0, columnspan = 2)
        
        # text box where user writes
        self.write_box = tk.Text(self.root, height = 10, width = 90)
        self.write_box.grid(row  = 2, column = 0, columnspan = 2)
        self.write_box.config(state = "disabled")

        # quit button
        self.quit_button = tk.Button(self.root, text = "Quit", command = self.quit_app)
        self.quit_button.grid(row = 3, column = 0)

        # save as button
        self.save_as_button = tk.Button(self.root, text = "Save as", command = self.save_as)
        self.save_as_button.grid(row = 3, column = 1)

        # dummy label
        self.dummy_label = tk.Label(self.root)
        self.dummy_label.grid(row = 4, column = 1)
        
    def start_typing(self):
        self.write_box.config(state = "normal")
        self.input_text = self.write_box.get(1.0, "end-1c")
        self.write_box.after(500, self.kill_text)
        
    def save_as(self):
        content = self.input_text
        output_path = filedialog.asksaveasfile(mode = "w", defaultextension = (".txt"))
        output_path.write(content)
        output_path.close()

    def compare_texts(self):
        new_text = self.write_box.get(1.0, "end-1c")
        if new_text == self.input_text:
            self.equal_text = True
        else:
            self.equal_text = False
            self.input_text = new_text
            self.last_change = time.time()
            
    def kill_text(self):
        self.compare_texts()
        if self.equal_text == True and ((time.time() - 5) >= self.last_change):
            self.write_box.delete(1.0, "end-1c")
        self.dummy_label.config(text = f"equal_text = {self.equal_text}, and difftime = {time.time() - self.last_change:.2f}")
        self.write_box.after(500, self.kill_text)

    def quit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DisappearingApp(root)
    root.mainloop()
