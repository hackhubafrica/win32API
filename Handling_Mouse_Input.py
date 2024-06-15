import ctypes

# Load user32.dll
user32 = ctypes.windll.user32

# Define INPUT structure
class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        class _MOUSEINPUT(ctypes.Structure):
            _fields_ = [
                ("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_uint32),
                ("dwFlags", ctypes.c_uint32),
                ("time", ctypes.c_uint32),
                ("dwExtraInfo", ctypes.c_void_p),
            ]
        _fields_ = [("mi", _MOUSEINPUT)]
    _anonymous_ = ("_input",)
    _fields_ = [("type", ctypes.c_uint32), ("_input", _INPUT)]

# Constants
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

# Create INPUT structure for mouse move
mouse_move = INPUT()
mouse_move.type = 0  # INPUT_MOUSE
mouse_move.mi.dx = int(65536 * 500 / user32.GetSystemMetrics(0))  # Move to X:500
mouse_move.mi.dy = int(65536 * 500 / user32.GetSystemMetrics(1))  # Move to Y:500
mouse_move.mi.dwFlags = MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE

# Create INPUT structure for mouse click
mouse_click_down = INPUT()
mouse_click_down.type = 0  # INPUT_MOUSE
mouse_click_down.mi.dwFlags = MOUSEEVENTF_LEFTDOWN

mouse_click_up = INPUT()
mouse_click_up.type = 0  # INPUT_MOUSE
mouse_click_up.mi.dwFlags = MOUSEEVENTF_LEFTUP

# Send mouse move and click
user32.SendInput(1, ctypes.byref(mouse_move), ctypes.sizeof(INPUT))
user32.SendInput(1, ctypes.byref(mouse_click_down), ctypes.sizeof(INPUT))
user32.SendInput(1, ctypes.byref(mouse_click_up), ctypes.sizeof(INPUT))