import subprocess

def monitor_http_traffic(interface):
    command = f'tshark -i {interface} -f "port 80" -Y "http.request.method == GET"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("HTTP Traffic Monitoring:")
        print(result.stdout)
    else:
        print(f"Failed to monitor HTTP traffic: {result.stderr}")

# Example usage
monitor_http_traffic("eth0")