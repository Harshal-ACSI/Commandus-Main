print("Programme Loading...")

# IMPORTS:
import ctypes
import os
import sys
import webbrowser

import pyperclip
from AppOpener import open, close

from Library import (
    install_app,
    uninstall_app,
    run_registry_file,
    run_powershell7_command,
    run_powershell5_command,
    search_file,
    start_vm,
    stop_vm,
    connect_vm,
    list_vms,
    is_admin,
    list_2_str,
    upgrade_app,
)

# DATA:
Version = 1.0
Programmer = "Harshal"
Update = "20-09-2024"
Commands = {
    "Help": "Shows all the commands",
    "Exit": "Exits the program",
    "Clear": "Clears the screen",
    "Version": "Shows the version of the program",
    "Programmer": "Shows the programmer of the program",
    "Update": "Shows the update of the program",
    "Open": "Opens the application",
    "Close": "Closes the application",
    "ListApps": "Lists all the applications",
    "Install": "Installs the application",
    "Google": "Searches the query on Google",
    "Bing": "Searches the query on Bing",
    "Surf": "Surfs the URL",
    "H@ck": "Hacks the system",
    "PowerShell": "Runs the PowerShell command",
    "Locate": "Locates the file in the system",
    "Access": "Accesses the file",
    "Delete": "Deletes the file",
    "VM": "Manages the Virtual Machine",
    "Shutdown": "Shuts the computer down",
    "Restart": "Restarts the computer",
    "Logoff": "Logs out of the computer",
    "Sleep": "Lets the computer sleep",
}

# MAINLOOP:
os.system("cls")
while True:
    RawCommand = input("\nCommand: /")
    FormattedCommand = RawCommand.lower().strip().replace("/", " ")
    ParsedCommand = RawCommand.split(" ")

    if "hello" in RawCommand or "hi" in RawCommand:
        print("Hello There! How can I help you?")

    elif ParsedCommand[0] == "commandus":
        print(r"""
   ______                                          __          
  / ____/___  ____ ___  ____ ___  ____ _____  ____/ /_  _______
 / /   / __ \/ __ `__ \/ __ `__ \/ __ `/ __ \/ __  / / / / ___/
/ /___/ /_/ / / / / / / / / / / / /_/ / / / / /_/ / /_/ (__  ) 
\____/\____/_/ /_/ /_/_/ /_/ /_/\__,_/_/ /_/\__,_/\__,_/____/  
        
Version: 1.0 
© Copywrite Harshal                                                                                 
        """)

    # SYSTEM COMMANDS:
    elif RawCommand == "":
        pass
    elif ParsedCommand[0] == "exit" or ParsedCommand[0] == "e":
        break

    elif ParsedCommand[0] == "help" or ParsedCommand[0] == "h":
        for Command, Description in Commands.items():
            print(f"{Command} : {Description}")

    elif ParsedCommand[0] == "clear" or ParsedCommand[0] == "cls":
        os.system("cls")

    elif ParsedCommand[0] == "version" or ParsedCommand[0] == "v":
        print(f"Version: {Version}")

    elif ParsedCommand[0] == "programmer" or ParsedCommand[0] == "p":
        print(f"Programmer: {Programmer}")

    elif ParsedCommand[0] == "update" or ParsedCommand[0] == "u":
        print(f"Update: {Update}")

    # APPLICATION COMMANDS:
    elif ParsedCommand[0] == "open" or ParsedCommand[0] == "o":
        Appname = (
            str(ParsedCommand[1:])
            .replace("ms ", "microsoft ")
            .replace(" ", "")
            .replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .replace(",", "")
        )
        open(Appname, match_closest=True, throw_error=False)

    elif ParsedCommand[0] == "close" or ParsedCommand[0] == "c":
        Appname = (
            str(ParsedCommand[1:])
            .replace("ms ", "microsoft ")
            .replace(" ", "")
            .replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .replace(",", "")
        )
        close(Appname, match_closest=True, throw_error=False)

    elif ParsedCommand[0] == "listapps" or ParsedCommand[0] == "laps":
        print("List of all the applications:")
        for App in os.listdir("C:/Program Files"):
            print(App)

    elif ParsedCommand[0] == "install":
        install_app(
            str(ParsedCommand[1:])
            .replace("ms ", "microsoft ")
            .replace(" ", "")
            .replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .replace(",", "")
        )
    elif ParsedCommand[0] == "uninstall":
        uninstall_app(
            str(ParsedCommand[1:])
            .replace("ms ", "microsoft ")
            .replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .replace(",", "")
        )

    elif ParsedCommand[0] == "upgrade":
        upgrade_app(
            str(ParsedCommand[1:])
            .replace("ms ", "microsoft ")
            .replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .replace(",", "")
        )

    # INTERNET COMMANDS:
    elif ParsedCommand[0] == "google" or ParsedCommand[0] == "g":
        if len(ParsedCommand) > 1:
            query = " ".join(ParsedCommand[1:])
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            print("Please specify a search query.")

    elif ParsedCommand[0] == "bing" or ParsedCommand[0] == "b":
        if len(ParsedCommand) > 1:
            query = " ".join(ParsedCommand[1:])
            webbrowser.open(f"https://www.bing.com/search?q={query}")
        else:
            print("Please specify a search query.")

    elif ParsedCommand[0] == "surf" or ParsedCommand[0] == "s":
        if len(ParsedCommand) > 1:
            query = " ".join(ParsedCommand[1:])
            webbrowser.open(f"https://www.{query}")
        else:
            print("Please specify a URL.")

    # POWERSHELL:
    elif ParsedCommand[0] == "h@ck" or ParsedCommand[0] == "@":
        if not is_admin():
            script_to_run = (
                r"C:\Users\parent\Jetbrains\Pycharm_Projects\Commandus\Hack.py"
            )
            print(f"Running {script_to_run} with elevated privileges...")
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, script_to_run, None, 1
            )
        else:
            run_registry_file(r"C:\Users\parent\Documents\Registry\DeleteBlocksi.reg")
            print("H@cked Successfully")

    elif ParsedCommand[0] == "powershell" or ParsedCommand[0] == "ps":
        if ParsedCommand[1] == "7":
            try:
                PSCommand = input("PS7: ")
                run_powershell7_command(PSCommand)
            except:
                print("Invalid Command")
        elif ParsedCommand[1] == "5":
            try:
                PSCommand = input("PS5: ")
                run_powershell5_command(PSCommand)
            except:
                print("Invalid Command")
        else:
            print("Invalid Command; Wrong Powershell Version.")

    # FILE SYSTEM COMMANDS:
    elif ParsedCommand[0] == "locate" or ParsedCommand[0] == "l":
        try:
            if ParsedCommand[2] == "in":
                File = ParsedCommand[1]
                Directory = ParsedCommand[3]
                File_Path = search_file(Directory, File)
                File_Path2 = search_file(Directory, File.replace("_", " "))
                if File_Path:
                    print(f"File found at: {File_Path}")
                    pyperclip.copy(File_Path)
                elif File_Path2:
                    print(f"File found at: {File_Path2}")
                    pyperclip.copy(File_Path2)
                else:
                    print("File not found.")
            else:
                print("Invalid Command")

        except:
            File = (
                str(ParsedCommand[1:])
                .replace("[", "")
                .replace("]", "")
                .replace("'", "")
                .replace(",", "")
            )
            Directory = r"C:\ "
            File_Path = search_file(Directory.replace(" ", ""), File)
            if File_Path:
                print(f"File found at: {File_Path}")
                pyperclip.copy(File_Path)
            else:
                print("File not found.")

    elif ParsedCommand[0] == "access" or ParsedCommand[0] == "a":
        try:
            File = list_2_str(ParsedCommand[1:])
            os.startfile(File)
        except:
            print("Invalid Command")

    elif ParsedCommand[0] == "delete" or ParsedCommand[0] == "d":
        try:
            File = list_2_str(ParsedCommand[1:])
            os.remove(File)
            print(f"{File} deleted successfully.")
        except:
            print("Invalid Command")

    # VIRTUAL MACHINE COMMANDS:
    elif ParsedCommand[0] == "vm":
        if ParsedCommand[1] == "start" or ParsedCommand[1] == "+":
            start_vm(list_2_str(ParsedCommand[2:]))
        elif ParsedCommand[1] == "stop" or ParsedCommand[1] == "-":
            stop_vm(list_2_str(ParsedCommand[2:]))
        elif ParsedCommand[1] == "connect" or ParsedCommand[1] == "=":
            print("Connecting to the VM...")
            connect_vm(list_2_str(ParsedCommand[2:]))
        elif ParsedCommand[1] == "list":
            list_vms()

    # OPERATING SYSTEM COMMANDS:
    elif ParsedCommand[0] == "shutdown" or ParsedCommand[0] == "sd":
        os.system("shutdown /s /t 1")

    elif (
            ParsedCommand[0] == "restart"
            or ParsedCommand[0] == "reboot"
            or ParsedCommand[0] == "r"
    ):
        os.system("shutdown /r /t 1")

    elif (
            ParsedCommand[0] == "logoff"
            or ParsedCommand[0] == "lock"
            or ParsedCommand[0] == "lk"
    ):
        os.system("shutdown /l")

    elif (
            ParsedCommand[0] == "sleep"
            or ParsedCommand[0] == "suspend"
            or ParsedCommand[0] == "sl"
            or ParsedCommand[0] == "slp"
            or ParsedCommand[0] == "sp"
    ):
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    else:
        try:
            run_powershell7_command(RawCommand)
        except:
            print("Invalid Command")
