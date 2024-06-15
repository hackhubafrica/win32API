import subprocess

def audit_account_policies():
    command = 'net accounts /domain'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("User Account Policies:")
        print(result.stdout)
    else:
        print(f"Failed to audit account policies: {result.stderr}")

audit_account_policies()