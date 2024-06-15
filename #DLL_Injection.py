import ctypes

# Load kernel32.dll
kernel32 = ctypes.windll.kernel32

# Define constants
PROCESS_ALL_ACCESS = 0x001F0FFF

# Function prototypes
OpenProcess = kernel32.OpenProcess
VirtualAllocEx = kernel32.VirtualAllocEx
WriteProcessMemory = kernel32.WriteProcessMemory
CreateRemoteThread = kernel32.CreateRemoteThread

# Specify the DLL path and target process ID
dll_path = r"C:\\path\\to\\your.dll"
target_pid = 7984  # Replace with the target process ID

# Open the target process
hProcess = OpenProcess(PROCESS_ALL_ACCESS, False, target_pid)
if not hProcess:
    raise ctypes.WinError()

# Allocate memory for the DLL path
arg_address = VirtualAllocEx(hProcess, 0, len(dll_path), 0x3000, 0x40)
if not arg_address:
    kernel32.CloseHandle(hProcess)
    raise ctypes.WinError()

# Write the DLL path to the allocated memory
if not WriteProcessMemory(hProcess, arg_address, dll_path, len(dll_path), None):
    kernel32.CloseHandle(hProcess)
    raise ctypes.WinError()

# Get the address of LoadLibraryA
load_library = kernel32.GetProcAddress(kernel32.GetModuleHandleA(b"kernel32.dll"), b"LoadLibraryA")
if not load_library:
    kernel32.CloseHandle(hProcess)
    raise ctypes.WinError()

# Create a remote thread to load the DLL
if not CreateRemoteThread(hProcess, None, 0, load_library, arg_address, 0, None):
    kernel32.CloseHandle(hProcess)
    raise ctypes.WinError()

print("DLL injected successfully.")
kernel32.CloseHandle(hProcess)