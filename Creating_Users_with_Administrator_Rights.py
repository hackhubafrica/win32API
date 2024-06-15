import subprocess

def create_admin_user(username, password):
    command_user = f"net user {username} {password} /add"
    command_admin = f"net localgroup administrators {username} /add"
    
    result_user = subprocess.run(command_user, shell=True, capture_output=True, text=True)
    if result_user.returncode == 0:
        print(f"User '{username}' created successfully.")
    else:
        print(f"Failed to create user: {result_user.stderr}")
    
    result_admin = subprocess.run(command_admin, shell=True, capture_output=True, text=True)
    if result_admin.returncode == 0:
        print(f"User '{username}' added to the Administrators group successfully.")
    else:
        print(f"Failed to add user to Administrators group: {result_admin.stderr}")

# Example usage
create_admin_user("newadmin", "password123")