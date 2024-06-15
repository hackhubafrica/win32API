import subprocess

def monitor_process_creation():
    command = 'powershell -Command "Get-WinEvent -FilterHashTable @{LogName=\'Security\'; ID=4688} | Format-Table -Property TimeCreated,ProviderName,Message -AutoSize"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Monitoring process creation events:")
        print(result.stdout)
    else:
        print(f"Failed to monitor process creation events: {result.stderr}")

monitor_process_creation()