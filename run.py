# (c) ArtGames101 2017 - 2018
# This Console was created by ArtGames101 and is under copyright notice!

# 

import sys, os, random, time, subprocess
import urllib
import config as c
from data import gold as g
from data import alphapps as alpha
from data import anew
from log import notification
from user import safezone
from data import upgradestay as upg
try:
    from user import logindata as logind
    from user import loginpass as loginp
    from user import parental as parent
    from user import reminder as remind
    from user import img
except:
    pass

# Version
vr = "10.9"
version = "v{}-Stable".format(vr)
# Next Version
nextup = "v11.0-Stable"

error = open("log/lasterror.txt", "w")
start = open("log/startlog.txt", "w")
try:
    webb = open("web/name.py", "w")
    webb.write("name = '{}'".format(logind.USERNAME))
except:
    pass
webb.close()
santa = False
games = ["snake", "BattleSim", "squirrel", "Santa", "Tetris", "GunRush", "DocCreator", "VF"]
apps = ["DocCreator", "VF", "WebBrowser"]
gm = 6
ap = 3
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


def new():
    clear_screen()
    try:
       subprocess.call(('notify-send', 'ArtSystem Verification', 'Please enter your 6 digit code!'))
    except:
        pass
    print("(A) ArtSystem {}\n"
          "==========================".format(vr))
    print("\n"
          "Please enter your 6 digit verification code\n"
          "to continue!")
    print("\n"
          "?: Get it from the ArtSystem Github")
    choice = user_choice()
    if choice == "pa64ap":
        confirm = open("data/anew.py", "w")
        confirm.write("new = False")
        input("Verification code accepted!")
        confirm.close()
        neww()
    else:
        input("Invalid Verification Code!")
        new()

def neww():
    clear_screen()
    print("(A) ArtSystem {}\n"
          "==========================".format(vr))
    print("\n"
          "Welcome to ArtSystem!\n"
          "\n"
          "Here is what your ArtSystem can do!\n"
          "\n"
          "* Plays Games\n"
          "* Manages Accounts\n"
          "* Browses the web\n"
          " And More!")
    input("\n"
          "Enter")
    clear_screen()
    print("(A) ArtSystem {}\n"
          "==========================".format(vr))
    print("\n"
          "Your ArtSystem Comes with Restore Options and Web Protection!\n"
          "\n"
          "Push Enter to Start ArtSystem!\n")
    input(".")
    loading()


def loading():
    clear_screen()
    if IS_WINDOWS:
        try:
            os.system("welcome.vbs")
        except:
            pass
    else:
        try:
            subprocess.call(('notify-send', 'ArtSystem Startup', 'ArtSystem Vortex is starting up...'))
        except:
            try:
                subprocess.call(('zenity', '--info', '--text="ArtSystem is starting up!"', '--timeout=5 2'))
                clear_screen()
            except:
                pass
    print("\n"
      "     / -----------\      \n"
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
    print("            |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /- ----------\      \n"
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
    print("            /")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /-- ---------\      \n"
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
    print("            -")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /--- --------\      \n"
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
    print("            |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /---- -------\      \n"
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
    print("            -")
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
    print("            \ ")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /------ -----\      \n"
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
    print("            |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /------- ----\      \n"
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
    print("            |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /-------- ---\      \n"
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
    print("            /")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /--------- --\      \n"
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
    print("            -")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /---------- -\      \n"
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
    print("            |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     /----------- \      \n"
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
    print("            -")
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
    print("            \ ")
    time.sleep(1)
    welcome()
    
    
def welcome():
    clear_screen()
    try:
        from user import logindata
        from user import img
        from user import loginpass
        print(logindata.USERNAME)
        print(img.usrimg)
        print(loginpass.PASSWORD)
        clear_screen()
    except:
        clear_screen()
        print("============\n"
              " File Error \n"
              "============\n")
        print("Your Login files have stoped working or you are not registered!!!\n"
              "What do you want to do?")
        print("\n"
              "1. Register (Will Write Fresh data)\n"
              "2. Guest Account  (Use Guest account for now!)\n"
              "3. Restore  (Restore 'LAST' Save data)")
        choice = user_choice()
        if choice == "1":
            register()
        if choice == "2":
            guestmain()
        if choice == "3":
            restore()
    try:
        subprocess.call(('notify-send', 'ArtSystem Startup', 'ArtSystem has sucessfuly Loaded!'))
    except:
        try:
            subprocess.call(('zenity', '--info', '--text="ArtSystem Vortex has sucessfuly Loaded!"', '--timeout=5 2'))
            clear_screen()
        except:
            pass
        if img.usrimg == None:
            print("_________\n"
                  "         |\n"
                  "         | 1. [?] {}\n"
                  "         |\n"
                  "         | 2. [G] Guest\n"
                  " Welcome |\n"
                  "         |\n"
                  "         | r. Register\n"
                  "         | 0. More Options\n"
                  "_________|\n".format(logind.USERNAME))
            choice = user_choice()
            if choice == "1":
                login()
            if choice == "2":
                guesta()
            if choice == "r":
                register()
            if choice == "0":
                try:
                    mainmore()
                except:
                    pass
            else:
                welcome()
        else:
            print("_________\n"
                  "         |\n"
                  "         | 1. [{}] {}\n"
                  "         |\n"
                  "         | 2. [G] Guest\n"
                  " Welcome |\n"
                  "         |\n"
                  "         | r. Register\n"
                  "         | 0. More Options\n"
                  "_________|\n".format(img.usrimg, logind.USERNAME))
            choice = user_choice()
            if choice == "1":
                login()
            if choice == "2":
                guesta()
            if choice == "r":
                register()
            if choice == "0":
                try:
                    mainmore()
                except:
                    pass
            else:
                welcome()
def mainmore():
    clear_screen()
    print("==============\n"
          " More Options \n"
          "==============\n")
    print("\n"
          "1. Refer\n"
          "2. Restore\n"
          "3. Shutdown Options\n"
          "\n"
           "0. Back")
    choice = user_choice()
    if choice == "1":
        refer()
    if choice == "2":
        restore()
    if choice == "3":
        wshutdown()
    if choice == "0":
        welcome()


def refer():
    clear_screen()
    print("=================\n"
          " Refer ArtSystem \n"
          "=================\n")
    print("\n"
          "Github : https://github.com/ArtGames101/ArtSystem\n"
          "\n"
          "Install cmd : git clone https://github.com/ArtGames101/ArtSystem.git")
    input("\n"
          "Back")
    mainmore()

def restore():
    clear_screen()
    try:
        from data.restore import name, passw
    except:
        input("No Data to restore!")
        mainmore()
    print("=========\n"
          " Restore \n"
          "=========\n")
    print("ArtSystem is restoring your old data!")
    usr = open("user/logindata.py", "w")
    usr.write("USERNAME = '{}'".format(name.old))
    pa = open("user/loginpass.py", "w")
    pa.write("PASSWORD = '{}'".format(passw.old))
    input("ArtSystem Restored!")
    subprocess.call((sys.executable, "run.py"))
    
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
        guestmain()
    if choice == "2":
        welcome()

    
def login():
    clear_screen()
    print("=========\n"
          " Welcome \n"
          "=========\n")
    try:
        print("{}".format(logind.USERNAME))
    except:
        input("No User found!")
        register()
    print("\n{}".format(remind.rem))
    print("\n"
          "Password\n"
          "\n"
          "_____________")
    choice = user_choice()
    if choice == loginp.PASSWORD:
        main()
    else:
        loginf()

def loginf():
    clear_screen()
    print("=========\n"
          " Welcome \n"
          "=========\n")
    try:
        print("{}".format(logind.USERNAME))
    except:
        input("No User found!")
        register()
    print("\n{}".format(remind.rem))
    print("\n"
          "Password\n"
          "\n"
          "_____________")
    print("\n"
          "Incorrect Password!")
    choice = user_choice()
    if choice == loginp.PASSWORD:
        main()
    else:
        loginf()
        
def register():
    clear_screen()
    print("==========\n"
          " Register \n"
          "==========\n")
    print("1 Username  2 Password 3 Reminder 4 Avatar\n"
          "----------")
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
    print("✓ Username  2 Password 3 Reminder 4 Avatar\n"
          "----------------------")
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
    print("✓ Username  ✓ Password 3 Reminder 4 Avatar\n"
          "---------------------------------")
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
        print("✓ Username  ✓ Password 3 Reminder 4 Avatar\n"
              "---------------------------------")
        print("Type Reminder message")
        choice = user_choice()
        rem.write("rem = '{}'".format(choice))
        rem.close()
        registeri()
    if choice == "2":
        rem = open("user/reminder.py", "w")
        rem.write("rem = 'None'")
        rem.close()
        registeri()

def registeri():
    img = open("user/img.py", "w")
    clear_screen()
    print("==========\n"
          " Register \n"
          "==========\n")
    print("✓ Username  ✓ Password ✓ Reminder 4 Avatar\n"
          "------------------------------------------")
    print("\n"
          "Pick an avatar!")
    print("\n"
          "1. :D\n"
          "2. ^.^\n"
          "3. ?!\n"
          "4. :)\n"
          "5. :4)\n"
          "c. Custom")
    choice = user_choice()
    usr = open("data/restore/name.py", "w")
    usr.write("old = '{}'".format(logind.USERNAME))
    pas = open("data/restore/passw.py", "w")
    pas.write("old = '{}'".format(loginp.PASSWORD))
    usr.close()
    pas.close()
    if choice == "1":
        img.write("usrimg = ':D'")
        input("Registration Complete!\n"
              "\n"
              "Enter")
        img.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "2":
        img.write("usrimg = '^.^'")
        input("Registration Complete!\n"
              "\n"
              "Enter")
        img.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "3":
        img.write("usrimg = '?!'")
        input("Registration Complete!\n"
              "\n"
              "Enter")
        img.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "4":
        img.write("usrimg = ':)'")
        input("Registration Complete!\n"
              "\n"
              "Enter")
        img.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "5":
        img.write("usrimg = ':4)'")
        input("Registration Complete!\n"
              "\n"
              "Enter")
        img.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "c":
        clear_screen()
        print("Write an Avatar\n"
              "Recomended : Use 3 characters at most!")
        choice = user_choice()
        img.write("usrimg = '{}'".format(choice))
        input("Registration Complete!\n"
              "\n"
              "Enter")
        img.close()
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
    clear_screen()
    print("========================================================\n"
          " {}        |  {}     \n"
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
    print("\n\n\n"
          " ____________________________________________________________________\n"
          "|(A). Start |                                   u. Upgrade           |\n"
          "|___________|________________________________________________________|")
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
    if choice == "(A)":
        menu()
    if choice == "A":
        menu()
    if choice == "a":
        menu()
    if choice == "u":
        subprocess.call((sys.executable, "upgrade.py"))
    if choice == "0":
        logout()
    else:
        main()

def guestmain():
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
    clear_screen()
    print("========================================================\n"
          "=. Guest        |  {}     \n"
          "========================================================\n".format(time.ctime()))

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
                guestmain()
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
                guestmain()
    if choice == "sa":
        if santa == True:
            santagift()
        else:
            guestmain()
    if choice == "n":
        notification()
    if choice == "w":
        subprocess.call((sys.executable, "web/web.py"))
    if choice == "=":
        guestmenu()
    if choice == "0":
        guestlogout()
    else:
        guestmain()


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
        guestmain()
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
    clear_screen()
    print("=======\n"
          " Start \n"
          "=======\n")
    print("1. Loop Game")
    print("2. Shutdown Options")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        loop()
    if choice == "2":
        logout()
    if choice == "0":
        main()

def loop():
    r = ["Ha", "LOOOOOOOOOOOOOOOOOLP", "Restart to exit!", "lololodloefokog", "fuywefuwegfuyehf", "My name is Jeff", "idk"]
    input("{} | Push Enter".format(random.choice(r)))
    loop()
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

def guestlogout():
    clear_screen()
    print("==========\n"
          "  Logout  \n"
          "==========\n")
    print("1. Restart")
    print("2. Shutdown")
    print("3. Logout")
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
        welcome()
    if choice == "0":
        guestmain()
    else:
        guestlogout()

        
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
          "* Added New Main Screen\n"
          "* Added New Login Screen\n"
          "* Added Restore Option\n"
          "* Added New registation options\n"
          "* Added Avatars\n"
          "* Added Login File Errors (You can now restore them when they\n"
          "  are not working!)\n"
          "* Squashed Heaps of bugs\n"
          "* Guests now get their own Seperate Console!\n"
          "* Added Start Menu (May be removed!)")
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
          "* Added Py Web Browser!\n"
          "* Changed Register Data\n"
          "* Changed Login Screen\n"
          "* Fixed Bugs")
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
    print("1. Py Web Browser   (ArtGames101)")
    print("2. Document Creator (ArtGames101)")
    print("3. VirtualFriend VF (ArtGames101)")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        storeweb()
    if choice == "2":
        storedoc()
    if choice == "3":
        storevf()
    if choice == "0":
        store()

def storeweb():
    clear_screen()
    print("Py Web Browser\n"
          "\n"
          "Description:\n"
          "Search the web!\n"
          "\n"
          "Publisher:\n"
          "ArtGames101\n")
    print("Installed!")
    print("0. Back")
    choice = user_choice()
    if choice == "0":
        storegames()

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
    if anew.new == True:
        new()
    else:
        if safezone.NAME == None:
            loading()
        else:
            subprocess.call((sys.executable, "safe.py"))  
else:
    subprocess.call((sys.executable, "ArtSystem/run.py"))
