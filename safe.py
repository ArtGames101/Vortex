import sys, os, time, random, psutil, subprocess
from user import safezone as name
from safedata import new
from safedata import parental
from safedata.pet import ptype as pt

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n0> ").lower().strip()

def loading():
    clear_screen()
    print("Starting SafeZone... |")
    time.sleep(1)
    clear_screen()
    print("Starting SafeZone... /")
    time.sleep(1)

    clear_screen()
    print("Starting SafeZone... -")
    time.sleep(1)
    clear_screen()
    print("Starting SafeZone... |")
    time.sleep(1)
    clear_screen()
    print("Starting SafeZone... -")
    time.sleep(1)
    clear_screen()
    print("Starting SafeZone... \ ")
    time.sleep(1)
    clear_screen()
    print("Starting SafeZone... |")
    time.sleep(1)
    clear_screen()
    print("Starting SafeZone... |")
    time.sleep(1)
    clear_screen()
    print("Starting SafeZone... /")
    time.sleep(1)
    clear_screen()
    print("Starting SafeZone... -")
    time.sleep(1)
    if new.isn == True:
        intro()
    else:
        main()
IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n0> ").lower().strip()

def intro():
    clear_screen()
    print("Welcome to The ArtSystem SafeZone!\n"
          "\n"
          "A place where you or your child can play games together and raise a pet!\n"
          "\n"
          "You can change back to the Normal ArtSystem launcher if you wish to!")
    input("\nPush Enter to continue")
    setup()

def setup():
    clear_screen()
    print("Setup\n"
          "\n"
          "Your Child's name has already been set to {}!".format(name.NAME))
    print("But we also have to setup a Parental Password\n"
          "Please enter one here!  __________")
    choice = user_choice()
    par = open("safedata/parental.py", "w")
    par.write("PA = '{}'".format(choice))
    n = open("safedata/new.py", "w")
    n.write("isn = False")
    input("Setup Complete!\n"
          "Push Enter to continue!")
    par.close()
    n.close()
    subprocess.call((sys.executable, "run.py"))


def main():
    clear_screen()
    print("=. Welcome {}!         | {}\n"
          "================================================".format(name.NAME, time.ctime()))
    print("\n"
          "1. Pet  | 2. Game Store | 3. Installed Games")
    choice = user_choice()
    if choice == "1":
        pet()
    if choice == "2":
        store()
    if choice == "3":
        installed()
    if choice == "=":
        parental()
    else:
        main()

def parental():
    parent()

def parent():
    clear_screen()
    print("==========\n"
          " Settings \n"
          "==========\n")
    print("a. Change back to ArtSystem")
    print("\n"
          "0. Back")
    choice = user_choice()
    if choice == "a":
        c = open("data/safezone.py", "w")
        c.write("NAME = None")
        input("Changed Back to ArtSystem Launcher!")
        c.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "0":
        main()
def store():
    clear_screen()
    print("==========\n"
          " Parental \n"
          " Password \n"
          "==========\n")
    choice = user_choice()
    if choice == parental.PA:
        sstore()
    else:
        main()

def sstore():
    clear_screen()
    print("===========\n"
          "  Comming  \n"
          "   Soon!   \n"
          "===========\n")
    input("Shop is in Development!")
    main()
def pet():
    clear_screen()
    try:
        if pt.ptype == None:
            clear_screen()
            print("Choose your pet!")
            print("\n"
                  "1. Dog  | 2. Cat | 3. Fish")
            choice = user_choice()
            if choice == "1":
                dog = open("safedata/pet/ptype.py", "w")
                dog.write("ptype = 'Dog'")
                input("Yay you have chosen a 'Dog' to be your pet!")
                input("Push Enter to restart!")
                dog.close()
                subprocess.call((sys.executable, "run.py"))
            if choice == "2":
                cat = open("safedata/pet/ptype.py", "w")
                cat.write("ptype = 'Cat'")
                input("Yay you have chosen a 'Cat' to be your pet!")
                input("Push Enter to restart!")
                cat.close()
                subprocess.call((sys.executable, "run.py"))
            if choice == "3":
                fish = open("safedata/pet/ptype.py", "w")
                fish.write("ptype = 'Fish'")
                input("Yay you have chosen a 'Fish' to be your pet!")
                input("Push Enter to restart!")
                fish.close()
                subprocess.call((sys.executable, "run.py"))
        else:
            cpet()
    except:
        wtype = open("safedata/pet/ptype.py", "w")
        wtype.write("ptype = None")
        input("There Was an error in the pet file we have just fixed it for you!\n"
              "You will have to restart to take effect!\n"
              "\n"
              "Push Enter to continue!")
        wtype.close()
        subprocess.call((sys.executable, "run.py"))

def cpet():
    h = ["[=       ]", "[====    ]", "[========]"]
    hu = ["[========]", "[====    ]", "[=       ]"]
    games = ["Fetch", "Tricks"]
    clear_screen()
    print("Your pet {}!  | Happy {}  | Hunger {}\n"
          "===================================================".format(pt.ptype, random.choice(h), random.choice(hu)))
    print("\n"
          "==========================================\n"
          "|1. Feed |2. Play |0. Back |")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        input("You fed your pet, {} Food! -1 Hunger".format(pt.ptype))
        cpet()
    if choice == "2":
        clear_screen()
        input("You Played {} With your pet".format(random.choice(games)))
        cpet()
    if choice == "0":
        main()

 
loading()
