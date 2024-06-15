import ctypes
from ctypes import wintypes

# Load kernel32.dll
kernel32 = ctypes.windll.kernel32

# Define constants
PROCESS_ALL_ACCESS = 0x001F0FFF

# Function prototypes
OpenProcess = kernel32.OpenProcess
ReadProcessMemory = kernel32.ReadProcessMemory
CloseHandle = kernel32.CloseHandle

# Specify the process ID (PID) of the target process
pid = 7984  # Replace with the target PID

# Open the target process
hProcess = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
if not hProcess:
    raise ctypes.WinError()

# Specify the address to read from (example address)
address = 0x7FFDF000  # Replace with the target address
buffer = ctypes.create_string_buffer(1024)
bytes_read = wintypes.SIZE()

# Read process memory
if not ReadProcessMemory(hProcess, address, buffer, len(buffer), ctypes.byref(bytes_read)):
    CloseHandle(hProcess)
    raise ctypes.WinError()

# Print the read data
print(f"Data: {buffer.raw[:bytes_read.value]}")

# Close the process handle
CloseHandle(hProcess)