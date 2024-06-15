import subprocess

def enable_defender_cloud_protection():
    command = "powershell -Command \"Set-MpPreference -CloudBlockLevel Enabled\""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Windows Defender Cloud Protection enabled successfully.")
    else:
        print(f"Failed to enable Windows Defender Cloud Protection: {result.stderr}")

enable_defender_cloud_protection()