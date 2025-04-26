



# Plagiarism Checker 🧠📝

A simple desktop application built with **Python Tkinter** to check plagiarism between two pieces of text.  
Users can either manually enter text or upload `.txt` files to compare similarity.

---

## ✨ Features

- ✅ Enter text manually into two separate text fields.
- ✅ Upload `.txt` files to automatically load text into the fields.
- ✅ Check the similarity percentage using a simple button click.
- ✅ User-friendly graphical interface (GUI).
- ✅ Displays a neat similarity percentage.

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Tkinter** (for GUI)
- **difflib.SequenceMatcher** (for comparing text)

---

## 🚀 How to Run the Project

1. Make sure you have **Python 3** installed on your system.

2. Install any necessary libraries (Tkinter usually comes pre-installed):
   ```bash
   pip install tk
   ```

3. Download or clone the repository:
   ```bash
   git clone https://github.com/renukanainala/plagrismchecker.git

   ```

4. Navigate into the project folder:
   ```bash
   cd plagrismchecker
   ```

5. Run the Python file:
   ```bash
   python app.py
   ```

---

## 📋 How to Use

1. **Manual Entry:**
   - Type or paste the first piece of text into the left text area.
   - Type or paste the second piece of text into the right text area.
   
2. **Using Files:**
   - Click **"Browse File 1"** to upload the first `.txt` file.
   - Click **"Browse File 2"** to upload the second `.txt` file.

3. **Check Plagiarism:**
   - Press **"Check Plagiarism"**.
   - The similarity percentage will be displayed below the button.

---


## 📢 Notes

- Only `.txt` files are supported for file upload.
- This is a basic plagiarism check based on text similarity, **not a deep AI-based detection**.
