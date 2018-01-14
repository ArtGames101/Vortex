# -*- coding: utf-8 -*-
# (c) ArtGames101 2017

# This is the upgrade module (DONT TAMPER WITH!)
# ✓ Verified
import subprocess
import sys, os, time, random
from user import logindata
from user import loginpass

repo = "https://github.com/ArtGames101/ArtSystem.git"
t = [2, 4, 6, 8, 10]
IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def user_choice():
    return input("\n>>> ").lower().strip()

def warning():
    clear_screen()
    print("==================\n"
          " ArtSystem Update \n"
          "==================\n")
    print("Would you like to upgrade to ArtSystem v10.7-Stable?\n"
          "\n"
          "WARNING! : If the newest version has not been released\n"
          "           The Current version will be installed\n"
          "\n"
          "WARNING! : if you do not have wifi it will not install\n"
          "           but it will say it has! so dont mess with\n"
          "           the settings until it has actualy installed!\n"
          "\n"
          "\n"
          "1. Install ArtSystem v10.7\n"
          "\n"
          "0. Exit")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        print("1 Install  2 Transfer data 3 Confirm Update")
        print("\n"
              "Installing ArtSystem v10.7-Stable...")
        time.sleep(random.choice(t))
        subprocess.call(("git", "clone", repo))
        time.sleep(random.choice(t))
        clear_screen()
        print("✓ Install  2 Transfer data 3 Confirm Update")
        print("\n"
              "Transfering data to v10.7-Stable...")
        user = open("ArtSystem/user/logindata.py", "w")
        user.write("USERNAME = '{}'".format(logindata.USERNAME))
        user.close()
        passw = open("ArtSystem/user/loginpass.py", "w")
        passw.write("PASSWORD = '{}'".format(loginpass.PASSWORD))
        passw.close()
        time.sleep(random.choice(t))
        clear_screen()
        print("✓ Install  ✓ Transfer data 3 Confirm Update")
        print("\n"
              "Confirming Update...")
        time.sleep(random.choice(t))
        clear_screen()
        input("Push Enter to see information!")
        info()
    if choice == "0":
        subprocess.call((sys.executable, "run.py"))


def info():
    clear_screen()
    print("=============\n"
          " Information \n"
          "=============\n")
    print("Press 1 to automaticly go to the next version!\n"
          "\n"
          "Or push 0 to just exit and normaly run it!")
    choice = user_choice()
    if choice == "1":
        n = open("data/upgradestay.py", "w")
        n.write("stay = False")
        input("Push Enter!")
        n.close()
        subprocess.call((sys.executable, "ArtSystem/run.py"))
    if choice == "0":
        sys.exit()
        
    
warning()
