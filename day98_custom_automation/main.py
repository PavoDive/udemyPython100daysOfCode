import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
import pandas as pd

class Writer:
    def __init__(self):
        self.input_file = None
        self.name_position = (567, 267)
        self.id_position = (567, 399)
        self.output_path = None
        self.template_path = None

    def write_certificates(self):
        df = pd.read_csv(self.input_file)
        # possible fonts: /home/gp/.local/share/fonts/Unknown Vendor/TrueType/Cinzel/Cinzel_SemiBold.ttf
        # /home/gp/.local/share/fonts/Unknown Vendor/TrueType/Island Moments/Island_Moments_Regular.ttf
        # /usr/share/fonts/opentype/urw-base35/Z003-MediumItalic.otf
        font = ImageFont.truetype("/usr/share/fonts/opentype/urw-base35/Z003-MediumItalic.otf", size=36)

        for i in range(len(df)):
            img = Image.open(self.template_path)
            self.name_position = (img.size[0] / 2, 245)
            self.id_position = (img.size[0] / 2, 390)
            draw = ImageDraw.Draw(img)
            draw.text(self.name_position, df.name.iloc[i], (0, 0, 0), font=font, anchor="mm", align = "center")
            draw.text(self.id_position, df.id_number.iloc[i].astype("str"), (0, 0, 0), font=font, anchor= "mm", align = "center")
            output_path = self.output_path+"/"+df.name.iloc[i].replace(" ", "_")+".jpg"
            img.save(output_path)
            

class DiplomatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diplomator App")
        self.root.geometry("650x650")
        self.create_widgets()
        self.template_path = None
        self.output_path = None
        self.writer = Writer()

    def create_widgets(self):
        # welcome label
        self.label_welcome = tk.Label(self.root, text = "Welcome to the Certificate Generator")
        self.label_welcome.pack()
        
        # select template button
        self.template_button = tk.Button(self.root, text = "Select template file", command = self.template_select)
        self.template_button.pack()

        # select namelist file button
        self.namelist_button = tk.Button(self.root, text = "Select namelist", command = self.namelist_select)
        self.namelist_button.pack()

        # save path
        self.save_path = tk.Button(self.root, text = "Save Path", command = self.path_saveas)
        self.save_path.pack()
        self.save_path.config(state = "disabled")

        # a label to indicate completion
        self.completed_label = tk.Label(self.root, font = 20, fg = "red")
        self.completed_label.pack()
        
    def template_select(self):
        self.template_path = filedialog.askopenfilename()
        # self.previewer.pdf_location = self.pdf_path
        self.save_path.config(state = "normal")

    def namelist_select(self):
        self.namelist_path = filedialog.askopenfilename()
        
    def path_saveas(self):
        # this was my original code, along with the commented part in the
        # main loop. It didn't run because the ifs are evaluated at instantiation time and not during the loops: "The issue in your code is that the if app.pdf_path: and if app.output_path: conditions are outside of the event loop (root.mainloop()), so they are executed immediately after creating the PdfSpeechApp instance, not when the user interacts with the GUI."
        # The following is the corrected code
        # self.output_path = filedialog.asksaveasfile(mode = "w", defaultextension = (".mp3"))
        if self.template_path:
            self.writer.template_path = self.template_path
            self.writer.input_file = self.namelist_path

            self.output_path = filedialog.askdirectory()
            
            self.writer.output_path = self.output_path

            if self.output_path:
                self.completed_label.config(text = "PROCESSING... Please wait")
                self.writer.write_certificates()

                self.root.update_idletasks()  # Force an update of the GUI
                self.completed_label.config(text="COMPLETED")


if __name__ == "__main__":
    root = tk.Tk()
    app = DiplomatorApp(root)
    root.mainloop()
