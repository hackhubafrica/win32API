import ctypes

# System information structure
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

# Load kernel32.dll
kernel32 = ctypes.windll.kernel32
system_info = SYSTEM_INFO()

# Get system information
kernel32.GetSystemInfo(ctypes.byref(system_info))

# Print system information
print(f"Processor Architecture: {system_info.wProcessorArchitecture}")
print(f"Number of Processors: {system_info.dwNumberOfProcessors}")
print(f"Processor Type: {system_info.dwProcessorType}")

