import ctypes

# Constants
GENERIC_WRITE = 0x40000000
CREATE_ALWAYS = 2
FILE_ATTRIBUTE_NORMAL = 0x80

# Function prototypes
CreateFile = ctypes.windll.kernel32.CreateFileW
WriteFile = ctypes.windll.kernel32.WriteFile
CloseHandle = ctypes.windll.kernel32.CloseHandle

# Create file
handle = CreateFile(
    'C:\\Users\\Administrator\\Desktop\\WinAPI\\file.txt', GENERIC_WRITE, 0, None, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, None
)

# Data to write
data = b'Hello, World!'
written = ctypes.c_uint32()

# Write data to file
WriteFile(handle, data, len(data), ctypes.byref(written), None)

# Close file handle
CloseHandle(handle)