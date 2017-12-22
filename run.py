# (c) ArtGames101 2017
# This Console was created by ArtGames101 and is under copyright notice!

import sys, os, random, time, subprocess, psutil
import config as c
from data import gold as g
try:
    from user import logindata as logind
    from user import loginpass as loginp
    from user import parental as parent
except:
    pass

error = open("log/lasterror.txt", "w")
start = open("log/startlog.txt", "w")
gold = open("data/gold.py", "w")
santa = True
games = ["snake", "BattleSim", "squirrel", "Santa", "Tetris"]
apps = ["DocCreator"]
gm = 5
ap = 1
pa = 1
ad = ["Go Gold and get ALPHA games that are comming soon!", "Squirrel (GO GOLD!) (Eat other squirrels to become the OMEGA SQUIRREL)", "Snake (a game where you have to eat apples!)", "BattleSim (The best battle simulator for python!)", "Tetris  (A Game where you have to stack blocks!)", "Merry Christmas!"]
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
    print("Getting Ready...")
    time.sleep(5)
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
    time.sleep(5)
    welcome()

def welcome():
    clear_screen()
    print("=================\n"
          "+   +Welcome+   +\n"
          "=================\n")
    print("\n"
          "1. Login    | 2. Register\n"
          "3. Guest    | 4. Refer   \n")
    choice = user_choice()
    if choice == "1":
        login()
    if choice == "2":
        register()
    if choice == "3":
        guest()
    if choice == "4":
        clear_screen()
        print("Help the community by refering ArtSystem to someone!")
        print("\n\nURL : https://github.com/ArtGames101/ArtSystem")
        input("\nBack")
        welcome()

def guest():
    clear_screen()
    loginw = open("user/logindata.py", "w")
    loginpw = open("user/loginpass.py", "w")
    loginw.write("USERNAME = 'Guest'")
    loginpw.write("PASS = 'guestie'")
    loginw.close()
    loginpw.close()
    input("You Are logging in as a guest get ready for restart!")
    subprocess.call((sys.executable, "run.py"))
    
def login():
    clear_screen()
    print("=========\n"
          "  Login  \n"
          "=========\n")
    try:
        if logind.USERNAME == 'Guest':
            print("Guest Passwords are: guestie")
        else:
            pass
    except:
        pass
    try:
        print("{}\n".format(logind.USERNAME))
    except:
        register()
    print("\n"
          "Password: \n"
          "")
    choice = user_choice()
    if choice == loginp.PASSWORD:
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
    clear_screen()
    print("Writing....")
    time.sleep(5)
    clear_screen()
    input("Get Ready for restart!")
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
    else:
        game = "None"
    size = '{:.2f} MiB'.format(__import__('psutil').Process().memory_full_info().uss / 1024 ** 2)
    start.write("Name : {}\n"
                "\n"
                "CGame : {}\n"
                "\n"
                "Size : {}".format(c.NAMETAG, game, size))
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
    print("set. Settings")
    if santa == True:
        print("sa. Santa's Gift!")
    else:
        pass
    print("\n{}".format(random.choice(ad)))
    print("\n0. Logout")
    choice = user_choice()
    if choice == "(o)":
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
    if choice == "=":
        menu()
    if choice == "0":
        logout()
    else:
        main()

def settings():
    clear_screen()
    print("============\n"
          "  Settings  \n"
          "    BETA    \n"
          "============\n")
    print("Change Settings here!")
    print("\a")
    print("u. Username")
    print("pass. Password")
    print("p. Parental Control")
    print("\n"
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
    if choice == "r":
        subprocess.call((sys.executable, "run.py"))
    if choice == "0":
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
        main()
    else:
        main()
        
        
def menu():
    size = '{:.2f} MiB'.format(__import__('psutil').Process().memory_full_info().uss / 1024 ** 2)
    clear_screen()
    print("========\n"
          " Status \n"
          "========\n")
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
        sys.exit(1)
    if choice == "3":
        wait()
    if choice == "4":
        welcome()
    if choice == "0":
        main()

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


def changelog():
    clear_screen()
    print("=================\n"
          "    Changelog    \n"
          "=================\n")
    print("Whats New?")
    print("\n"
          "* Added Parental Controls!\n"
          "* Added Apps Page\n"
          "")
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
    print("Whats New?")
    print("\n"
          "* Added Changelog\n"
          "* Removed Installed Page (Wasn't Functional!)\n"
          "* Added Tetris Game to Store")
    input("\nBack")
    changelog()
    
def store():
    clear_screen()
    print("=================\n"
          " ArtSystem Store \n"
          "=================\n")
    print("1. Games")
    print("2. Apps")
    print("3. Passes")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        storegames()
    if choice == "2":
        apps()
    if choice == "3":
        passes()
    if choice == "0":
        main()

def passes():
    clear_screen()
    print("=================\n"
          "     Passes      \n"
          "=================\n")
    print("1. Gold")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        gogold()
    if choice == "0":
        store()

def apps():
    clear_screen()
    print("=================\n"
          "      Apps       \n"
          "=================\n")
    print("1. Document Creator (ArtGames101)")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        storedoc()
    if choice == "0":
        store()

def storedoc():
    clear_screen()
    print("Document Creator\n"
          "\n"
          "Description:\n"
          "Create Documents!\n"
          "\n"
          "Publisher:\n"
          "ArtGames101\n")
    try:
        import DocCreator
        print("\nInstalled!")
    except:
        print("i. Install")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        subprocess.call(("git", "clone", "https://github.com/artsystem101/DocCreator.git"))
        input("Installed!")
        storerdoc()
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
    if choice == "0":
        store()

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
          "ArtGames101\n")
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

loading()
