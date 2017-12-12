# (c) ArtGames101 2017
# This System was created by ArtGames101 and is under copyright notice!
import sys, os, random, time, subprocess
import config as c
error = open("log/lasterror.txt", "w")

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
    games = ["snake", "BattleSim"]
    if c.currentgame == "snake":
        game = "snake"
    elif c.currentgame == "BattleSim":
        game = "BattleSim"
    else:
        game = "None"
    clear_screen()
    print("===========================\n"
          "{}        |  ArtSystem     \n"
          "===========================\n".format(c.NAMETAG))
    if game in games:
        print("(o). Disc Game ({})".format(game))
    else:
        print("\a")
    print("g. Installed")
    print("s. Store")
    print("\n0. Shutdown")
    choice = user_choice()
    if choice == "(o)":
        if game == "snake":
            subprocess.call(("python", "snake.py"))
        if game == "BattleSim":
            subprocess.call((sys.executable, "BattleSim/run.py"))
    if choice == "g":
        installed()
    if choice == "s":
        store()
    if choice == "0":
        shutdown()
    else:
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
        sys.exit()
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
    print("If you have installed BattleSim we can not show it!")
    input("\nBack")
    main()
def store():
    clear_screen()
    print("=================\n"
          " ArtSystem Store \n"
          "=================\n")
    print("1. Games")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        storegames()
    if choice == "0":
        main()

def storegames():
    clear_screen()
    print("=================\n"
          "      Games      \n"
          "=================\n")
    print("1. Snake  (Pygame)")
    print("2. Battle Sim  (ArtGames101)")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        storesnake()
    if choice == "2":
        storebattlesim()
    if choice == "0":
        store()

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

if c.autoloadgames == True:
    if currentgame == "snake":
        subprocess.call(("python", "snake.py"))
    if currentgame == "BattleSim":
        subprocess.call((sys.executable, "BattleSim/run.py"))
    else:
        loading()
else:
    loading()
