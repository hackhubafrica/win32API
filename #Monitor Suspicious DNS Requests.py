import subprocess

def monitor_dns_requests():
    try:
        # Set execution policy
        set_policy_command = 'powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force"'
        set_policy_result = subprocess.run(set_policy_command, shell=True, capture_output=True, text=True)
        if set_policy_result.returncode != 0:
            raise Exception(f"Failed to set execution policy: {set_policy_result.stderr}")

        # Command to get DNS events
        command = 'powershell -Command "Get-WinEvent -FilterHashTable @{LogName=\'Microsoft-Windows-DNS-Client/Operational\'; ID=3009} | Format-Table -Property TimeCreated,Message -AutoSize"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            if "No events were found" in result.stdout:
                print("No DNS events found.")
            else:
                print("Monitoring for suspicious DNS requests:")
                print(result.stdout)
        else:
            raise Exception(f"Failed to monitor DNS requests: {result.stderr}")
    
    except Exception as e:
        print(e)

monitor_dns_requests()
