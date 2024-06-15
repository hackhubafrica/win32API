import subprocess

def monitor_network_traffic(interface):
    command = f'tshark -i {interface} -f "not port 22" -Y "http.request.method == GET"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Monitoring network traffic:")
        print(result.stdout)
    else:
        print(f"Failed to monitor network traffic: {result.stderr}")

# Example usage
monitor_network_traffic("eth0")