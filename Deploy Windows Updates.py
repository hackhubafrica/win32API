import subprocess

def deploy_windows_updates():
    command = 'powershell -Command "Install-WindowsUpdate -MicrosoftUpdate -AcceptAll -AutoReboot"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Deploying Windows updates:")
        print(result.stdout)
    else:
        print(f"Failed to deploy Windows updates: {result.stderr}")

deploy_windows_updates()