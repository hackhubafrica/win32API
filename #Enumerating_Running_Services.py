import ctypes
import ctypes.wintypes as wintypes

# Load advapi32.dll
advapi32 = ctypes.windll.advapi32

# Define constants
SC_MANAGER_ENUMERATE_SERVICE = 0x0004
SERVICE_WIN32 = 0x00000030
SERVICE_STATE_ALL = 0x00000003

# Define structures
class ENUM_SERVICE_STATUS_PROCESS(ctypes.Structure):
    _fields_ = [
        ("lpServiceName", wintypes.LPWSTR),
        ("lpDisplayName", wintypes.LPWSTR),
        ("ServiceStatusProcess", wintypes.SERVICE_STATUS_PROCESS)
    ]

# Function prototypes
OpenSCManager = advapi32.OpenSCManagerW
EnumServicesStatusEx = advapi32.EnumServicesStatusExW

# Open the service control manager
sc_manager = OpenSCManager(None, None, SC_MANAGER_ENUMERATE_SERVICE)
if not sc_manager:
    raise ctypes.WinError()

# Allocate buffer
buffer_size = 8192
buffer = ctypes.create_string_buffer(buffer_size)
bytes_needed = wintypes.DWORD()
services_returned = wintypes.DWORD()
resume_handle = wintypes.DWORD()

# Enumerate services
if not EnumServicesStatusEx(
    sc_manager,
    0,
    SERVICE_WIN32,
    SERVICE_STATE_ALL,
    ctypes.byref(buffer),
    buffer_size,
    ctypes.byref(bytes_needed),
    ctypes.byref(services_returned),
    ctypes.byref(resume_handle),
    None
):
    advapi32.CloseServiceHandle(sc_manager)
    raise ctypes.WinError()

# Parse services
services = ctypes.cast(buffer, ctypes.POINTER(ENUM_SERVICE_STATUS_PROCESS * services_returned.value)).contents
for service in services:
    print(f"Service Name: {service.lpServiceName}")
    print(f"Display Name: {service.lpDisplayName}")

# Close the service control manager handle
advapi32.CloseServiceHandle(sc_manager)