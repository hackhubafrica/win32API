import subprocess

def audit_group_policy():
    command = 'gpresult /H gpresult.html'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Auditing Group Policy settings:")
        print(result.stdout)
    else:
        print(f"Failed to audit Group Policy: {result.stderr}")

audit_group_policy()