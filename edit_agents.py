import json
from colorama import Fore, Back, Style
import os
from os import system
import sys



def main():
    system("title " + "InstaLock")
    with open('json/agents.json', 'r') as f:
        all_agents = json.load(f)
    try:
        print(Fore.RED + " Please enter the agents you want for each map" + Fore.WHITE)
        dash = '-'
        print(" " + Fore.WHITE+ dash*46)
        while True:
            ascent = input(Fore.BLUE +" Ascent: " + Fore.WHITE)
            bind = input(Fore.GREEN + " Bind: " + Fore.WHITE)
            breeze = input(Fore.YELLOW + " Breeze: " + Fore.WHITE)
            fracture = input(Fore.CYAN + " Fracture: " + Fore.WHITE)
            haven = input(Fore.LIGHTMAGENTA_EX + " Haven: " + Fore.WHITE)
            icebox = input(Fore.LIGHTGREEN_EX + " Icebox: " + Fore.WHITE)
            pearl = input(Fore.LIGHTCYAN_EX + " Pearl: " + Fore.WHITE)
            ascent = ascent.lower()
            bind = bind.lower()
            breeze = breeze.lower()
            fracture = fracture.lower()
            haven = haven.lower()
            icebox = icebox.lower()
            pearl = pearl.lower()
            if ascent == "":
                print("")
                print(Fore.RED + "You cannot leave any fields blank." + Fore.WHITE)
                sys.exit()
            if ascent != '' and ascent not in all_agents['all_agents']:
                print("")
                print(Fore.RED + f"{ascent} is not a valid agent." + Fore.WHITE)
                sys.exit()
            if bind == "":
                print("")
                print(Fore.RED + "You cannot leave any fields blank." + Fore.WHITE)
                sys.exit()
            if bind != '' and bind not in all_agents['all_agents']:
                print("")
                print(Fore.RED + f"{bind} is not a valid agent." + Fore.WHITE)
                sys.exit()
            if breeze == "":
                print("")
                print(Fore.RED + "You cannot leave any fields blank." + Fore.WHITE)
                sys.exit()
            if breeze != '' and breeze not in all_agents['all_agents']:
                print("")
                print(Fore.RED + f"{breeze} is not a valid agent." + Fore.WHITE)
                sys.exit()
            if fracture == "":
                print("")
                print(Fore.RED + "You cannot leave any fields blank." + Fore.WHITE)
                sys.exit()
            if fracture != '' and fracture not in all_agents['all_agents']:
                print("")
                print(Fore.RED + f"{fracture} is not a valid agent." + Fore.WHITE)
                sys.exit()
            if haven == "":
                print("")
                print(Fore.RED + "You cannot leave any fields blank." + Fore.WHITE)
                sys.exit()
            if haven != '' and haven not in all_agents['all_agents']:
                print("")
                print(Fore.RED + f"{haven} is not a valid agent." + Fore.WHITE)
                sys.exit()
            if icebox == "":
                print("")
                print(Fore.RED + "You cannot leave any fields blank." + Fore.WHITE)
                sys.exit()
            if icebox != '' and icebox not in all_agents['all_agents']:
                print("")
                print(Fore.RED + f"{icebox} is not a valid agent." + Fore.WHITE)
                sys.exit()
            if pearl == "":
                print("")
                print(Fore.RED + "You cannot leave any fields blank." + Fore.WHITE)
                sys.exit()
            if pearl != '' and pearl not in all_agents['all_agents']:
                print("")
                print(Fore.RED + f"{pearl} is not a valid agent." + Fore.WHITE)
                sys.exit()
            break
        print("")
        ask = input("Are you sure you want to save these agents? ")

        dictionary = {
            "maps": {
                "ascent": ascent,
                "bind": bind,
                "breeze": breeze,
                "fracture": fracture,
                "haven": haven,
                "icebox": icebox,
                "pearl": pearl
            }
        }


        json_object = json.dumps(dictionary, indent=4)

        if ask.lower() == "yes" or ask.lower() == "y":
            with open("json/maps.json", "w") as outfile:
                outfile.write(json_object)
            print("Saved!")
            sys.exit()
        elif ask.lower() == "no" or ask.lower() == "n":
            print("Not saved!")
            sys.exit()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    os.system('cls')
    main()
