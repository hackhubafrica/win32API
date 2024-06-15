import subprocess

def check_cis_compliance():
    command = 'lynis audit system --pentest --quick'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Checking system compliance with CIS benchmarks:")
        print(result.stdout)
    else:
        print(f"Failed to check CIS compliance: {result.stderr}")

check_cis_compliance()