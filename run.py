# (c) ArtGames101 2017
# This Console was created by ArtGames101 and is under copyright notice!

# If you want to create your own version of this be my guest! there is sooooooo
# much code like ALOT and its confusing!
import sys, os, random, time, subprocess, psutil
import urllib
import config as c
from data import gold as g
from data import alphapps as alpha
from log import notification
from user import safezone
from data import upgradestay as upg
try:
    from user import logindata as logind
    from user import loginpass as loginp
    from user import parental as parent
    from user import reminder as remind
except:
    pass

# Version
version = "v10.7-Stable"
# Next Version
nextup = "v10.8-Stable"

error = open("log/lasterror.txt", "w")
start = open("log/startlog.txt", "w")
santa = False
games = ["snake", "BattleSim", "squirrel", "Santa", "Tetris", "GunRush", "DocCreator", "VF"]
apps = ["DocCreator", "VF"]
gm = 5
ap = 2
pa = 2
ad = ["Go Gold and get ALPHA games that are comming soon!", "Get Alphapps to install the newest apps!", "Squirrel (GO GOLD!) (Eat other squirrels to become the OMEGA SQUIRREL)", "Snake (a game where you have to eat apples!)", "BattleSim (The best battle simulator for python!)", "Tetris  (A Game where you have to stack blocks!)"]
try:
    import snake
except Exception as e:
    exc = '{}: {}'.format(type(e).__name__, e)
    error.write(exc)

try:
    import tetris
except Exception as e:
    exc = '{}: {}'.format(type(e).__name__, e)
    error.write(exc)
try:
    from BattleSim import run as battle
except Exception as e:
    exc = '{}: {}'.format(type(e).__name__, e)
    error.write(exc)

try:
    import squirrel
except Exception as e:
    exc = '{}: {}'.format(type(e).__name__, e)
    error.write(exc)

try:
    import santa
except Exception as e:
    exc = '{}: {}'.format(type(e).__name__, e)
    error.write(exc)

try:
    import introduction
except Exception as e:
    exc = '{}: {}'.format(type(e).__name__, e)
    error.write(exc)

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def loading():
    clear_screen()
    if IS_WINDOWS:
        try:
            os.system("welcome.vbs")
        except:
            pass
    else:
        try:
            subprocess.call(('notify-send', 'ArtSystem Startup', 'ArtSystem is starting up...'))
        except:
            try:
                subprocess.call(('zenity', '--info', '--text="ArtSystem is starting up!"', '--timeout=5 2'))
                clear_screen()
            except:
                pass
    print("\n"
      "     /------------\      \n"
      "    /              \     \n"
      "   /                \    \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |__________________|   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "                         \n"
      "        ArtSystem        \n")
    print("Starting ArtSystem... |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /------------\      \n"
      "    /              \     \n"
      "   /                \    \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |__________________|   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "                         \n"
      "        ArtSystem        \n")
    print("Starting ArtSystem... /")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /------------\      \n"
      "    /              \     \n"
      "   /                \    \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |__________________|   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "                         \n"
      "        ArtSystem        \n")
    print("Starting ArtSystem... -")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /------------\      \n"
      "    /              \     \n"
      "   /                \    \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |__________________|   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "                         \n"
      "        ArtSystem        \n")
    print("Starting ArtSystem... |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /------------\      \n"
      "    /              \     \n"
      "   /                \    \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |__________________|   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "                         \n"
      "        ArtSystem        \n")
    print("Starting ArtSystem... -")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /------------\      \n"
      "    /              \     \n"
      "   /                \    \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |__________________|   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "                         \n"
      "        ArtSystem        \n")
    print("Starting ArtSystem... \ ")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /------------\      \n"
      "    /              \     \n"
      "   /                \    \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |__________________|   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "                         \n"
      "        ArtSystem        \n")
    print("Starting ArtSystem... |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /----- ------\      \n"
      "    /              \     \n"
      "   /                \    \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |__________________|   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "                         \n"
      "        ArtSystem        \n")
    print("Starting ArtSystem... |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /------------\      \n"
      "    /              \     \n"
      "   /                \    \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |__________________|   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "                         \n"
      "        ArtSystem        \n")
    print("Starting ArtSystem... /")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /------------\      \n"
      "    /              \     \n"
      "   /                \    \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |__________________|   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "                         \n"
      "        ArtSystem        \n")
    print("Starting ArtSystem... -")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /------------\      \n"
      "    /              \     \n"
      "   /                \    \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |__________________|   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "                         \n"
      "        ArtSystem        \n")
    print("Starting ArtSystem... |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /------------\      \n"
      "    /              \     \n"
      "   /                \    \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |__________________|   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "                         \n"
      "        ArtSystem        \n")
    print("Starting ArtSystem... -")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /------------\      \n"
      "    /              \     \n"
      "   /                \    \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |__________________|   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "                         \n"
      "        ArtSystem        \n")
    print("Starting ArtSystem... \ ")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /------------\      \n"
      "    /              \     \n"
      "   /                \    \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |__________________|   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "  |                  |   \n"
      "                         \n"
      "        ArtSystem        \n")
    print("Starting ArtSystem... |")
    time.sleep(1)
    welcome()
    
    
def welcome():
    clear_screen()
    try:
        subprocess.call(('notify-send', 'ArtSystem Startup', 'ArtSystem has sucessfuly Loaded!'))
    except:
        try:
            subprocess.call(('zenity', '--info', '--text="ArtSystem has sucessfuly Loaded!"', '--timeout=5 2'))
            clear_screen()
        except:
            pass
    print("===================\n"
          "+   +ArtSystem+   +\n"
          "===================               {}".format(version))
    print("\n"
          "1. Login    | 2. Register\n"
          "3. Guest    | 4. Refer   \n")
    print("\n"
          "      0. Shutdown          ")
    choice = user_choice()
    if choice == "1":
        login()
    if choice == "2":
        register()
    if choice == "3":
        guesta()
    if choice == "4":
        clear_screen()
        print("Help the community by refering ArtSystem to someone!")
        print("\n\nURL : https://github.com/ArtGames101/ArtSystem")
        input("\nBack")
        welcome()
    if choice == "0":
        wshutdown()

def wshutdown():
    clear_screen()
    print("==========\n"
          " Shutdown \n"
          "==========\n")
    print("1. Shutdown")
    print("2. Restart")
    print("\n"
          "0. Back")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        print("\n"
              "     /------------\      \n"
              "    /              \     \n"
              "   /                \    \n"
              "  |                  |   \n"
              "  |                  |   \n"
              "  |__________________|   \n"
              "  |                  |   \n"
              "  |                  |   \n"
              "  |                  |   \n"
              "\n"
              "        ArtSystem        \n")
        print("Shutdown!")
    if choice == "2":
        subprocess.call((sys.executable, "run.py"))
    if choice == "0":
        welcome()

def guesta():
    clear_screen()
    print("===============\n"
          " Guest Account \n"
          "===============\n")
    print("\n"
          "Are you sure you want to login as a guest?")
    print("1. Yes    | 2. No")
    choice = user_choice()
    if choice == "1":
        guest()
    if choice == "2":
        welcome()
def guest():
    clear_screen()
    loginw = open("user/logindata.py", "w")
    loginpw = open("user/loginpass.py", "w")
    loginw.write("USERNAME = 'Guest'")
    loginpw.write("PASSWORD = 'guestie'")
    loginw.close()
    loginpw.close()
    print("===============\n"
          " Guest Account \n"
          "===============\n")
    input("You Are logging in as a guest get ready for restart!")
    subprocess.call((sys.executable, "run.py"))
    
def login():
    clear_screen()
    print("=========\n"
          "  Login  \n"
          "=========\n")
    if logind.USERNAME == None:
        register()
    else:
        pass
    try:
        if logind.USERNAME == 'Guest':
            print("Guest Passwords are: guestie")
        else:
            pass
    except:
        pass
    try:
        print("\n{}\n".format(logind.USERNAME))
    except:
        register()
    print("\n"
          "Password: \n"
          "")
    try:
        if remind.rem == "None":
            pass
        else:
            try:
                print("\n"
                      "Reminder : {}".format(remind.rem))
            except:
                pass
    except:
        pass
    choice = user_choice()
    if choice == loginp.PASSWORD:
        gold = open("data/gold.py", "w")
        alphapps = open("data/alphapps.py", "w")
        alphapps.write("A = False")
        gold.write("g = False")
        main()
    else:
        login()

def register():
    clear_screen()
    print("==========\n"
          " Register \n"
          "==========\n")
    loginw = open("user/logindata.py", "w")
    print("First Choose a Username!")
    choice = user_choice()
    loginw.write("USERNAME = '{}'".format(choice))
    loginw.close()
    registerp()

def registerp():
    clear_screen()
    print("==========\n"
          " Register \n"
          "==========\n")
    loginpw = open("user/loginpass.py", "w")
    print("Now Choose a password")
    choice = user_choice()
    loginpw.write("PASSWORD = '{}'".format(choice))
    loginpw.close()
    registerl()

def registerl():
    clear_screen()
    print("==========\n"
          " Register \n"
          "==========\n")
    print("\n"
          "Would you like a password reminder msg?")
    print("\n"
          "1. Yes  | 2. No")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        rem = open("user/reminder.py", "w")
        print("==========\n"
              " Register \n"
              "==========\n")
        print("Type Reminder message")
        choice = user_choice()
        rem.write("rem = '{}'".format(choice))
        clear_screen()
        input("Registration Complete!")
        rem.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "2":
        rem = open("user/reminder.py", "w")
        rem.write("rem = 'None'")
        rem.close()
        input("Registration Complete!")
        subprocess.call((sys.executable, "run.py"))
        

def main():
    if c.currentgame == "snake":
        game = "snake"
    if c.currentgame == "Tetris":
        game = "Tetris"
    elif c.currentgame == "BattleSim":
        game = "BattleSim"
    elif c.currentgame == "Santa":
        game = "Santa"
    elif c.currentgame == "squirrel":
        game = "squirrel"
    elif c.currentgame == "GunRush":
        game = "GunRush"
    elif c.currentgame == "DocCreator":
        game = "DocCreator"
    elif c.currentgame == "VF":
        game = "VF"
    else:
        game = "None"
    size = '{:.2f} MiB'.format(__import__('psutil').Process().memory_full_info().uss / 1024 ** 2)
    clear_screen()
    print("========================================================\n"
          "=. {}        |  {}     \n"
          "========================================================\n".format(c.NAMETAG, time.ctime()))

    if game in games:
        print("(o). Disc Game ({})".format(game))
    else:
        print("\a")
    print("c. Changelog")
    print("s. Store")
    print("w. Py Web Browser")
    print("set. Settings")
    if santa == True:
        print("sa. Santa's Gift!")
    else:
        pass
    print("n. Notifications")
    print("\n{}".format(random.choice(ad)))
    print("\n0. Logout")
    choice = user_choice()
    if choice == "(o)":
        if game == "DocCreator":
            subprocess.call((sys.executable, "DocCreator/run.py"))
        if game == "VF":
            subprocess.call((sys.executable, "VirtualFriend-VF/run.py"))
        if game == "snake":
            subprocess.call(("python", "snake.py"))
        if game == "Tetris":
            subprocess.call(("python", "tetris.py"))
        if game == "squirrel":
            subprocess.call(("python", "squirrel.py"))
        if game == "BattleSim":
            subprocess.call((sys.executable, "BattleSim/run.py"))
        if game == "Santa":
            subprocess.call((sys.executable, "SantasLittleHelper/santa.py"))
        if game == "GunRush":
            subprocess.call((sys.executable, "GunRush/run.py"))
    if choice == "s":
        if parent.PAPASS == None:
            store()
        else:
            clear_screen()
            print("Enter Parental Control Password")
            choice = user_choice()
            if choice == parent.PAPASS:
                store()
            else:
                main()
    if choice == "c":
        changelog()
    if choice == "set":
        if parent.PAPASS == None:
            settings()
        else:
            clear_screen()
            print("Enter Parental Control Password")
            choice = user_choice()
            if choice == parent.PAPASS:
                settings()
            else:
                main()
    if choice == "sa":
        if santa == True:
            santagift()
        else:
            main()
    if choice == "n":
        notification()
    if choice == "w":
        subprocess.call((sys.executable, "web/web.py"))
    if choice == "=":
        menu()
    if choice == "0":
        logout()
    else:
        main()

def notification():
    clear_screen()
    print("=====================\n"
          " Newest Notification \n"
          "=====================\n")
    try:
        print(notification.NOT)
    except:
        print("No New Notifications")
    print("\n"
          "1. Clear  | 0. Back")
    choice = user_choice()
    if choice == "1":
        rewrite = open("log/notification.py", "w")
        rewrite.write("NOT = 'None'")
    if choice == "0":
        main()
    else:
        notification()
def settings():
    if logind.USERNAME == "Guest":
        input("Guests cant do that!")
        main()
    else:
        clear_screen()
        print("============\n"
              "  Settings  \n"
              "============\n")
        print("Change Settings here!")
        print("\a")
        print("u. Username")
        print("pass. Password")
        print("p. Parental Control")
        print("\n"
              "a. Advanced Settings\n"
              "r. Restart (Saves Settings)")
        print("0. Back")
        choice = user_choice()
        if choice == "u":
            usernamec()
        if choice == "pass":
            passchange()
        if choice == "p":
            if parent.PAPASS == None:
                parentalcontrol()
            else:
                parentalsettings()
        if choice == "a":
            advancedsettings()
        if choice == "r":
            subprocess.call((sys.executable, "run.py"))
        if choice == "0":
            main()
        else:
            settings()

def advancedsettings():
    clear_screen()
    print("============\n"
          "  Advanced  \n"
          "  Settings  \n"
          "============\n")
    print("n. Change Recent Notification")
    print("u. Upgrade to {}".format(nextup))
    print("\n"
          "Danger Zone!!!:\n"
          "\n")
    print("s. Safe Zone Alpha  (Completely Bug Free Version of ArtSystem easy for little kids)")
    print("d. ****Delete Accoount****  (Deletes Current Account!)")
    print("o. ****Overwrite ArtSystem**** (Fully Destroys the main System!)")
    print("\n"
          "r. Restart (Saves Settings)\n"
          "0. Back")
    choice = user_choice()
    if choice == "n":
        notifichange()
    if choice == "u":
        subprocess.call((sys.executable, "upgrade.py"))
    if choice == "s":
        setupsafezone()
    if choice == "d":
        deleteacc()
    if choice == "o":
        override()
    if choice == "r": 
        subprocess.call((sys.executable, "run.py"))
    if choice == "0":
        settings()
    else:
        advancedsettings()

def setupsafezone():
    clear_screen()
    print("===========\n"
          " Safe Zone \n"
          "   Setup   \n"
          "===========\n")
    print("Information:\n"
          "\n"
          "SafeZone is mostly for children it will soon be\n"
          "loaded with lots of educational apps\n"
          "SafeZone can be undone if wanted to!\n"
          "When you run the default launcher it will send you to SafeZone\n"
          "So you dont have to do this again!\n"
          "\n"
          "WARNING : Safezone may be buggy when reverting back!")
    print("\n"
          "Features:\n"
          "\n"
          "* Take Care of a pet\n"
          "* Educational Games\n"
          "And MORE!")
    print("\n"
          "Would you like to continue?")
    print("\n"
          "y. Yes  | n. No")
    choice = user_choice()
    if choice == "y":
        csafezone()
    if choice == "n":
        advancedsettings()

def csafezone():
    num = ["255", "123", "000", "432", "900", "124"]
    clear_screen()
    print("===========\n"
          " Safe Zone \n"
          "   Setup   \n"
          "===========\n")
    print("Choose Your SafeZone Username")
    choice = user_choice()
    safe = open("user/safezone.py", "w")
    safe.write("NAME = '{}{}'".format(choice, random.choice(num)))
    new = open("safedata/new.py", "w")
    new.write("isn = True")
    input("Push Enter to continue to SafeZone!")
    safe.close()
    new.close()
    subprocess.call((sys.executable, "run.py"))

def deleteacc():
    clear_screen()
    print("=================\n"
          " Delete Account? \n"
          "=================\n")
    print("Are You Sure you want to delete your account?")
    print("\n"
          "y. Yes  | n. No")
    choice = user_choice()
    if choice == "y":
        loginw = open("user/logindata.py", "w")
        loginpw = open("user/loginpass.py", "w")
        loginw.write("USERNAME = ")
        loginpw.write("PASSWORD = ")
        input("Enter to continue")
        loginw.close()
        loginpw.close()
        subprocess.call((sys.executable, "run.py"))
def override():
    if parent.PAPASS == None:
        clear_screen()
        print("====================\n"
              " **** Overwrite **** \n"
              "====================\n")
        print("\n"
              "Are you sure you want to Override ArtSystem this can not be undone?")
        print("\n"
              "y. Yes   | n. No")
        choice = user_choice()
        if choice == "y":
            over = open("run.py", "w")
            over.write("# You Have overwrited ArtSystem\n"
                       "print('Opps! This wont work!')")
            over.close()
            subprocess.call((sys.executable, "run.py"))
        if choice == "n":
            main()
        else:
            override()
    else:
        main()
def parentalsettings():
    clear_screen()
    print("==================\n"
          " Parental Control \n"
          "==================\n")
    print("Parental Control Settings:")
    print("\n"
          "p. Change Parental Password\n"
          "c. Clear Parental Password")
    choice = user_choice()
    if choice == "p":
        parentalcontrol()

    if choice == "c":
        par = open("user/parental.py", "w")
        par.write("PAPASS = None")
        clear_screen()
        input("Restarting...")
        par.close()
        subprocess.call((sys.executable, "run.py"))
def parentalcontrol():
    clear_screen()
    print("==================\n"
          " Parental Control \n"
          "==================\n")
    print("Enter your Account Password!")
    choice = user_choice()
    if choice == loginp.PASSWORD:
        input("Accepted!")
        parentalac()
    else:
        input("Incorrect Password!")
        settings()

def parentalac():
    clear_screen()
    print("==================\n"
          " Parental Control \n"
          "==================\n")
    print("Choose Your parental control password!")
    choice = user_choice()
    if choice == loginp.PASSWORD:
        input("You can not use your account password!")
        settings()
    else:
        par = open("user/parental.py", "w")
        par.write("PAPASS = '{}'".format(choice))
        clear_screen()
        input("Restarting...")
        par.close()
        subprocess.call((sys.executable, "run.py"))
def usernamec():
    clear_screen()
    print("============\n"
          "  Username  \n"
          "============\n")
    loginw = open("user/logindata.py", "w")
    print("\n"
          "New Username :")
    choice = user_choice()
    loginw.write("USERNAME = '{}'".format(choice))
    input("Done!")
    settings()

def passchange():
    clear_screen()
    print("============\n"
          "  Password  \n"
          "============\n")
    print("\n"
          "New Password :")
    loginpw = open("user/loginpass.py", "w")
    choice = user_choice()
    loginpw.write("USERNAME = '{}'".format(choice))
    input("Done!")
    settings()


def santagift():
    clear_screen()
    print("You will need internet for this if you have no internet push enter!")
    print("\n"
          "Merry Christmas!")
    print("\nc. Collect")
    choice = user_choice()
    if choice == "c":
        subprocess.call(("git", "clone", "https://github.com/artsystem101/SantasLittleHelper.git"))
        subprocess.call(("git", "clone", "https://github.com/artsystem101/squirrel.git"))
        subprocess.call(("git", "clone", "https://github.com/artsystem101/snake.git"))
        subprocess.call(("git", "clone", "https://github.com/ArtGames101/BattleSim.git"))
        gold.write("gold = True")
        input("All ArtSystem Games have been installed and also you have recieved Gold!")
        input("Unpack snake and squirrel from their folders!")
        notifi = open("log/notification.py", "w")
        notifi.write("import time\n"
                     "NOT = '{} |  {}'.format(time.ctime(), 'Collected Santa's Gift!')")
        main()
    else:
        main()
        
        
def menu():
    size = '{:.2f} MiB'.format(__import__('psutil').Process().memory_full_info().uss / 1024 ** 2)
    clear_screen()
    print("========\n"
          " Status \n"
          "========\n")
    print("Current Version:\n"
          "{}".format(version))
    print("Games in Store:\n"
          "{}".format(gm))
    print("Apps in Store:\n"
          "{}".format(ap))
    print("Passes in Store:\n"
          "{}".format(pa))
    print("Size of ArtSystem:\n"
          "{}".format(size))
    input("\nBack")
    main()

def logout():
    clear_screen()
    print("==========\n"
          "  Logout  \n"
          "==========\n")
    print("1. Restart")
    print("2. Shutdown")
    print("3. Wait")
    print("4. Logout")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        subprocess.call((sys.executable, "run.py"))
    if choice == "2":
        clear_screen()
        print("\n"
              "     /------------\      \n"
              "    /              \     \n"
              "   /                \    \n"
              "  |                  |   \n"
              "  |                  |   \n"
              "  |__________________|   \n"
              "  |                  |   \n"
              "  |                  |   \n"
              "  |                  |   \n"
              "\n"
              "        ArtSystem        \n")
        print("Shutdown!")
        sys.exit(1)
    if choice == "3":
        wait()
    if choice == "4":
        welcome()
    if choice == "0":
        main()
    else:
        logout()

def wait():
    clear_screen()
    print("========\n"
          "  Wait  \n"
          "========\n")
    print("10. 10 Secs")
    print("20. 20 Secs")
    print("30. 30 Secs")
    print("40. 40 Secs")
    print("50. 50 Secs")
    print("60. 1 Min")
    print("70. 1 Min 10 Secs")
    print("80. 1 Min 20 Secs")
    choice = user_choice()
    if choice == "10":
        time.sleep(10)
        main()
    if choice == "20":
        time.sleep(20)
        main()
    if choice == "30":
        time.sleep(30)
        main()
    if choice == "40":
        time.sleep(40)
        main()
    if choice == "50":
        time.sleep(50)
        main()
    if choice == "60":
        time.sleep(60)
        main()
    if choice == "70":
        time.sleep(70)
        main()
    if choice == "80":
        time.sleep(80)
        main()


def changelog():
    clear_screen()
    print("=================\n"
          "    Changelog    \n"
          "=================\n")
    print("Whats New in {}?".format(version))
    print("\n"
          "* Added Py Web Browser!\n"
          "* Changed Register Data\n"
          "* Changed Login Screen\n"
          "* Fixed Bugs")
    print("\n"
          "<. Last Update   | 0. Back")
    choice = user_choice()
    if choice == "<":
        lastupdate()
    if choice == "0":
        main()

def lastupdate():
    clear_screen()
    print("=================\n"
          "    Changelog    \n"
          "=================\n")
    print("Whats Was in the last update?!?!")
    print("\n"
          "* Added New Game by MrBackPack\n"
          "* Changed Upgrade (Added Options, Now automaticly goes to new version)\n"
          "* Added Featured Games in store\n"
          "* Added Welcome messages (Ubuntu, Raspberry pi, Windows)\n"
          "* Added VirtualFriend to Apps Page")
    input("\nBack")
    changelog()
    
def store():
    if logind.USERNAME == "Guest":
        input("Guests Cant do that!")
        main()
    else:
        clear_screen()
        print("=================\n"
              " ArtSystem Store \n"
              "=================\n")
        print("1. Featured")
        print("2. Games")
        print("3. Apps")
        print("4. Passes")
        print("0. Back")
        choice = user_choice()
        if choice == "1":
            featured()
        if choice == "2":
            storegames()
        if choice == "3":
            apps()
        if choice == "4":
            passes()
        if choice == "0":
            main()

def featured():
    clear_screen()
    print("================\n"
          "    Featured    \n"
          "================\n")
    print("The top 3 games and apps are here!\n\n")
    print("1. BattleSim (ArtGames101)")
    print("2. Snake (Pygame)")
    print("3. GunRush (MrBackPack)")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        storebattlesim()
    if choice == "2":
        storesnake()
    if choice == "3":
        storegunrush()
    if choice == "0":
        store()

def passes():
    clear_screen()
    print("=================\n"
          "     Passes      \n"
          "=================\n")
    print("1. Gold  (ArtSystem)")
    print("2. Alphapps  (ArtSystem)")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        gogold()
    if choice == "2":
        goalphapps
    if choice == "0":
        store()

def apps():
    clear_screen()
    print("=================\n"
          "      Apps       \n"
          "=================\n")
    print("1. Document Creator (ArtGames101)")
    print("2. VirtualFriend VF (ArtGames101)")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        storedoc()
    if choice == "2":
        storevf()
    if choice == "0":
        store()

def storevf():
    clear_screen()
    print("VirtualFriend VF\n"
          "\n"
          "Description:\n"
          "Have Fun with your own Virtual Friend\n"
          "That has lots of features!\n"
          "\n"
          "Publisher:\n"
          "ArtGames101\n")
    print("i. Install")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        subprocess.call(("git", "clone", "https://github.com/ArtGames101/VirtualFriend-VF.git"))
        input("Installed!")
        notifi = open("log/notification.py", "w")
        notifi.write("import time\n"
                     "NOT = '{} |  {}'.format(time.ctime(), 'Installed Game (GunRush)')")
        storetetris()
    if choice == "0":
        storegames()
        
def storedoc():
    clear_screen()
    print("Document Creator\n"
          "\n"
          "Description:\n"
          "Create Documents!\n"
          "\n"
          "Publisher:\n"
          "ArtGames101\n")
    if alpha.A == True:
        try:
            import DocCreator
            print("Installed!")
        except:
            print("i. Install  (With Alphapps Pass!)")
    else:
        print("Get Alphapps to install!")
    choice = user_choice()
    if choice == "i":
        if alpha.A == True:
            subprocess.call(("git", "clone", "https://github.com/artsystem101/DocCreator.git"))
            input("Installed!")
            notifi = open("log/notification.py", "w")
            notifi.write("import time\n"
                         "NOT = '{} |  {}'.format(time.ctime(), 'Installed App (Document Creator)')")
            storedoc()
        else:
            input("Install Alphapps Pass to Get this!")
            storedoc()
    if choice == "0":
        apps()
def storegames():
    clear_screen()
    print("=================\n"
          "      Games      \n"
          "=================\n")
    print("1. Snake  (Pygame)")
    print("2. Battle Sim  (ArtGames101)")
    print("3. Squirrel (Pygame)  (GOLD!)")
    print("4. Santas Little Helper (ArtGames101)  (Christmas Gift!)")
    print("5. Tetris  (ArtGames101)")
    print("6. GunRush (MrBackPack)")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        storesnake()
    if choice == "2":
        storebattlesim()
    if choice == "3":
        storesquirrel()
    if choice == "4":
        slh()
    if choice == "5":
        storetetris()
    if choice == "6":
        storegunrush()
    if choice == "0":
        store()

def storegunrush():
    clear_screen()
    print("GunRush\n"
          "\n"
          "Description:\n"
          "None\n"
          "\n"
          "Publisher:\n"
          "MrBackPack\n")
    try:
        from GunRush import run
        print("\nInstalled!")
    except:
        print("i. Install")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        subprocess.call(("git", "clone", "https://github.com/ArtGames101/GunRush.git"))
        input("Installed!")
        notifi = open("log/notification.py", "w")
        notifi.write("import time\n"
                     "NOT = '{} |  {}'.format(time.ctime(), 'Installed Game (GunRush)')")
        storetetris()
    if choice == "0":
        storegames()
def storetetris():
    clear_screen()
    print("Tetris\n"
          "\n"
          "Description:\n"
          "Stack Blocks and get as many rows as you can!\n"
          "\n"
          "Publisher:\n"
          "ArtGames101\n")
    try:
        import tetris
        print("\nInstalled!")
    except:
        print("i. Install")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        subprocess.call(("git", "clone", "https://github.com/artsystem101/tetris.git"))
        input("Installed!")
        input("To Unpack tetris game move tetris.py & the mid files from the tetris folder!")
        notifi = open("log/notification.py", "w")
        notifi.write("import time\n"
                     "NOT = '{} |  {}'.format(time.ctime(), 'Installed Game (Tetris)')")
        storetetris()
    if choice == "0":
        storegames()

def slh():
    clear_screen()
    print("Santa's Little Helper\n"
          "\n"
          "Description:\n"
          "Help Santa Deliver Presents to Children\n"
          "\n"
          "Publisher:\n"
          "ArtGames101\n")
    if santa == True:
        try:
            import SantasLittleHelper
            print("Installed!")
        except:
            print("i. Install  (For Christmas)")
    else:
        print("Install on Christmas Updates!")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        if santa == True:
            subprocess.call(("git", "clone", "https://github.com/artsystem101/SantasLittleHelper.git"))
            input("Installed!")
            input("Merry Christmas (Your game does not need unpacking!)")
            notifi = open("log/notification.py", "w")
            notifi.write("import time\n"
                         "NOT = '{} |  {}'.format(time.ctime(), 'Installed Exclusive Game (Santas little helper!)')")
            slh()
        else:
            slh()
    if choice == "0":
        storegames()

def storesquirrel():
    clear_screen()
    print("Squirrel\n"
          "\n"
          "Description:\n"
          "Kill Smaller Squirrels to become the OMEGA SQUIRREL\n"
          "\n"
          "Publisher:\n"
          "Pygame\n")
    if g.gold == True:
        try:
            import squirrel
            print("Installed!")
        except:
            print("i. Install  (With Gold Pass!)")
    else:
        print("Go Gold to install!")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        if g.gold == True:
            subprocess.call(("git", "clone", "https://github.com/artsystem101/squirrel.git"))
            input("Installed!")
            input("To Unpack squirrel game move squirrel.py and squirrel.png from the squirrel folder!")
            notifi = open("log/notification.py", "w")
            notifi.write("import time\n"
                         "NOT = '{} |  {}'.format(time.ctime(), 'Installed Gold Game (Squirrel)')")
            storesquirrel()
        else:
            storesquirrel()
    if choice == "0":
        storegames()

def storesnake():
    clear_screen()
    print("Snake\n"
          "\n"
          "Description:\n"
          "Eat as many apples as you can without loosing!\n"
          "\n"
          "Publisher:\n"
          "Pygame\n")
    try:
        import snake
        print("\nInstalled!")
    except:
        print("i. Install")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        subprocess.call(("git", "clone", "https://github.com/artsystem101/snake.git"))
        input("Installed!")
        input("To Unpack snake game move snake.py from the snake folder!")
        notifi = open("log/notification.py", "w")
        notifi.write("import time\n"
                     "NOT = '{} |  {}'.format(time.ctime(), 'Installed Game (Snake)')")
        storesnake()
    if choice == "0":
        storegames()

def storebattlesim():
    clear_screen()
    print("Battle Sim\n"
          "\n"
          "Description:\n"
          "Battle Enemies & unlock characters!\n"
          "\n"
          "Publisher:\n"
          "ArtGames101\n")
    try:
        from BattleSim import run
        print("\nInstalled!")
    except:
        print("i. Install")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        subprocess.call(("git", "clone", "https://github.com/ArtGames101/BattleSim.git"))
        input("Installed!")
        input("Your Game Doesnt Need unpacking!")
        notifi = open("log/notification.py", "w")
        notifi.write("import time\n"
                     "NOT = '{} |  {}'.format(time.ctime(), 'Installed Game (Battle Sim)')")
        storebattlesim()
    if choice == "0":
        storegames()


def gogold():
    clear_screen()
    print("*Gold Game Pass*\n"
          "\n"
          "Description:\n"
          "Get Special Access to store games that have not been released!\n"
          "\n"
          "Publisher:\n"
          "ArtSystem\n")
    if g.gold == True:
        print("\nActive!")
    else:
        print("\ni. Go Gold!")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        gold.write("gold = True")
        input("Gold Pass Updated!")
        gogold
    if choice == "0":
        passes()

def goalphapps():
    clear_screen()
    print("*Alphapps*\n"
          "\n"
          "Description:\n"
          "Get Special Access to Apps!!!!\n"
          "\n"
          "Publisher:\n"
          "ArtSystem\n")
    if alpha.A == True:
        print("\nActive!")
    else:
        print("\ni. Get Alphapps")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        gold.write("A = True")
        input("Alphapps Pass Updated!")
        goalphapps
    if choice == "0":
        passes()


if upg.stay == True:
    if safezone.NAME == None:
        loading()
    else:
        subprocess.call((sys.executable, "safe.py"))  
else:
    subprocess.call((sys.executable, "ArtSystem/run.py"))
