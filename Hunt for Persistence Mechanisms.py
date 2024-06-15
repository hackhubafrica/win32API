import subprocess

def hunt_persistence_mechanisms():
    command = 'powershell -Command "Get-ScheduledTask -TaskPath \'\\\' -TaskName * | Format-Table -Property TaskName,TaskPath,State,NextRunTime,LastRunTime -AutoSize"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Hunting for persistence mechanisms:")
        print(result.stdout)
    else:
        print(f"Failed to hunt persistence mechanisms: {result.stderr}")

hunt_persistence_mechanisms()