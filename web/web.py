import subprocess, sys, os, time, webbrowser


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
    print("===================\n"
          "     Py Browser    \n"
          "===================       {}".format(time.ctime()))
    print("\n"
          "Enter a URL!")
    print("\n"
          "0. Exit")
    url = user_choice()
    if url == "0":
        sys.exit()
    else:
        try:
            webbrowser.open(url)
            main()
        except:
            input("Unable to open this URL!")
            main()


main()
