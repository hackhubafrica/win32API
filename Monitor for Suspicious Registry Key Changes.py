import subprocess

def monitor_registry_changes():
    command = 'powershell -Command "Get-WinEvent -FilterHashTable @{LogName=\'Security\'; ID=4657} | Format-Table -Property TimeCreated,Message -AutoSize"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Monitoring for suspicious registry key changes:")
        print(result.stdout)
    else:
        print(f"Failed to monitor registry key changes: {result.stderr}")

monitor_registry_changes()