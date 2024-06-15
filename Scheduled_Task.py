import subprocess

def create_scheduled_task(task_name, file_path):
    command = f'schtasks /create /tn "{task_name}" /tr "{file_path}" /sc onlogon /rl highest /f'
    subprocess.run(command, shell=True)

# Example usage
create_scheduled_task("MyTask", r"C:\path\to\your\program.exe")