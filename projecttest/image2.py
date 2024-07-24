from tkinter import Tk, Button, Label
from tkinter import filedialog
from PIL import Image, ImageTk
from io import BytesIO

window = Tk()
window.title("Image Viewer")

# Global variable to store the image data
image_data = None

def open_image():
    global image_data
    
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg; *.jpeg; *.png")])

    # Check if a file was selected
    if file_path:
        # Read the image file as bytes
        with open(file_path, "rb") as file:
            image_data = file.read()

        # Display the image
        display_image()

def display_image():
    global image_data
    
    if image_data:
        # Create a PIL Image object from the image data
        image = Image.open(BytesIO(image_data))
        
        # Resize the image if needed
        image = image.resize((300, 300))
        
        # Convert the PIL Image to a Tkinter-compatible format
        tk_image = ImageTk.PhotoImage(image)
        
        # Create a label to display the image
        image_label = Label(window, image=tk_image)
        image_label.pack()

# Button to open the image file dialog
open_button = Button(window, text="Open Image", command=open_image)
open_button.pack()

# Call the display_image() function initially to show any existing image
display_image()

window.mainloop()
