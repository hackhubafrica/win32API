import subprocess

def audit_ad_groups():
    command = 'dsquery group -limit 0 | dsget group -members -expand'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Auditing Active Directory group memberships:")
        print(result.stdout)
    else:
        print(f"Failed to audit AD group memberships: {result.stderr}")

audit_ad_groups()