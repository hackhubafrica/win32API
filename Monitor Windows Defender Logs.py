import subprocess

def monitor_defender_logs():
    command = 'powershell -Command "Get-WinEvent -FilterHashtable @{LogName=\'Microsoft-Windows-Windows Defender/Operational\'; ID=1116} | Format-Table -Property TimeCreated,Message -AutoSize"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Monitoring Windows Defender logs for detections:")
        print(result.stdout)
    else:
        print(f"Failed to monitor Windows Defender logs: {result.stderr}")

monitor_defender_logs()