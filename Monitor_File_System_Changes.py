import ctypes
import os

# Define constants
FILE_LIST_DIRECTORY = 0x0001
FILE_NOTIFY_CHANGE_FILE_NAME = 0x00000001
FILE_NOTIFY_CHANGE_DIR_NAME = 0x00000002
FILE_NOTIFY_CHANGE_ATTRIBUTES = 0x00000004
FILE_NOTIFY_CHANGE_SIZE = 0x00000008
FILE_NOTIFY_CHANGE_LAST_WRITE = 0x00000010

# Load kernel32.dll
kernel32 = ctypes.windll.kernel32

# Function prototypes
ReadDirectoryChangesW = kernel32.ReadDirectoryChangesW

# Define FILE_NOTIFY_INFORMATION structure
class FILE_NOTIFY_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("NextEntryOffset", ctypes.c_uint32),
        ("Action", ctypes.c_uint32),
        ("FileNameLength", ctypes.c_uint32),
        ("FileName", ctypes.c_wchar * 1),
    ]

# Specify the directory to monitor
directory = r"C:\\Users\\Administrator\\Desktop"

# Open directory handle
directory_handle = kernel32.CreateFileW(
    directory,
    FILE_LIST_DIRECTORY,
    0x00000007,
    None,
    3,
    0x02000000,
    None,
)

# Buffer to store change information
buffer = ctypes.create_string_buffer(1024)

# Monitor directory changes
while True:
    bytes_returned = ctypes.c_uint32()
    result = ReadDirectoryChangesW(
        directory_handle,
        ctypes.byref(buffer),
        len(buffer),
        True,
        FILE_NOTIFY_CHANGE_FILE_NAME | FILE_NOTIFY_CHANGE_DIR_NAME | FILE_NOTIFY_CHANGE_ATTRIBUTES | FILE_NOTIFY_CHANGE_SIZE | FILE_NOTIFY_CHANGE_LAST_WRITE,
        ctypes.byref(bytes_returned),
        None,
        None,
    )
    if result:
        notify_info = FILE_NOTIFY_INFORMATION.from_buffer(buffer)
        print(f"Change detected: Action={notify_info.Action}, FileName={notify_info.FileName[:notify_info.FileNameLength // 2]}")

# Close directory handle (unreachable in this infinite loop example)
kernel32.CloseHandle(directory_handle)