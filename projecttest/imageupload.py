from tkinter import Tk, Button, Label
from tkinter import filedialog
from PIL import ImageTk, Image

def open_image():
    # Open file dialog for image selection
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg; *.jpeg; *.png")])
    
    # Create a PIL Image object from the selected file
    image = Image.open(file_path)
    
    # Resize the image if needed
    # image = image.resize((width, height))

    
    # Create a Tkinter-compatible image object
    tk_image = ImageTk.PhotoImage(image)
    
    # Update the label with the new image
    profile_image.config(image=tk_image)
    profile_image.image = tk_image

# Create the Tkinter window
window = Tk()

# Create a button for image selection
upload_button = Button(window, text="Upload Image", command=open_image)
upload_button.pack()

# Create a label to display the selected image
profile_image = Label(window)
profile_image.pack()

# Start the Tkinter event loop
window.mainloop()
