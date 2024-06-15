import ctypes
import platform
from datetime import datetime

# Define SYSTEM_INFO structure
class SYSTEM_INFO(ctypes.Structure):
    _fields_ = [
        ("wProcessorArchitecture", ctypes.c_uint16),
        ("wReserved", ctypes.c_uint16),
        ("dwPageSize", ctypes.c_uint32),
        ("lpMinimumApplicationAddress", ctypes.c_void_p),
        ("lpMaximumApplicationAddress", ctypes.c_void_p),
        ("dwActiveProcessorMask", ctypes.c_void_p),
        ("dwNumberOfProcessors", ctypes.c_uint32),
        ("dwProcessorType", ctypes.c_uint32),
        ("dwAllocationGranularity", ctypes.c_uint32),
        ("wProcessorLevel", ctypes.c_uint16),
        ("wProcessorRevision", ctypes.c_uint16),
    ]

# Define MEMORYSTATUSEX structure
class MEMORYSTATUSEX(ctypes.Structure):
    _fields_ = [
        ("dwLength", ctypes.c_uint32),
        ("dwMemoryLoad", ctypes.c_uint32),
        ("ullTotalPhys", ctypes.c_uint64),
        ("ullAvailPhys", ctypes.c_uint64),
        ("ullTotalPageFile", ctypes.c_uint64),
        ("ullAvailPageFile", ctypes.c_uint64),
        ("ullTotalVirtual", ctypes.c_uint64),
        ("ullAvailVirtual", ctypes.c_uint64),
        ("sullAvailExtendedVirtual", ctypes.c_uint64),
    ]

# Load kernel32.dll
kernel32 = ctypes.windll.kernel32
system_info = SYSTEM_INFO()

# Get system information
kernel32.GetSystemInfo(ctypes.byref(system_info))

# Get memory status
memory_status = MEMORYSTATUSEX()
memory_status.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
kernel32.GlobalMemoryStatusEx(ctypes.byref(memory_status))

# Get system time
system_time = ctypes.c_uint64()
kernel32.GetSystemTimeAsFileTime(ctypes.byref(system_time))

# Convert system time to datetime
system_time = system_time.value
dt = datetime.utcfromtimestamp((system_time - 116444736000000000) / 10000000)

# Print system information
print(f"Processor Architecture: {system_info.wProcessorArchitecture}")
print(f"Number of Processors: {system_info.dwNumberOfProcessors}")
print(f"Processor Type: {system_info.dwProcessorType}")
print(f"Processor Level: {system_info.wProcessorLevel}")
print(f"Processor Revision: {system_info.wProcessorRevision}")

# Print memory status
print(f"Total Physical Memory: {memory_status.ullTotalPhys / (1024 ** 3):.2f} GB")
print(f"Available Physical Memory: {memory_status.ullAvailPhys / (1024 ** 3):.2f} GB")
print(f"Total Virtual Memory: {memory_status.ullTotalVirtual / (1024 ** 3):.2f} GB")
print(f"Available Virtual Memory: {memory_status.ullAvailVirtual / (1024 ** 3):.2f} GB")
print(f"Memory Load: {memory_status.dwMemoryLoad}%")

# Print system time
print(f"System Time: {dt.strftime('%Y-%m-%d %H:%M:%S')}")