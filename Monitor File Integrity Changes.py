import subprocess

def monitor_file_changes():
    command = 'powershell -Command "Get-WinEvent -FilterHashTable @{LogName=\'Security\'; ID=4656} | Format-Table -Property TimeCreated,Message -AutoSize"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Monitoring file integrity changes:")
        print(result.stdout)
    else:
        print(f"Failed to monitor file changes: {result.stderr}")

monitor_file_changes()