import winreg

def add_to_startup(file_path, name="MyApp"):
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, file_path)
    winreg.CloseKey(registry_key)

# Example usage
add_to_startup(r"C:\\path\\to\\your\\program.exe", "MyApp")