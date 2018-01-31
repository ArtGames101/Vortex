import subprocess, sys, os, time, webbrowser
import name

# Website open : webbrowser.open(URL)

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()


def main():
    clear_screen()
    print("Welcome {}".format(name.name))
    print("\n"
          "1. Search | 2. Suggested Sites")
    print("       0. Exit                ")
    choice = user_choice()
    if choice == "1":
        search()
    if choice == "2":
        suggested()
    if choice == "0":
        sys.exit(1)


def search():
    clear_screen()
    print("Welcome {}".format(name.name))
    print("\n"
          "Enter URL Below")
    choice = user_choice()
    webbrowser.open(choice)
    main()

def suggested():
    clear_screen()
    print("Welcome {}".format(name.name))
    print("\n"
          "Suggested Sites:\n"
          "\n"
          "1. https://google.com.au\n"
          "2. https://youtube.com\n"
          "3. https://github.com\n"
          "4. https://github.com/ArtSystemStudios/Vortex\n"
          "5. https://github.com/ArtGames101\n"
          "\n"
          "0. Back")
    choice = user_choice()
    if choice == "1":
        webbrowser.open("https://google.com.au")
    if choice == "2":
        webbrowser.open("https://youtube.com")
    if choice == "3":
        webbrowser.open("https://github.com")
    if choice == "4":
        webbrowser.open("https://github.com/ArtSystem/Vortex")
    if choice == "5":
        webbrowser.open("https://github.com/ArtGames101")
    if choice == "0":
        main()
    else:
        main()
main()
