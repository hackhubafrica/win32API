import ctypes
import ctypes.wintypes as wintypes

# Define WNDPROC type
WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM)

# Define window procedure
@WNDPROC
def window_proc(hwnd, msg, wparam, lparam):
    if msg == 0x0002:  # WM_DESTROY
        ctypes.windll.user32.PostQuitMessage(0)
    return ctypes.windll.user32.DefWindowProcW(hwnd, msg, wparam, lparam)

# Define WNDCLASS structure
class WNDCLASS(ctypes.Structure):
    _fields_ = [
        ("style", ctypes.c_uint),
        ("lpfnWndProc", WNDPROC),
        ("cbClsExtra", ctypes.c_int),
        ("cbWndExtra", ctypes.c_int),
        ("hInstance", wintypes.HINSTANCE),
        ("hIcon", wintypes.HICON),
        ("hCursor", wintypes.HCURSOR),
        ("hbrBackground", wintypes.HBRUSH),
        ("lpszMenuName", wintypes.LPCWSTR),
        ("lpszClassName", wintypes.LPCWSTR),
    ]

# Load user32.dll
user32 = ctypes.windll.user32

# Create and register window class
wndclass = WNDCLASS()
wndclass.lpfnWndProc = window_proc
wndclass.lpszClassName = "MessageOnlyWindow"
wndclass.hInstance = user32.GetModuleHandleW(None)
user32.RegisterClassW(ctypes.byref(wndclass))

# Create message-only window
hwnd = user32.CreateWindowExW(
    0,
    wndclass.lpszClassName,
    "Message Only Window",
    0,
    0, 0, 0, 0,
    user32.HWND_MESSAGE,
    None,
    wndclass.hInstance,
    None
)

# Run message loop
msg = wintypes.MSG()
while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
    user32.TranslateMessage(ctypes.byref(msg))
    user32.DispatchMessageW(ctypes.byref(msg))

# Unregister window class (optional)
user32.UnregisterClassW(wndclass.lpszClassName, wndclass.hInstance)