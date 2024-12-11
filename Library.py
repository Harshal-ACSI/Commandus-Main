import ctypes
import os
import subprocess


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_registry_file(file_path):
    try:
        # Use reg import to apply the registry file
        result = subprocess.run(
            ["reg", "import", file_path], capture_output=True, text=True, check=True
        )
        if result.returncode == 0:
            print(f"Registry file '{file_path}' imported successfully.")
        else:
            print(
                f"Failed to import registry file '{file_path}'. Output: {result.stdout}"
            )
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")


def run_powershell7_command(command):
    try:
        # Specify the path to the PowerShell 7 executable
        powershell7_path = r"C:\Program Files\PowerShell\7\pwsh.exe"
        result = subprocess.run(
            [powershell7_path, "-Command", command],
            capture_output=True,
            text=True,
            check=True,
        )
        print(f"PowerShell: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")


def run_powershell5_command(command):
    try:
        result = subprocess.run(
            ["powershell", "-Command", command],
            capture_output=True,
            text=True,
            check=True,
        )
        print(f"Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")


def search_file(root_directory, file_name):
    for root, dirs, files in os.walk(root_directory):
        print(f"Searching in:{root}")
        if file_name in files:
            return os.path.join(root, file_name)
    return None


def install_app(app_name):
    try:
        print("\n")
        os.system(f"winget search {app_name}")
        app_id = input("Enter the ID of the application: ")
        if (
            app_id == ""
            or app_id == "/e"
            or app_id == "/exit"
            or app_id == "/q"
            or app_id == "/quit"
            or app_id == "/cancel"
            or app_id == "/abort"
            or app_id == "/a"
        ):
            print("Installation aborted due to invalid Application ID.")
        else:
            os.system(f"winget install {app_id}")
    except:
        print("Invalid Command")


def uninstall_app(app_name):
    try:
        os.system(f"winget search {app_name}")
        app_id = input("Enter the ID of the application: ")
        uninstall_command = f'winget uninstall --name "{app_id}"'
        result = subprocess.run(
            uninstall_command, capture_output=True, text=True, shell=True
        )
        if result.returncode == 0:
            print(f"{app_name} uninstalled successfully.")
        else:
            print(f"Failed to uninstall {app_name}. Output: {result.stdout}")
    except Exception as e:
        print(f"An error occurred: {e}")


def upgrade_app(app_name):
    try:
        os.system(f"winget search {app_name}")
        app_id = input("Enter the ID of the application: ")
        upgrade_command = f'winget upgrade --name "{app_name}"'
        result = subprocess.run(
            upgrade_command, capture_output=True, text=True, shell=True
        )
        if result.returncode == 0:
            print(f"{app_name} upgraded successfully.")
        else:
            print(f"Failed to upgrade {app_name}. Output: {result.stdout}")
    except Exception as e:
        print(f"An error occurred: {e}")


def list_2_str(list_1):
    return str(list_1).replace("']", "").replace("['", "").replace("', '", " ")


def start_vm(vm_name):
    try:
        # Use PowerShell to start the VM
        start_command = f'Start-VM -Name "{vm_name}"'
        result = subprocess.run(
            ["powershell", "-Command", start_command],
            capture_output=True,
            text=True,
            check=True,
        )
        if result.returncode == 0:
            print(f"VM '{vm_name}' started successfully.")
        else:
            print(f"Failed to start VM '{vm_name}'. Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")


def stop_vm(vm_name):
    try:
        # Use PowerShell to stop the VM
        stop_command = f'Stop-VM -Name "{vm_name}"'
        result = subprocess.run(
            ["powershell", "-Command", stop_command],
            capture_output=True,
            text=True,
            check=True,
        )
        if result.returncode == 0:
            print(f"VM '{vm_name}' stopped successfully.")
        else:
            print(f"Failed to stop VM '{vm_name}'. Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")


def connect_vm(vm_name):
    try:
        # Use vmconnect.exe to connect to the VM
        connect_command = f'vmconnect.exe localhost "{vm_name}"'
        result = subprocess.run(
            connect_command, capture_output=True, text=True, shell=True
        )
        if result.returncode == 0:
            print(f"Connected to VM '{vm_name}' successfully.")
        else:
            print(f"Failed to connect to VM '{vm_name}'. Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")


def list_vms():
    try:
        # Use PowerShell to list all VMs
        list_command = "Get-VM | Select-Object -Property Name"
        result = subprocess.run(
            ["powershell", "-Command", list_command],
            capture_output=True,
            text=True,
            check=True,
        )
        if result.returncode == 0:
            print("List of VMs:")
            print(result.stdout)
        else:
            print(f"Failed to list VMs. Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")
