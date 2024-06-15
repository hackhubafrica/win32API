import ctypes

# Define constants
SERVICE_WIN32_OWN_PROCESS = 0x00000010
SERVICE_AUTO_START = 0x00000002
SERVICE_ERROR_NORMAL = 0x00000001

# Load advapi32.dll
advapi32 = ctypes.windll.advapi32

# Function prototypes
CreateService = advapi32.CreateServiceW

# Define service parameters
service_name = "MyService"
display_name = "My Service"
binary_path = r"C:\\path\\to\\your\\program.exe"

# Open service control manager
sc_handle = advapi32.OpenSCManagerW(None, None, 0x0002)
if not sc_handle:
    raise ctypes.WinError()

# Create the service
service_handle = CreateService(
    sc_handle,
    service_name,
    display_name,
    0xF01FF,
    SERVICE_WIN32_OWN_PROCESS,
    SERVICE_AUTO_START,
    SERVICE_ERROR_NORMAL,
    binary_path,
    None,
    None,
    None,
    None,
    None
)

if not service_handle:
    advapi32.CloseServiceHandle(sc_handle)
    raise ctypes.WinError()

print(f"Service '{service_name}' created successfully.")

# Close handles
advapi32.CloseServiceHandle(service_handle)
advapi32.CloseServiceHandle(sc_handle)