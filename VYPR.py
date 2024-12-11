print("Programme Loading...")

# IMPORTS:
import os
import threading

from pynput.keyboard import Key, Listener

# DATA:
Version = 0.1
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
global Path
Path = ''
global RawCommand
RawCommand = ''


# Threads
def Printer():
    global Path
    global RawCommand
    Old_Path = 'a'
    Old_Command = 'a'
    while True:
        if Path != Old_Path or RawCommand != Old_Command:
            os.system('cls')
            if Path == '':
                print('@ Root')
            else:
                print('@', Path)
            print("Command/", RawCommand)

        Old_Path = Path
        Old_Command = RawCommand


PRINTER_THREAD = threading.Thread(target=Printer())
PRINTER_THREAD.start()


def on_release(key):
    print(f'\nKey pressed : {key}')  # Add your code here for when keys are released

    if key == Key.esc:
        return False  # Stop listener, stops the script and exits program


with Listener(on_release=on_release) as listener:
    listener.join()
