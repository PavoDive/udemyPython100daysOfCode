from openai import OpenAI
from password import oa_org_id, oa_api_key
import tkinter as tk
from pdfminer.high_level import extract_text
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import filedialog
import re

global oa_org_id
global oa_api_key

class TextToSpeech:
    def __init__(self):
        global oa_org_id
        global oa_api_key

        self.client = OpenAI(api_key=oa_api_key, organization = oa_org_id)
        self.speech_file_path = None
        self.input_text = None
        self.voice = "Male"

    def save_response(self):
        voices = {"Male": "onyx", "Female": "shimmer"}
        response = self.client.audio.speech.create(
            model = "tts-1",
            voice = voices[self.voice],
            input = self.input_text
        )
        response.stream_to_file(self.speech_file_path)

class PdfExtractor:
    def __init__(self):
        self.pdf_file_path = None
        self.extracted_text = None

    def extract_text(self):
        self.extracted_text = extract_text(self.pdf_file_path)
        self.extracted_text = re.sub("\\n\\n[0-9]+\\n\\n", "", self.extracted_text)

class PdfSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF to Speech Converter")
        self.root.geometry("650x650")
        self.create_widgets()
        self.pdf_path = None
        self.output_path = None
        self.tts = TextToSpeech()
        self.pdf_extractor = PdfExtractor()

    def create_widgets(self):
        # welcome label
        self.label_welcome = tk.Label(self.root, text = "Welcome to the PDF to Speech Converter")
        self.label_welcome.pack()
        
        # select pdf button
        self.pdf_button = tk.Button(self.root, text = "Select pdf file", command = self.pdf_select)
        self.pdf_button.pack()

        # # preview pdf
        # # creating object of ShowPdf from tkPDFViewer.
        # self.previewer = pdf.ShowPdf().pdf_view(self.root, width = 50, height = 5)
        # self.previewer.pack()
        
        # save as mp3
        self.save_mp3 = tk.Button(self.root, text = "Save to MP3", command = self.mp3_saveas)
        self.save_mp3.pack()
        self.save_mp3.config(state = "disabled")

        # a label to indicate completion
        self.completed_label = tk.Label(self.root, font = 20, fg = "red")
        self.completed_label.pack()
        
    def pdf_select(self):
        self.pdf_path = filedialog.askopenfilename()
        # self.previewer.pdf_location = self.pdf_path
        self.save_mp3.config(state = "normal")

    def mp3_saveas(self):
        # this was my original code, along with the commented part in the
        # main loop. It didn't run because the ifs are evaluated at instantiation time and not during the loops: "The issue in your code is that the if app.pdf_path: and if app.output_path: conditions are outside of the event loop (root.mainloop()), so they are executed immediately after creating the PdfSpeechApp instance, not when the user interacts with the GUI."
        # The following is the corrected code
        # self.output_path = filedialog.asksaveasfile(mode = "w", defaultextension = (".mp3"))
        if self.pdf_path:
            self.pdf_extractor.pdf_file_path = self.pdf_path
            self.pdf_extractor.extract_text()
            self.tts.input_text = self.pdf_extractor.extracted_text

            self.output_path = filedialog.asksaveasfile(mode="w", defaultextension=(".mp3"))

            if self.output_path:
                self.tts.speech_file_path = self.output_path.name
                self.completed_label.config(text = "PROCESSING... Please wait")
                self.root.update_idletasks()  # Force an update of the GUI
                self.tts.save_response()
                self.completed_label.config(text="COMPLETED")


if __name__ == "__main__":
    root = tk.Tk()
    app = PdfSpeechApp(root)
    root.mainloop()

