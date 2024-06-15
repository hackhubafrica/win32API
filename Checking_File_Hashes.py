import ctypes
import hashlib

# Load kernel32.dll
kernel32 = ctypes.windll.kernel32

# Function prototypes
CreateFile = kernel32.CreateFileW
ReadFile = kernel32.ReadFile
CloseHandle = kernel32.CloseHandle

# Define constants
GENERIC_READ = 0x80000000
OPEN_EXISTING = 3

# Specify the file path
file_path = "C:\\Users\\Administrator\\Desktop\\WinAPI\\file.txt"  # Replace with the target file path

# Open the file
hFile = CreateFile(file_path, GENERIC_READ, 0, None, OPEN_EXISTING, 0, None)
if hFile == -1:
    raise ctypes.WinError()

# Read the file and compute the hash
hasher = hashlib.sha256()
buffer_size = 4096
buffer = ctypes.create_string_buffer(buffer_size)
bytes_read = ctypes.c_uint32()

while True:
    if not ReadFile(hFile, buffer, buffer_size, ctypes.byref(bytes_read), None):
        CloseHandle(hFile)
        raise ctypes.WinError()
    if bytes_read.value == 0:
        break
    hasher.update(buffer.raw[:bytes_read.value])

# Close the file handle
CloseHandle(hFile)

# Print the hash
print(f"SHA-256: {hasher.hexdigest()}")