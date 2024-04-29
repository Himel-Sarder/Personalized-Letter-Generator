# Personalized Letter Generator
![image](https://github.com/Himel-Sarder/Personalized-Letter-Generator/assets/143216886/9d6e22e1-0b22-4449-a8d6-634c8f869a93)

## Overview

The Personalized Letter Generator is a Python script that automates the process of generating personalized letters for multiple recipients. It reads a list of names from a file, replaces a placeholder in a letter template with each name, and creates individualized letters for each recipient.

## How It Works

1. **Input Files**: 
   - `Names_container.txt`: Contains a list of names, with each name on a separate line.
   - `Letter_container.txt`: Contains the letter template with a placeholder `[NAME]` where the recipient's name will be inserted.

2. **Processing**:
   - The script reads the list of names from `Names_container.txt`.
   - It reads the letter template from `Letter_container.txt`.
   - For each name in the list, it replaces the placeholder `[NAME]` in the letter template with the actual name.
   - It creates a new text file for each recipient with the personalized letter.

3. **Output**:
   - Individualized letters are saved in the `Output` directory with filenames formatted as `letter_for_[NAME].txt`.

## Usage

1. **Prepare Input Files**:
   - Ensure that `Names_container.txt` contains the list of names and `Letter_container.txt` contains the letter template with `[NAME]` as a placeholder.

2. **Run the Script**:
   - Execute the Python script `main.py`.

3. **Generated Letters**:
   - Personalized letters for each recipient will be created and saved in the `Output` directory.

## Dependencies

- Python 3.x

# Python File Handling( readlines(), strip(), replace() )     

### 1. `readlines()`
The `readlines()` method reads all lines from the file and returns them as a list of strings.

```python
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

### 2. `strip()`
The `strip()` method removes leading and trailing whitespace (including newline characters) from a string.

```python
line = "   Hi ! I am Himel   \n"
stripped_line = line.strip()
print(stripped_line)  # Output: "Hi ! I am Himel"
```

### 3. `replace()`
The `replace()` method replaces occurrences of a specified substring with another string.

```python
text = "Hello, [NAME]! How are you, [NAME]?"
new_text = text.replace("[NAME]", "Himel")
print(new_text)  # Output: "Hello, Himel! How are you, Himel?"
```

### Example: Reading a File, Stripping, and Replacing
```python
# Read lines from a file, strip whitespace, and replace placeholders
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        stripped_line = line.strip()  # Strip leading/trailing whitespace
        replaced_line = stripped_line.replace("[NAME]", "Himel")  # Replace placeholders
        print(replaced_line)
```

This example reads lines from a file, strips whitespace, and replaces placeholders (`[NAME]`) with a specific name ("Himel"). 

## Contributing

Contributions to the Personalized Letter Generator are welcome! If you have any suggestions, bug fixes, or improvements, feel free to open an issue or submit a pull request.
## Coder   
Coded by -
- Himel Sarder
- Dept. of CSE, BSFMSTU, Bangladesh
- gmail : info.himelcse@gmail.com   
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# Thank You
