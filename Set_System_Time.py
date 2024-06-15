import ctypes
from datetime import datetime

# Define SYSTEMTIME structure
class SYSTEMTIME(ctypes.Structure):
    _fields_ = [
        ("wYear", ctypes.c_uint16),
        ("wMonth", ctypes.c_uint16),
        ("wDayOfWeek", ctypes.c_uint16),
        ("wDay", ctypes.c_uint16),
        ("wHour", ctypes.c_uint16),
        ("wMinute", ctypes.c_uint16),
        ("wSecond", ctypes.c_uint16),
        ("wMilliseconds", ctypes.c_uint16),
    ]

# Load kernel32.dll
kernel32 = ctypes.windll.kernel32

# Function prototype
SetSystemTime = kernel32.SetSystemTime

# Specify the new system time
new_time = SYSTEMTIME()
dt = datetime(2024, 6, 12, 18, 2, 0)
new_time.wYear = dt.year
new_time.wMonth = dt.month
new_time.wDay = dt.day
new_time.wHour = dt.hour
new_time.wMinute = dt.minute
new_time.wSecond = dt.second
new_time.wMilliseconds = dt.microsecond // 1000

# Set system time
if not SetSystemTime(ctypes.byref(new_time)):
    raise ctypes.WinError()

print("System time updated successfully.")