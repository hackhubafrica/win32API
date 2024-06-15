import subprocess

def check_expired_certificates():
    command = 'powershell -Command "Get-ChildItem -Path Cert:\\LocalMachine\\My | Where-Object {$_.NotAfter -lt (Get-Date)} | Format-Table -Property Thumbprint,Subject,NotAfter -AutoSize"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Checking for expired certificates:")
        print(result.stdout)
    else:
        print(f"Failed to check expired certificates: {result.stderr}")

check_expired_certificates()