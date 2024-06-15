import subprocess

def monitor_network_with_zeek(interface):
    command = f'zeek -i {interface} -C zeek.conf'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Monitoring network traffic with Zeek:")
        print(result.stdout)
    else:
        print(f"Failed to monitor network with Zeek: {result.stderr}")

# Example usage
monitor_network_with_zeek("eth0")