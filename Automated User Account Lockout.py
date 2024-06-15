import subprocess

def lockout_user_account(username):
    command = f'net user {username} /lock'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"User account '{username}' locked out successfully.")
    else:
        print(f"Failed to lock out user account: {result.stderr}")

# Example usage
lockout_user_account("john.doe")