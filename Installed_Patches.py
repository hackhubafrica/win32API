import subprocess

def get_installed_patches():
    command = "wmic qfe list"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Installed Patches:")
        print(result.stdout)
    else:
        print(f"Failed to retrieve installed patches: {result.stderr}")

get_installed_patches()