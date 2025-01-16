from PIL import Image
import os
import tkinter as tk
from tkinter import Tk, Label, Button, filedialog, messagebox, Entry, StringVar, ttk, IntVar
from tkinterdnd2 import DND_FILES, TkinterDnD

def get_file_creation_date(file_path):
    """Get the creation or modified date of a file."""
    return os.path.getmtime(file_path)

def sort_images_by_metadata(image_files):
    """Sort images based on file metadata."""
    return sorted(image_files, key=get_file_creation_date)

def images_to_pdf(image_files, output_pdf, progress_var):
    """Convert a list of image files into a single PDF with progress."""
    images = []
    for i, file in enumerate(image_files):
        img = Image.open(file)
        if img.mode != 'RGB':  # Convert to RGB if not already
            img = img.convert('RGB')
        images.append(img)

        # Update progress bar
        progress_var.set(int((i + 1) / len(image_files) * 100))

    if images:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        return True
    return False

def select_folder():
    """Allow the user to select a folder via a dialog."""
    folder_path = filedialog.askdirectory(title="Select Folder Containing Images")
    if folder_path:
        folder_var.set(folder_path)

def start_conversion():
    """Start the image-to-PDF conversion process."""
    folder_path = folder_var.get()
    output_name = file_name_var.get()

    if not folder_path:
        messagebox.showwarning("No Folder Selected", "Please select a folder containing images.")
        return

    if not output_name:
        messagebox.showwarning("No File Name", "Please provide a name for the output PDF.")
        return

    # Get all image files in the folder
    image_files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(('png', 'jpg', 'jpeg'))
    ]

    if not image_files:
        messagebox.showerror("No Images Found", "No image files found in the selected folder.")
        return

    # Sort images by metadata
    sorted_images = sort_images_by_metadata(image_files)

    # Define output PDF file path
    output_pdf = os.path.join(folder_path, f"{output_name}.pdf")

    # Reset progress bar
    progress_var.set(0)

    # Convert images to PDF
    success = images_to_pdf(sorted_images, output_pdf, progress_var)
    if success:
        messagebox.showinfo("Success", f"PDF successfully created at:\n{output_pdf}")
    else:
        messagebox.showerror("Error", "Failed to create PDF. Please try again.")

# Drag and Drop Event Handling
def drop_event(event):
    """Handle folder drag-and-drop."""
    folder_path = event.data.strip().replace("{", "").replace("}", "")
    folder_var.set(folder_path)

# Create the main UI
def main():
    global folder_var, file_name_var, progress_var

    root = TkinterDnD.Tk()
    root.title("Enhanced Image to PDF Converter")
    root.geometry("450x300")
    
    folder_var = StringVar()
    file_name_var = StringVar()
    progress_var = tk.IntVar()

    Label(root, text="Image to PDF Converter", font=("Arial", 16)).pack(pady=10)

    # Folder Selection
    Label(root, text="Folder:").pack(anchor="w", padx=10)
    Entry(root, textvariable=folder_var, width=50).pack(padx=10, pady=5, anchor="w")
    Button(root, text="Browse", command=select_folder).pack(padx=10, anchor="w")

    # File Name Input
    Label(root, text="Output PDF Name:").pack(anchor="w", padx=10)
    Entry(root, textvariable=file_name_var, width=50).pack(padx=10, pady=5, anchor="w")

    # Progress Bar
    Label(root, text="Progress:").pack(anchor="w", padx=10)
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate", variable=progress_var)
    progress_bar.pack(pady=5, padx=10)

    # Start Conversion Button
    Button(root, text="Convert to PDF", command=start_conversion, bg="lightblue", font=("Arial", 12)).pack(pady=20)

    # Drag-and-Drop Support
    root.drop_target_register("DND_Files")
    root.dnd_bind("<<Drop>>", drop_event)

    root.mainloop()

if __name__ == "__main__":
    main()
