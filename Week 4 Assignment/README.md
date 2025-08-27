# File Handling and Exception Handling Assignment

## 📌 Overview
This project demonstrates **basic file handling** and **error handling** in Python.  
The program reads the contents of an input file, modifies them, and writes the result to a new output file. It also includes error handling for missing or unreadable files.

---

## 🗂️ Files in the Repository
- `read_write.py` → Main Python script that performs file read/write operations and handles errors.
- `README.md` → Documentation for the project.
- `input.txt` → (You create this) Example input file for testing.
- `output.txt` → Generated output file after running the script.

---

## ⚙️ How It Works
1. The script asks the user for the **filename to read**.
2. If the file exists:
   - Reads its contents.
   - Transforms the text (e.g., converts to uppercase).
   - Writes the modified content into `output.txt`.
3. If the file does not exist:
   - Prints an error message:  
     ```
     ❌ Error: The file 'filename.txt' does not exist.
     ```

---

## ▶️ How to Run
Make sure you are in the project folder, then run:

```bash
python read_write.py
```
