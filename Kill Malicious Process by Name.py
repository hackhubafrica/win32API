import subprocess

def kill_malicious_process(process_name):
    command = f'taskkill /IM {process_name} /F'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Process '{process_name}' killed successfully.")
    else:
        print(f"Failed to kill process '{process_name}': {result.stderr}")

# Example usage
kill_malicious_process("malicious.exe")