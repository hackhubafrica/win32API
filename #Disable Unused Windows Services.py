import subprocess

def disable_unused_services(service_name):
    command = f'sc config {service_name} start= disabled'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Service '{service_name}' disabled successfully.")
    else:
        print(f"Failed to disable service '{service_name}': {result.stderr}")

# Example usage
disable_unused_services("Telnet")