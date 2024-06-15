import ctypes
import psutil

# Define PROCESSENTRY32 structure
class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.c_uint32),
        ("cntUsage", ctypes.c_uint32),
        ("th32ProcessID", ctypes.c_uint32),
        ("th32DefaultHeapID", ctypes.c_uintptr),
        ("th32ModuleID", ctypes.c_uint32),
        ("cntThreads", ctypes.c_uint32),
        ("th32ParentProcessID", ctypes.c_uint32),
        ("pcPriClassBase", ctypes.c_int32),
        ("dwFlags", ctypes.c_uint32),
        ("szExeFile", ctypes.c_char * 260),
    ]

# Load kernel32.dll
kernel32 = ctypes.windll.kernel32
CreateToolhelp32Snapshot = kernel32.CreateToolhelp32Snapshot
Process32First = kernel32.Process32First
Process32Next = kernel32.Process32Next
CloseHandle = kernel32.CloseHandle

# Constants
TH32CS_SNAPPROCESS = 0x00000002
INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value

# Create snapshot of all processes
hProcessSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
if hProcessSnap == INVALID_HANDLE_VALUE:
    raise Exception("Failed to create snapshot")

# Initialize PROCESSENTRY32
pe32 = PROCESSENTRY32()
pe32.dwSize = ctypes.sizeof(PROCESSENTRY32)

# Get the first process
if not Process32First(hProcessSnap, ctypes.byref(pe32)):
    CloseHandle(hProcessSnap)
    raise Exception("Failed to retrieve first process")

# List all processes
processes = []
while True:
    processes.append({
        'Process ID': pe32.th32ProcessID,
        'Executable': pe32.szExeFile.decode('utf-8'),
        'Thread Count': pe32.cntThreads,
        'Parent Process ID': pe32.th32ParentProcessID,
    })
    if not Process32Next(hProcessSnap, ctypes.byref(pe32)):
        break

# Close snapshot handle
CloseHandle(hProcessSnap)

# Print process details
for process in processes:
    print(f"Process ID: {process['Process ID']}")
    print(f"Executable: {process['Executable']}")
    print(f"Thread Count: {process['Thread Count']}")
    print(f"Parent Process ID: {process['Parent Process ID']}")
    print('-' * 20)