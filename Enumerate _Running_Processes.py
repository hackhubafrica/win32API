import ctypes
import ctypes.wintypes as wintypes

# Load psapi.dll
psapi = ctypes.windll.psapi

# Define constants
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010
MAX_PATH = 260

# Function prototypes
EnumProcesses = psapi.EnumProcesses
GetModuleBaseName = psapi.GetModuleBaseNameW

# Define buffer size
buffer_size = 9000

# Enumerate processes
process_ids = (ctypes.c_uint * buffer_size)()
bytes_returned = ctypes.c_uint()

if not EnumProcesses(ctypes.byref(process_ids), ctypes.sizeof(process_ids), ctypes.byref(bytes_returned)):
    raise ctypes.WinError()

process_count = bytes_returned.value // ctypes.sizeof(ctypes.c_uint)

# Iterate over processes
for i in range(process_count):
    process_id = process_ids[i]
    hProcess = ctypes.windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, process_id)
    if hProcess:
        module_name = ctypes.create_unicode_buffer(MAX_PATH)
        if GetModuleBaseName(hProcess, None, module_name, MAX_PATH):
            print(f"Process ID: {process_id}, Name: {module_name.value}")
        ctypes.windll.kernel32.CloseHandle(hProcess)