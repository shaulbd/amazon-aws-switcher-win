# AWS WorkSpaces Switcher

This Python script creates a small utility window using Tkinter that provides a button to show the Windows taskbar. The utility window automatically appears and disappears based on the presence of the Amazon WorkSpaces window.

## Features

- The utility window stays on top of other windows.
- The window contains a button to show the Windows taskbar.
- The window appears when the mouse cursor enters it and hides when the cursor leaves.
- The window only becomes fully visible when the Amazon WorkSpaces window is detected.

## Requirements

- Python 3.x
- `keyboard` library
- `pywin32` library

## Installation

1. **Clone the repository or download the script:**

    ```bash
    git clone https://github.com/shaulbd/amazon-aws-switcher-win.git
    cd amazon-aws-switcher-win
    ```

2. **Install the required Python libraries:**

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file should contain:

    ```txt
    keyboard
    pywin32
    ```

## Usage

1. **Run the script:**

    ```bash
    python aws-switcher.pyw
    ```
    
2. **Interacting with the Utility:**

    - Move your mouse cursor to the top of the screen (or the position you set) to make the utility window appear.
    - The window will become fully visible if the Amazon WorkSpaces window is detected.
    - Click the ❌ button to show the Windows taskbar.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
