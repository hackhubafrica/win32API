import ctypes
from ctypes import wintypes

# Define callback prototype
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)

# Load user32.dll
user32 = ctypes.windll.user32

# Define buffer size
buffer_size = 1024

# Define callback function
def enum_windows_proc(hwnd, lParam):
    buffer = ctypes.create_unicode_buffer(buffer_size)
    user32.GetWindowTextW(hwnd, buffer, buffer_size)
    window_title = buffer.value
    if window_title:
        print(f"Window Handle: {hwnd}, Title: {window_title}")
    return True

# Enumerate open windows
user32.EnumWindows(EnumWindowsProc(enum_windows_proc), 0)