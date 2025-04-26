import tkinter as tk
from tkinter import messagebox, filedialog

def check_plagiarism():
    text1 = text1_entry.get("1.0", tk.END).strip()
    text2 = text2_entry.get("1.0", tk.END).strip()

    if not text1 or not text2:
        messagebox.showwarning("Input Error", "Please enter text in both fields.")
        return

    from difflib import SequenceMatcher
    similarity = SequenceMatcher(None, text1, text2).ratio() * 100

    result_label.config(text=f"Plagiarism Detected: {similarity:.2f}%")

def browse_file1():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            text1_entry.delete("1.0", tk.END)
            text1_entry.insert(tk.END, content)

def browse_file2():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            text2_entry.delete("1.0", tk.END)
            text2_entry.insert(tk.END, content)

# Main Window
root = tk.Tk()
root.title("Plagiarism Checker")
root.state('zoomed')
root.configure(bg="white")

# Heading
title_label = tk.Label(root, text="Plagiarism Checker", font=("Arial", 30, "bold"), bg="white")
title_label.pack(pady=20)

# Frame to hold both text fields
frame = tk.Frame(root, bg="white")
frame.pack(pady=20)

# Text 1
text1_frame = tk.Frame(frame, bg="white")
text1_frame.grid(row=0, column=0, padx=30)

text1_label = tk.Label(text1_frame, text="Enter Text 1", font=("Arial", 18, "bold"), bg="white")
text1_label.pack(pady=10)

text1_entry = tk.Text(text1_frame, width=50, height=15, font=("Arial", 14), bd=2, relief="solid")
text1_entry.pack()

browse_button1 = tk.Button(text1_frame, text="Browse File 1", font=("Arial", 12), bg="#2196F3", fg="white", command=browse_file1)
browse_button1.pack(pady=10)

# Text 2
text2_frame = tk.Frame(frame, bg="white")
text2_frame.grid(row=0, column=1, padx=30)

text2_label = tk.Label(text2_frame, text="Enter Text 2", font=("Arial", 18, "bold"), bg="white")
text2_label.pack(pady=10)

text2_entry = tk.Text(text2_frame, width=50, height=15, font=("Arial", 14), bd=2, relief="solid")
text2_entry.pack()

browse_button2 = tk.Button(text2_frame, text="Browse File 2", font=("Arial", 12), bg="#2196F3", fg="white", command=browse_file2)
browse_button2.pack(pady=10)

# Check Plagiarism Button
check_button = tk.Button(root, text="Check Plagiarism", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white", command=check_plagiarism)
check_button.pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="white", fg="green")
result_label.pack(pady=10)

root.mainloop()
