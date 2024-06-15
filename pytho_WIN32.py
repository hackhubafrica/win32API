import ctypes

# Load necessary DLLs
user32 = ctypes.WinDLL('user32')
kernel32 = ctypes.WinDLL('kernel32')

# Define constants
MB_OK = 0x00000000
MB_ICONINFORMATION = 0x00000040

# Define types used in Win32 API
HWND = ctypes.c_void_p
LPCWSTR = ctypes.c_wchar_p
UINT = ctypes.c_uint
DWORD = ctypes.c_ulong

# Define function prototypes
MessageBox = user32.MessageBoxW
MessageBox.argtypes = [HWND, LPCWSTR, LPCWSTR, UINT]
MessageBox.restype = ctypes.c_int

# Main function to display message box
def show_message_box():
    message = "Hello from Python and Win32 API!"
    caption = "Message Box"
    MessageBox(None, message, caption, MB_OK | MB_ICONINFORMATION)

# Entry point
if __name__ == "__main__":
    show_message_box()
