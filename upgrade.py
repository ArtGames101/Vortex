# -*- coding: utf-8 -*-
# (c) ArtGames101 2017

# This is the upgrade module (DONT TAMPER WITH!)
# ✓ = Verified

import subprocess
import sys, os, time, random
from user import logindata
from user import loginpass
from user import img

repo = "https://github.com/ArtSystemStudios/Vortex.git"
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
    print("Would you like to upgrade to ArtSystem Software Update?\n"
          "\n"
          "WARNING! : If the newest version has not been released\n"
          "           The Current version will be installed\n"
          "\n"
          "WARNING! : if you do not have wifi it will not install\n"
          "           but it will say it has! so dont mess with\n"
          "           the settings until it has actualy installed!\n"
          "INFO: if you do not have the correct data for logindata\n"
          "      , loginpass & img then it will not work!"
          "\n"
          "1. Install Software Update\n"
          "\n"
          "0. Exit")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        print("1 Install  2 Transfer data 3 Confirm Update\n"
              "---------")
        print("\n"
              "Installing Software Update...")
        time.sleep(random.choice(t))
        subprocess.call(("git", "clone", repo))
        time.sleep(random.choice(t))
        clear_screen()
        print("✓ Install  2 Transfer data 3 Confirm Update\n"
              "--------------------------")
        print("\n"
              "Transfering data to Software Update...")
        try:
            user = open("Vortex/user/logindata.py", "w")
            user.write("USERNAME = '{}'".format(logindata.USERNAME))
            user.close()
            passw = open("Vortex/user/loginpass.py", "w")
            passw.write("PASSWORD = '{}'".format(loginpass.PASSWORD))
            passw.close()
            imga = open("Vortex/user/img.py", "w")
            imga.write("usrimg = '{}'".format(img.usrimg))
            trance = True
        except:
            trance = False
        time.sleep(random.choice(t))
        clear_screen()
        if trance == False:
            print("✓ Install  X Transfer data 3 Confirm Update\n"
                  "-------------------------------------------\n")
        else:
            print("✓ Install  ✓ Transfer data 3 Confirm Update\n"
                  "-------------------------------------------\n")
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
    print("(A) ArtSystem Vortex Software Update\n"
          "======================================")
    print("\n\n1. Go to New Version | 2. Changelog  | 0. Exit")
    choice = user_choice()
    if choice == "1":
        n = open("data/upgradestay.py", "w")
        n.write("stay = False")
        input("Push enter to save this data!")
        n.close()
        subprocess.call((sys.executable, "Vortex/run.py"))
    if choice == "2":
        try:
            from ArtSystem import run
            run.fchangelog()
        except:
            input("Unable to get Changelog!")
            info()
    if choice == "0":
        sys.exit()
        
    
warning()
