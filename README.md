# File Handling in Python

This Python script demonstrates basic file handling operations including:

1. **Reading from a file (`sample.txt`)**
2. **Writing to a file (`output.txt`)**
3. **Appending to the same file (`output.txt`)**

---

## 🔹 Features

### 1. **Reading Lines from `sample.txt`**
- The script checks if `sample.txt` exists.
- If it exists, it reads the contents line by line.
- It prints:
  - Line 1
  - Line 2
  - Or shows an appropriate message if there are fewer lines or the file is empty.

### 2. **Writing to `output.txt`**
- Takes user input using `input()` and writes that content to `output.txt`.
- This **overwrites** the file if it already exists.

### 3. **Appending to `output.txt`**
- Takes another user input and **appends** it to the file without deleting the existing content.

---

## 🛠️ How to Run

1. Make sure Python is installed on your system.
2. Create a file named `sample.txt` in the same directory if you want the read part to succeed.
3. Run the script using:

```bash
python script_name.py

