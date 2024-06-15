import ctypes

# Define constants
SERVICE_QUERY_STATUS = 0x0004
SERVICE_WIN32 = 0x00000030
SC_MANAGER_ALL_ACCESS = 0xF003F
SERVICE_ACTIVE = 0x00000001

# Define SERVICE_STATUS structure
class SERVICE_STATUS(ctypes.Structure):
    _fields_ = [
        ("dwServiceType", ctypes.c_uint32),
        ("dwCurrentState", ctypes.c_uint32),
        ("dwControlsAccepted", ctypes.c_uint32),
        ("dwWin32ExitCode", ctypes.c_uint32),
        ("dwServiceSpecificExitCode", ctypes.c_uint32),
        ("dwCheckPoint", ctypes.c_uint32),
        ("dwWaitHint", ctypes.c_uint32),
    ]

# Load advapi32.dll
advapi32 = ctypes.windll.advapi32

# Open service control manager
hSCManager = advapi32.OpenSCManagerW(None, None, SC_MANAGER_ALL_ACCESS)
if not hSCManager:
    raise ctypes.WinError()

# Open the specified service
service_name = "wuauserv"  # Windows Update service
hService = advapi32.OpenServiceW(hSCManager, service_name, SERVICE_QUERY_STATUS)
if not hService:
    advapi32.CloseServiceHandle(hSCManager)
    raise ctypes.WinError()

# Query service status
service_status = SERVICE_STATUS()
if not advapi32.QueryServiceStatus(hService, ctypes.byref(service_status)):
    advapi32.CloseServiceHandle(hService)
    advapi32.CloseServiceHandle(hSCManager)
    raise ctypes.WinError()

# Print service status
print(f"Service: {service_name}")
print(f"Current State: {service_status.dwCurrentState}")

# Close service handles
advapi32.CloseServiceHandle(hService)
advapi32.CloseServiceHandle(hSCManager)