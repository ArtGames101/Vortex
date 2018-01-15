import subprocess, sys, os, time, webbrowser
import name

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
          "Suggested Websites:\n"
          "1. Google.com\n"
          "2. Github.com\n"
          "0. Exit")
    print("\n"
          "Enter URL")
    url = user_choice()
    if url == "1":
        webbrowser.open("https://google.com")
    if url == "2":
        webbrowser.open("https://github.com")
    if url == "0":
        sys.exit(1)
    else:
        try:
            webbrowser.open(url)
            main()
        except:
            input("Unable to open this URL!")
            main()


main()
