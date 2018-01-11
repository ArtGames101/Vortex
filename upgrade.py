# -*- coding: utf-8 -*-
# (c) ArtGames101 2017

# This is the upgrade module (DONT TAMPER WITH!)
# ✓
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
    print("Would you like to upgrade to ArtSystem v10.6-Stable?\n"
          "\n"
          "WARNING! : If the newest version has not been released\n"
          "           The Current version will be installed\n"
          "\n"
          "by typing 1 you agree this may brake ArtSystem!\n"
          "\n"
          "0. Exit")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        print("1 Install  2 Trancefer data 3 Confirm Update")
        print("\n"
              "Installing ArtSystem v10.6-Stable...")
        subprocess.call(("git", "clone", repo))
        time.sleep(random.choice(t))
        clear_screen()
        print("✓ Install  2 Trancefer data 3 Confirm Update")
        print("\n"
              "Trancefering data to v10.6-Stable...")
        user = open("ArtSystem/user/logindata.py", "w")
        user.write("USERNAME = '{}'".format(logindata.USERNAME))
        user.close()
        passw = open("ArtSystem/user/loginpass.py", "w")
        passw.write("PASSWORD = '{}'".format(loginpass.PASSWORD))
        passw.close()
        time.sleep(random.choice(t))
        clear_screen()
        print("✓ Install  ✓ Trancefer data 3 Confirm Update")
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
    print("\n"
          "Make Sure to move the new version into the folder that this version is in!\n"
          "then run the new version!")
    input("\n"
          "Exit")
    sys.exit(50)
    
warning()
