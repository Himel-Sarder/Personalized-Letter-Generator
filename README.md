# Personalized Letter Generator

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

## Contributing

Contributions to the Personalized Letter Generator are welcome! If you have any suggestions, bug fixes, or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

