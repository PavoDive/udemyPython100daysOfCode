import tkinter as tk
import time
import random

class TypingspeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Typing Speed App")
        self.root.geometry("850x650")
        self.start_time = time.time()
        self.input_text = ""
        self.stopped = False
        self.texts = ["""We must not underrate the gravity of the task which lies before us or the temerity of the ordeal, to which we shall not be found unequal. We must expect many disappointments, and many unpleasant surprises, but we may be sure that the task which we have freely accepted is one not beyond the compass and the strength of the British Empire and the French Republic.""",
                      """… from these honored dead we take increased devotion to that cause for which they heregave the last full measure of devotion; that we here highly resolve that the dead shall not have died in vain; that the Nation shall under God have a new birth of freedom, and that Governments of the people, by the people and for the people shall not perish from the earth.""",
                      """We choose to go to the moon. We choose to go to the moon in this decade and do the other things, not because they are easy, but because they are hard, because that goal will serve to organize and measure the best of our energies and skills, because that challenge is one that we are willing to accept, one we are unwilling to postpone, and one which we intend to win, and the others, too."""]
        self.create_widgets()

    def create_widgets(self):
        # welcome label
        self.label_welcome = tk.Label(self.root, text = "Welcome to the Typing speed App!")
        self.label_welcome.grid(row = 0, column = 0, columnspan = 3)

        # text to be copied
        self.original_text = tk.Label(self.root, wraplength = 750)
        self.original_text.grid(row = 1, column = 0, columnspan = 3)

        # text box where user writes
        self.copied_text = tk.Text(self.root, height = 10, width = 90)
        self.copied_text.grid(row = 2, column = 0, columnspan = 3)

        # label with the speed output
        self.output_label = tk.Label(self.root, wraplength = 500, font = ("Helvetica", 18, "bold"))
        self.output_label.grid(row = 3, column = 0, columnspan = 3)

        # restart button
        self.restart_button = tk.Button(self.root, text = "Restart", command = self.restart_test)
        self.restart_button.grid(row = 4, column = 0)

        # stop button
        self.stop_button = tk.Button(self.root, text = "Stop", command = self.stop_test)
        self.stop_button.grid(row = 4, column = 1)

        # quit button
        self.quit_button = tk.Button(self.root, text = "Quit", command = self.quit_app)
        self.quit_button.grid(row = 4, column = 2)

    def restart_test(self):
        # suggested by GPT, because I was using time.sleep() that interferes with tkinter
        self.stopped = False
        self.output_label.configure(text = "")
        self.original_text.configure(text="We'll start in three seconds, get ready!", fg="red", font=("Helvetica", 34, "bold"))
        self.original_text.after(1000, self.show_countdown, 3)

    def show_countdown(self, count):
        # suggested by GPT, because I was using time.sleep() that interferes with tkinter
        if count > 0:
            self.original_text.configure(text=str(count), fg="red", font=("Helvetica", 40, "bold"))
            self.original_text.after(1000, self.show_countdown, count - 1)
        else:
            self.original_text.configure(text=random.choice(self.texts), fg="black", font=("Helvetica", 16, "normal"))
            self.start_time = time.time()
            self.original_text.after(250, self.update_output)

    def update_output(self):
        if self.stopped == False:
            self.input_text = self.copied_text.get(1.0, "end-1c")
            words = len(self.input_text.split())
            chars = len(self.input_text)
            elapsed = (time.time() - self.start_time) / 60
            wpm = words / elapsed
            cpm = chars / elapsed
            self.output_label.configure(text = f"Your actual WPM is: {wpm:.1f} words per minute; CPM: {cpm:.1f} chars per minute.")
            self.output_label.after(250, self.update_output)
            
    def stop_test(self):
        self.stopped = True
        self.copied_text.delete(1.0, "end-1c")

    def quit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingspeedApp(root)
    root.mainloop()
        
        
