from colorama import *
import os
from time import *


def progress(percent=0, width=40):
    left = width * percent // 100
    right = width - left
    tags = "█" * left
    spaces = " " * right
    percents = f"{percent:.0f}%"
    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)

def load(x):
    for i in range(x):
        progress(i)
        sleep(0.01)

def menu():
    print(Fore.GREEN+"""
 ____        _            ____                                  
/ ___|  ___ | | ___      / ___|  ___ __ _ _ __  _ __   ___ _ __ 
\___ \ / _ \| |/ _ \ ____\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 ___) | (_) | | (_) |_____|__) | (_| (_| | | | | | | |  __/ |   
|____/ \___/|_|\___/     |____/ \___\__,_|_| |_|_| |_|\___|_|   

""")
    print(Fore.RED+"""
    [1] Website Vulnerable Scanner
        [!] Features : 
            [+] Find Potantial Sql Vulnerable 
            [+] Port Scanner
    
    """)

if __name__ == "__main__":

    os.system("clear")
    menu()
    load(101)
    print(" ")
    n = input(Fore.BLUE+"\nPlease Select :")
    print(" ")
    if n == "1":
        os.system("sudo python3 ./web/main.py")