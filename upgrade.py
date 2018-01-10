# (c) ArtGames101 2017

# This is the upgrade module (DONT TAMPER WITH!)
import subprocess
import sys, os

repo = "https://github.com/ArtGames101/ArtSystem.git"

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
    print("Would you like to upgrade to ArtSystem v10.5-Stable?\n"
          "\n"
          "WARNING! : If the newest version has not been released\n"
          "           The Current version will be installed\n"
          "\n"
          "by typing 1 you agree this may brake ArtSystem!\n"
          "\n"
          "0. Exit")
    choice = user_choice()
    if choice == "1":
        subprocess.call(("git", "clone", repo))
        input("Push Enter for instructions!")
        info()
    if choice == "0":
        subprocess.call(("run.py"))


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
