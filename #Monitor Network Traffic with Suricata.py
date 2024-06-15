import subprocess

def monitor_network_with_suricata(interface):
    command = f'suricata -c /etc/suricata/suricata.yaml -i {interface}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Monitoring network traffic with Suricata:")
        print(result.stdout)
    else:
        print(f"Failed to monitor network with Suricata: {result.stderr}")

# Example usage
monitor_network_with_suricata("eth0")