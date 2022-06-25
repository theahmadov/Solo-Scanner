from colorama import *
import os
from time import *



def menu():
    print(Fore.GREEN+"""
 ____        _            ____                                  
/ ___|  ___ | | ___      / ___|  ___ __ _ _ __  _ __   ___ _ __ 
\___ \ / _ \| |/ _ \ ____\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 ___) | (_) | | (_) |_____|__) | (_| (_| | | | | | | |  __/ |   
|____/ \___/|_|\___/     |____/ \___\__,_|_| |_|_| |_|\___|_|   

""")
    print(Fore.RED+"""
        [1] Find Potantial Sql Vulnerable 
        [2] Port Scanner
    
    """)

def sql(url):
    print()
if __name__ == "__main__":

    os.system("clear")
    menu()
    n = input(Fore.BLUE+"\nPlease Select :")
    url = input(Fore.BLUE+"\nPlease Input Target URL : ")
    if n == "1":
        sql(url)