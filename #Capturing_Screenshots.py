import ctypes
import ctypes.wintypes as wintypes
import numpy as np
from PIL import Image

# Load user32 and gdi32 DLLs
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# Get screen dimensions
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# Create a device context for the entire screen
hdesktop = user32.GetDC(0)

# Create a device context for the bitmap
hbitmap = gdi32.CreateCompatibleBitmap(hdesktop, screen_width, screen_height)
hdc = gdi32.CreateCompatibleDC(hdesktop)
gdi32.SelectObject(hdc, hbitmap)

# Copy the screen into the bitmap
gdi32.BitBlt(hdc, 0, 0, screen_width, screen_height, hdesktop, 0, 0, 0x00CC0020)

# Create a buffer to hold the bitmap data
bmp_info = ctypes.create_string_buffer(ctypes.sizeof(wintypes.BITMAPINFOHEADER) + screen_width * screen_height * 4)
bmp_header = wintypes.BITMAPINFOHEADER()
bmp_header.biSize = ctypes.sizeof(wintypes.BITMAPINFOHEADER)
bmp_header.biWidth = screen_width
bmp_header.biHeight = -screen_height  # Negative height to flip the image
bmp_header.biPlanes = 1
bmp_header.biBitCount = 32
bmp_header.biCompression = 0  # BI_RGB

# Get the bitmap data
gdi32.GetDIBits(hdc, hbitmap, 0, screen_height, bmp_info, bmp_header, 0)

# Convert the bitmap data to a NumPy array
image = np.frombuffer(bmp_info, dtype=np.uint8, offset=ctypes.sizeof(wintypes.BITMAPINFOHEADER)).reshape((screen_height, screen_width, 4))

# Save the image using PIL
img = Image.fromarray(image, 'RGBA')
img.save('screenshot.png')

# Clean up
gdi32.DeleteObject(hbitmap)
gdi32.DeleteDC(hdc)
user32.ReleaseDC(0, hdesktop)