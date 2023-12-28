import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont


def select_file():
    global file_path
    file_path = filedialog.askopenfilename()
    label_path.config(text=f"Selected File: {file_path}")

    # Display the image
    try:
        image = Image.open(file_path)
        image = image.resize((450, 450), Image.ANTIALIAS)  # Adjust the size as needed
        tk_image = ImageTk.PhotoImage(image)
        label_image.config(image=tk_image)
        label_image.image = tk_image  # Keep a reference to prevent garbage collection
    except Exception as e:
        print(f"Error loading image: {e}")

def quit_app():
    root.destroy()

def print_confirmation():
    global inp
    global align
    inp = watermark_text.get(1.0, "end-1c")
    align = watermark_alignment.get() 
    confirmation_label.config(text = f"Provided Input: '{inp}', to be located in {align}.") 
    button_process.config(state = "active")
    
def process_image():
    global file_path
    global inp
    global align

    img = Image.open(file_path)
    w, h = img.size
    alignment = {"Top-Left": (10, 10), "Top-Right": (w-10, 10), "Bottom-Left": (10, h-10), "Bottom-Right": (w-10, h-10)}
    anchors = {"Top-Left": "lt", "Top-Right": "rt", "Bottom-Left": "lb", "Bottom-Right": "rb"}
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size = 18)
    # draw.text((x, y),"Sample Text",(r,g,b))
    location = alignment[align]
    draw.text(location, inp, (0,0,0), font=font, anchor = anchors[align])
    output_path = filedialog.asksaveasfile(mode = "w", defaultextension = (".jpg"))
    img.save(output_path)
    button_process.config(state = "disabled")
    
# define possible alignment options:
alignments = ["Top-Left", "Top-Right", "Bottom-Left", "Bottom-Right"]

# Create the main window
root = tk.Tk()
root.title("The Watermarker App")
root.geometry('650x650')

# Label in grid position 0, 0
label_welcome = tk.Label(root, text="Welcome to the watermarker app!")
label_welcome.grid(row=0, column=0, columnspan = 3)

# Button to select a file in grid position 1, 0
button_select = tk.Button(root, text="Select File", command=select_file)
button_select.grid(row=1, column=0, columnspan = 3)

# Label to display the path of the selected file in grid position 2, 0
label_path = tk.Label(root, text="Selected File: ", wraplength = 450)
label_path.grid(row=2, column=0, columnspan = 3)

# Image display in grid position 3, 0
label_image = tk.Label(root)
label_image.grid(row=3, column=0, columnspan = 3)

# get watermark text in grid position 4, 0
watermark_text = tk.Text(root, height = 1, width = 32)
watermark_text.grid(row = 4, column = 0)

# get watermark alignment in grid position 4, 1
watermark_alignment = ttk.Combobox(root, width = 12, values=alignments, state="readonly")
watermark_alignment.grid(row = 4, column = 1)
watermark_alignment.set(alignments[0])

# confirm button for watermark text
watermark_confirm = tk.Button(root, text = "Submit", command = print_confirmation)
watermark_confirm.grid(row = 4, column = 2)

# print watermark chain in grid position 5, 0
confirmation_label = tk.Label(root)
confirmation_label.grid(row = 5, column =  0, columnspan = 3)

# Quit button in grid position 6, 0
button_quit = tk.Button(root, text="Quit", command=quit_app)
button_quit.grid(row=6, column=0)

# Process image button in grid position 6, 1
button_process = tk.Button(root, text = "Process", command = process_image)
button_process.grid(row = 6, column = 1)
button_process.config(state = "disabled")

# Run the main loop
root.mainloop()

