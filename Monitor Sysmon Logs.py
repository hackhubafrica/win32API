import subprocess

def monitor_sysmon_logs():
    command = 'powershell -Command "Get-WinEvent -FilterHashtable @{LogName=\'Microsoft-Windows-Sysmon/Operational\'} | Format-Table -Property TimeCreated,EventID,Message -AutoSize"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Monitoring Sysmon logs for suspicious activity:")
        print(result.stdout)
    else:
        print(f"Failed to monitor Sysmon logs: {result.stderr}")

monitor_sysmon_logs()