import subprocess

def monitor_dns_logs():
    command = 'powershell -Command "Get-WinEvent -FilterHashtable @{LogName=\'Microsoft-Windows-DNSServer/Analytical\'; ID=3008} | Format-Table -Property TimeCreated,Message -AutoSize"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Monitoring DNS query logs:")
        print(result.stdout)
    else:
        print(f"Failed to monitor DNS logs: {result.stderr}")

monitor_dns_logs()