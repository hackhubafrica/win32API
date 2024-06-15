import subprocess

def monitor_event_logs():
    command = 'powershell -Command "Get-WinEvent -FilterHashTable @{LogName=\'Security\'; Level=2,3,4} | Format-Table -Property TimeCreated,Message -AutoSize"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Monitoring Windows Event Logs for anomalies:")
        print(result.stdout)
    else:
        print(f"Failed to monitor Event Logs: {result.stderr}")

monitor_event_logs()