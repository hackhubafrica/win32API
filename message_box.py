import ctypes

# Constants
MB_OK = 0x0
MB_ICONINFORMATION = 0x40

# Function prototype
MessageBox = ctypes.windll.user32.MessageBoxW

# Display message box
MessageBox(None, 'Hello, World!', 'Message', MB_OK | MB_ICONINFORMATION)
