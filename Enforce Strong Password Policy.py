import subprocess

def enforce_password_policy():
    command = 'net accounts /minpwlen:12 /maxpwage:30 /minpwage:1 /uniquepw:5 /domain'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Strong password policy enforced successfully.")
    else:
        print(f"Failed to enforce strong password policy: {result.stderr}")

enforce_password_policy()