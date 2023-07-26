import tkinter as tk
from PIL import Image, ImageTk
import subprocess

class ImageViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Assembly Step Query Tool")
        self.geometry("800x500")

        # List of image paths
        self.image_paths = [f"./Resized StepImage/Step ({i}).png" for i in range(1, 8)]
        self.current_index = 0

        self.create_widgets()

    def create_widgets(self):
        # Label to display the image
        self.image_label = tk.Label(self)
        self.image_label.pack(pady=10)

        # Entry and confirm button for input page
        self.entry_label = tk.Label(self, text="Assembly Step Querying (1-8):")
        self.entry_label.pack(pady=10)
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_var)
        self.entry.pack()
        self.confirm_button = tk.Button(self, text="Confirm", command=self.show_image)
        self.confirm_button.pack(pady=10)

        # Buttons to navigate to the previous and next images
        self.prev_button = tk.Button(self, text="Previous", command=self.show_previous_image)
        self.prev_button.pack(side=tk.LEFT, padx=20, pady=10)
        self.next_button = tk.Button(self, text="Next", command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT, padx=20, pady=10)

        self.show_image()

    def show_image(self):
        try:
            index = int(self.entry_var.get())
            if 1 <= index <= 8:
                self.current_index = index - 1
                image_path = self.image_paths[self.current_index]
                image = Image.open(image_path)
                photo = ImageTk.PhotoImage(image)
                self.image_label.configure(image=photo)
                self.image_label.image = photo

                # Call detect.py and pass the index
                subprocess.Popen(["python", "detect.py", "--index", str(index)])
        except ValueError:
            pass

    def show_previous_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            image_path = self.image_paths[self.current_index]
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo

            # Update the entry field with the new index
            self.entry_var.set(str(self.current_index - 1))

    def show_next_image(self):
        if self.current_index < len(self.image_paths) - 1:
            self.current_index += 1
            image_path = self.image_paths[self.current_index]
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo

            # Update the entry field with the new index
            self.entry_var.set(str(self.current_index + 1))

if __name__ == "__main__":
    app = ImageViewer()
    app.mainloop()
