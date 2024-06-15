import subprocess

def monitor_network_connections():
    command = 'powershell -Command "Get-WinEvent -FilterHashTable @{LogName=\'Microsoft-Windows-TCPIP/Operational\'; ID=3} | Format-Table -Property TimeCreated,Message -AutoSize"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Monitoring network connections:")
        print(result.stdout)
    else:
        print(f"Failed to monitor network connections: {result.stderr}")

monitor_network_connections()