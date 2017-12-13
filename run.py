# (c) ArtGames101 2017
# This System was created by ArtGames101 and is under copyright notice!
import sys, os, random, time, subprocess, psutil
import config as c
from data import gold as g
error = open("log/lasterror.txt", "w")
gold = open("data/gold.py", "w")
games = ["snake", "BattleSim", "squirrel"]
gm = 3
ad = ["Go Gold and get ALPHA games that are comming soon!", "Squirrel (GO GOLD!) (Eat other squirrels to become the OMEGA SQUIRREL)", "Snake (a game where you have to eat apples!)", "BattleSim (The best battle simulator for python!)"]
try:
    import snake
except Exception as e:
    exc = '{}: {}'.format(type(e).__name__, e)
    error.write(exc)
try:
    from BattleSim import run as battle
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
    main()

def main():
    if c.currentgame == "snake":
        game = "snake"
    elif c.currentgame == "BattleSim":
        game = "BattleSim"
    elif c.currentgame == "squirrel":
        game = "squirrel"
    else:
        game = "None"
    clear_screen()
    print("==============================\n"
          "=. {}        |  ArtSystem     \n"
          "==============================\n".format(c.NAMETAG))
    if game in games:
        print("(o). Disc Game ({})".format(game))
    else:
        print("\a")
    print("g. Installed")
    print("s. Store")
    print("\n{}".format(random.choice(ad)))
    print("\n0. Shutdown")
    choice = user_choice()
    if choice == "(o)":
        if game == "snake":
            subprocess.call(("python", "snake.py"))
        if game == "squirrel":
            subprocess.call(("python", "squirrel.py"))
        if game == "BattleSim":
            subprocess.call((sys.executable, "BattleSim/run.py"))
    if choice == "g":
        installed()
    if choice == "s":
        store()
    if choice == "=":
        menu()
    if choice == "0":
        shutdown()
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
    print("Size of ArtSystem:\n"
          "{}".format(size))
    input("\nBack")
    main()
def shutdown():
    clear_screen()
    print("==========\n"
          " Shutdown \n"
          "==========\n")
    print("1. Restart")
    print("2. Shutdown")
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
    if choice == "0":
        main()
def installed():
    clear_screen()
    print("=================\n"
          " Installed Games \n"
          "=================\n")
    try:
        import snake
        print("\nSnake")
    except:
        print("\a")
    try:
        import squirrel
        print("\nSquirrel")
    except:
        print("\a")
    print("If you have installed BattleSim we can not show it!")
    input("\nBack")
    main()
def store():
    clear_screen()
    print("=================\n"
          " ArtSystem Store \n"
          "=================\n")
    print("1. Games")
    print("2. Passes")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        storegames()
    if choice == "2":
        passes()
    if choice == "0":
        main()

def passes():
    clear_screen()
    print("=================\n"
          "     Passes      \n"
          "=================\n")
    print("1. Gold")
    choice = user_choice()
    if choice == "1":
        gogold()
def storegames():
    clear_screen()
    print("=================\n"
          "      Games      \n"
          "=================\n")
    print("1. Snake  (Pygame)")
    print("2. Battle Sim  (ArtGames101)")
    print("3. Squirrel (Pygame)")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        storesnake()
    if choice == "2":
        storebattlesim()
    if choice == "3":
        storesquirrel()
    if choice == "0":
        store()

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
            print("i. Install  (With Gold Pass!")
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


if c.autoloadgames == True:
    if currentgame == "snake":
        subprocess.call(("python", "snake.py"))
    if currentgame == "BattleSim":
        subprocess.call((sys.executable, "BattleSim/run.py"))
    if currentgame == "squirrel":
        subprocess.call(("python", "squirrel.py"))
    else:
        loading()
else:
    loading()
