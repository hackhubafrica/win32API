import winreg

# Specify the registry path and value name
registry_path = r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion"
#value_name = "anydesk"
value_name = "ProgramFilesDir"

# Open the registry key
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_path, 0, winreg.KEY_READ)

# Read the value
value, reg_type = winreg.QueryValueEx(key, value_name)

# Close the registry key
winreg.CloseKey(key)

# Print the value
print(f"{value_name}: {value}")