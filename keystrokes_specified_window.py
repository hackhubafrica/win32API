import ctypes
import time

# Load user32.dll
user32 = ctypes.windll.user32

# Find the window handle
window_title = "Untitled - Notepad"
hwnd = user32.FindWindowW(None, window_title)
if not hwnd:
    raise Exception(f"Window '{window_title}' not found")

# Bring the window to the foreground
user32.SetForegroundWindow(hwnd)

# Wait for the window to become active
time.sleep(1)

# Define INPUT structure
class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        class _KEYBDINPUT(ctypes.Structure):
            _fields_ = [
                ("wVk", ctypes.c_uint16),
                ("wScan", ctypes.c_uint16),
                ("dwFlags", ctypes.c_uint32),
                ("time", ctypes.c_uint32),
                ("dwExtraInfo", ctypes.c_void_p),
            ]
        _fields_ = [
            ("ki", _KEYBDINPUT),
        ]
    _anonymous_ = ("_input",)
    _fields_ = [("type", ctypes.c_uint32), ("_input", _INPUT)]

# Define key constants
VK_A = 0x41

# Create INPUT structure for 'A' key press
input_a_down = INPUT()
input_a_down.type = 1  # INPUT_KEYBOARD
input_a_down.ki.wVk = VK_A
input_a_down.ki.dwFlags = 0  # Key down

# Create INPUT structure for 'A' key release
input_a_up = INPUT()
input_a_up.type = 1  # INPUT_KEYBOARD
input_a_up.ki.wVk = VK_A
input_a_up.ki.dwFlags = 2  # Key up

# Send 'A' key press and release
user32.SendInput(1, ctypes.byref(input_a_down), ctypes.sizeof(INPUT))
user32.SendInput(1, ctypes.byref(input_a_up), ctypes.sizeof(INPUT))