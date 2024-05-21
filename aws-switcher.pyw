# Import necessary modules
from tkinter import *
from tkinter import ttk
import keyboard
import win32ui

# Global variable to store the identifier returned by after method
hide_id = None

# Function to handle the taskbar visibility
def handleClick():
    """Shows the taskbar."""
    keyboard.press_and_release('windows')
    print("Showing task bar.")

# Function to set the position of the window frame
def setFramePosition(window, position, frame_width, frame_height):
    """Set button position based on desired location."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Determine coordinates based on position argument
    if position == "top":
        x_coord = (screen_width - frame_width) // 2
        y_coord = 0
    elif position == "bottom":
        x_coord = (screen_width - frame_width) // 2
        y_coord = screen_height - frame_height
    elif position in ("topleft", "topright"):
        y_coord = 0
        if position == "topleft":
            x_coord = 0
        else:
            x_coord = screen_width - frame_width
    elif position in ("bottomleft", "bottomright"):
        if position == "bottomleft":
            x_coord = 0
        else:
            x_coord = screen_width - frame_width
        y_coord = screen_height - frame_height
    else:
        raise ValueError("Invalid position")

    # Set window geometry
    window.geometry(f"{frame_width}x{frame_height}+{x_coord}+{y_coord}")

# Function to delay execution of a function
def delay(lmbd, delay):  
    global hide_id             
    if hide_id is not None:
         win.after_cancel(hide_id)      
    hide_id = win.after(delay, lambda: lmbd())

# Function to check if a window with given class name and name exists
def WindowExists(classname,name):
    try:
        win32ui.FindWindow(classname, name)
    except win32ui.error:
        return False
    else:
        return True
    
# Function to show the button frame
def showButton(event):
    delay(showButtonInternal, 500)

# Internal function to show the button frame based on Amazon WorkSpaces window existence
def showButtonInternal():
    if WindowExists(None, "Amazon WorkSpaces"):
        button_frame.pack(fill="both", expand=True)
        label.pack(side="left", expand=False, padx = 5)
        button.pack(side="right", expand=False)
        win.attributes('-alpha', 1.0)
    print("Showing button.")

# Function to hide the button frame
def hideButton(event):
    delay(hideButtonInternal, 1000)

# Internal function to hide the button frame
def hideButtonInternal():
    button_frame.pack_forget()
    win.attributes('-alpha', 0.01)
    print("Hiding button.")

# Create main window instance
win = Tk()

# Configure window attributes
win.overrideredirect(1)
win.attributes('-alpha', 0.01)
win.wm_attributes("-transparentcolor", 'grey')

# Set frame dimensions and position
setFramePosition(win, "top", 350, 22)

# Configure styles for frame, label, and button
frameStyle = ttk.Style()
frameStyle.configure("Custom.TFrame",  background="blue", relief="raised", highlightthickness = 0, borderwidth=0, bd = 0,)
textStyle = ttk.Style()
textStyle.configure("Custom.TLabel", font=('Arial', 8), foreground="white", background="blue",  highlightthickness = 0, borderwidth=0, bd = 0,relief="flat")
buttonStyle = ttk.Style()
buttonStyle.configure("Custom.TButton", font=('Arial', 8), foreground="blue", highlightthickness = 0, borderwidth=0,  bd = 0,relief="flat")

# Create button frame, label, and button
button_frame = ttk.Frame(win, style="Custom.TFrame")
label = ttk.Label(button_frame, text="AWS Workspace Switcher", style="Custom.TLabel")
button = ttk.Button(button_frame, text="❌", style="Custom.TButton", command=handleClick)

# Bind events to show and hide the button frame
win.bind("<Enter>", showButton)
win.bind("<Leave>", hideButton)

# Function to keep the window on top
def setOnTop():
    """Keep the window on top."""
    win.attributes('-topmost', True)
    win.after(1000, setOnTop)

# Start the function to keep window on top
win.after(1000, setOnTop)

# Start the Tkinter event loop
win.mainloop()
