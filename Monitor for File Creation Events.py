import subprocess

def monitor_file_creation():
    command = 'powershell -Command "Get-WinEvent -FilterHashTable @{LogName=\'Security\'; ID=4663} | Format-Table -Property TimeCreated,Message -AutoSize"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Monitoring for file creation events:")
        print(result.stdout)
    else:
        print(f"Failed to monitor file creation events: {result.stderr}")

monitor_file_creation()