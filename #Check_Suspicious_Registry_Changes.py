import subprocess

def check_registry_changes():
    command = 'powershell -Command "Get-WinEvent -FilterHashTable @{LogName=\'Security\'; ID=4657} | Format-Table -Property TimeCreated,Message -AutoSize"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Checking for suspicious registry changes:")
        print(result.stdout)
    else:
        print(f"Failed to check registry changes: {result.stderr}")

check_registry_changes()