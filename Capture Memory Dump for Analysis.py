import subprocess

def capture_memory_dump(process_name):
    command = f'procdump64.exe -accepteula -ma {process_name} dump.dmp'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Memory dump of process '{process_name}' captured successfully.")
    else:
        print(f"Failed to capture memory dump: {result.stderr}")

# Example usage
capture_memory_dump("malicious.exe")