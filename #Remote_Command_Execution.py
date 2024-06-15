import subprocess

def remote_command_execution(target_ip, username, password, command):
    psexec_path = "/path/to/psexec.exe"  # Replace with the actual path to PsExec executable
    command = f"{psexec_path} \\\\{target_ip} -u {username} -p {password} {command}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Command '{command}' executed successfully on {target_ip}.")
        print(result.stdout)
    else:
        print(f"Failed to execute command on {target_ip}: {result.stderr}")

# Example usage
remote_command_execution("192.168.1.100", "administrator", "password123", "hostname")