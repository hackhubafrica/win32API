import subprocess

def check_missing_patches():
    command = 'wmic qfe list brief /format:table'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Missing Patches:")
        print(result.stdout)
    else:
        print(f"Failed to check missing patches: {result.stderr}")

check_missing_patches()