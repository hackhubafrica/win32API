import ctypes
import ctypes.wintypes as wintypes

# Define callback function prototype
WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100

# Load user32.dll
user32 = ctypes.windll.user32

# Define a low-level keyboard hook procedure
@ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_int, ctypes.wintypes.WPARAM, ctypes.wintypes.LPARAM)
def low_level_keyboard_proc(nCode, wParam, lParam):
    if nCode == 0 and wParam == WM_KEYDOWN:
        kbd = ctypes.cast(lParam, ctypes.POINTER(wintypes.KBDLLHOOKSTRUCT)).contents
        print(f"Key: {kbd.vkCode}")
    return user32.CallNextHookEx(None, nCode, wParam, lParam)

# Set the hook
keyboard_hook = user32.SetWindowsHookExW(WH_KEYBOARD_LL, low_level_keyboard_proc, None, 0)
if not keyboard_hook:
    raise ctypes.WinError()

# Message loop to keep the script running
msg = wintypes.MSG()
while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
    user32.TranslateMessage(ctypes.byref(msg))
    user32.DispatchMessageW(ctypes.byref(msg))

# Unhook the procedure (unreachable in this infinite loop example)
user32.UnhookWindowsHookEx(keyboard_hook)