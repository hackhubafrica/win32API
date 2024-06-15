import subprocess

def add_defender_exclusion(path):
    command = f"powershell -Command \"Add-MpPreference -ExclusionPath '{path}'\""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Path '{path}' added to Windows Defender exclusions.")
    else:
        print(f"Failed to add exclusion: {result.stderr}")

# Example usage
add_defender_exclusion(r"C:\\Users\\Administrator\\Desktop\\WinAPI")