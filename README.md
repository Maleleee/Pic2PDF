# Welcome to Pic2PDF

**Pic2PDF** is a simple and user-friendly tool that converts images into a PDF file. Even if you have little technical knowledge, this guide will help you use the program with ease.

---

## Features
- Convert multiple images into a single PDF.
- Automatically sort images by their creation date to ensure the correct order.
- Drag-and-drop support for selecting image folders.
- Clean and intuitive interface.
- Progress bar to track the conversion process.

---

## Requirements
To run **Pic2PDF**, ensure you have the following:

1. **Windows or macOS**
2. **Python 3.10 or later**
3. Installed dependencies:
    - `tkinterdnd2`
    - `Pillow`

---

## Installation Guide

### Step 1: Install Python
1. Download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. During installation, check the box **"Add Python to PATH"**.

### Step 2: Install Required Libraries
1. Open the **Command Prompt** (Windows) or **Terminal** (macOS).
2. Type the following commands and press Enter after each:
   ```bash
   pip install tkinterdnd2
   pip install pillow
   ```

### Step 3: Download Pic2PDF
1. Clone or download this repository from GitHub.
2. Extract the contents if downloaded as a ZIP file.

---

## How to Use

### Step 1: Launch the Program
1. Open the folder where you saved the program files.
2. Double-click the file **`pic2pdf.py`** to start the tool.

### Step 2: Select Your Images
1. Drag and drop the folder containing your images into the program **or** click the **Browse** button to manually select a folder.
2. Enter a name for the output PDF file (e.g., `MyDocument.pdf`).

### Step 3: Start Conversion
1. Click the **Convert to PDF** button.
2. The progress bar will show the conversion status.
3. Once complete, a success message will appear, and your PDF will be saved in the same folder as the program.

---

## Troubleshooting

### Issue: "No module named 'tkinterdnd2'"
**Solution:** Ensure you installed `tkinterdnd2` by running:
```bash
pip install tkinterdnd2
```

### Issue: "FileNotFoundError"
**Solution:** Ensure the folder you selected contains valid image files (JPEG, PNG, etc.).

### Issue: "Program won't open."
**Solution:** Double-check you have Python installed and added to PATH. Reinstall if necessary.

---

## Frequently Asked Questions (FAQs)

**Q1: What image formats are supported?**
- Pic2PDF supports common formats like JPEG, PNG, and BMP.

**Q2: Where will my PDF be saved?**
- The PDF will be saved in the same folder as the program.

**Q3: Can I reorder the images?**
- Images are automatically sorted by creation date. To manually reorder, rename the files in your folder before starting the program.

---

## Support
If you have any issues or need help, feel free to contact us or open an issue on the GitHub repository.

---

Enjoy using **Pic2PDF**!

