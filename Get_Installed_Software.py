import winreg

def get_installed_software():
    uninstall_key_path = r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall'
    installed_software = []

    for hkey in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER):
        with winreg.OpenKey(hkey, uninstall_key_path) as uninstall_key:
            for i in range(winreg.QueryInfoKey(uninstall_key)[0]):
                subkey_name = winreg.EnumKey(uninstall_key, i)
                with winreg.OpenKey(uninstall_key, subkey_name) as subkey:
                    try:
                        display_name = winreg.QueryValueEx(subkey, 'DisplayName')[0]
                        installed_software.append(display_name)
                    except FileNotFoundError:
                        pass

    return installed_software

software_list = get_installed_software()
for software in software_list:
    print(software)