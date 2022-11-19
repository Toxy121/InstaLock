from pyautogui import *
import pyautogui
import time
import sys
import win32api, win32con
import keyboard
import win32gui
from pynput.mouse import Button, Controller
import json
from requests import session
from valclient.client import Client
import os
from os import system
from colorama import Fore, Back, Style
import string
import edit_agents
mouse = Controller()

try:
    system("title " + "InstaLock")
    playerRegion="na"
    client = Client(region=playerRegion)
    try:
        client.activate()
    except:
        print("Make sure you have Valorant open.")
    valid = False
    all_agents = {}
    seenMatches = []
    with open('json/agents.json', 'r') as f:
        all_agents = json.load(f)

    with open('json/maps.json', 'r') as f:
        maps = json.load(f)


    def checkmap():
        if maps['maps']['ascent'] == "" and maps['maps']['bind'] == "" and maps['maps']['breeze'] == "" and maps['maps']['fracture'] == "" and maps['maps']['haven'] == "" and maps['maps']['icebox'] == "" and maps['maps']['pearl'] == "":
            os.system('cls')
            print(Fore.RED + "You have no agents for any map.")
            add_now = input(Fore.RED + "Would you like to add them now? "+Fore.WHITE)
            if add_now.lower() == "yes" or add_now.lower() == "y":
                os.system('cls')
                edit_agents.main()
            elif add_now.lower() == "no" or add_now.lower() == "n":
                sys.exit()
            else:
                print("")
                print(Fore.RED + "Invalid input." + Fore.WHITE)
                sys.exit()
        if maps['maps']['ascent'] == "" or maps['maps']['bind'] == "" or maps['maps']['breeze'] == "" or maps['maps']['fracture'] == "" or maps['maps']['haven'] == "" or maps['maps']['icebox'] == "" or maps['maps']['pearl'] == "":
            os.system('cls')
            print(Fore.RED + "You do not have an agent for the following map(s):")
            dash = '-'
            print(Fore.WHITE+ dash*50)
        if maps['maps']['ascent'] == "":
            print(Fore.BLUE +"Ascent" + Fore.WHITE)
        if maps['maps']['bind'] == "":
            print(Fore.GREEN + "Bind" + Fore.WHITE)
        if maps['maps']['breeze'] == "":
            print(Fore.YELLOW + "Breeze" + Fore.WHITE)
        if maps['maps']['fracture'] == "":
            print(Fore.CYAN + "Fracture" + Fore.WHITE)
        if maps['maps']['haven'] == "":
            print(Fore.LIGHTMAGENTA_EX + "Haven" + Fore.WHITE)
        if maps['maps']['icebox'] == "":
            print(Fore.LIGHTRED_EX + "Icebox" + Fore.WHITE)
        if maps['maps']['pearl'] == "":
            print(Fore.LIGHTCYAN_EX + "Pearl" + Fore.WHITE)
        if maps['maps']['ascent'] == "" or maps['maps']['bind'] == "" or maps['maps']['breeze'] == "" or maps['maps']['fracture'] == "" or maps['maps']['haven'] == "" or maps['maps']['icebox'] == "" or maps['maps']['pearl'] == "":
            sys.exit()
        if maps['maps']['ascent'] not in all_agents['all_agents']:
            os.system('cls')
            print(Fore.RED + maps['maps']['ascent'] + " is not a valid agent." + Fore.WHITE)
            sys.exit()
        if maps['maps']['bind'] not in all_agents['all_agents']:
            os.system('cls')
            print(Fore.RED + maps['maps']['bind'] + " is not a valid agent." + Fore.WHITE)
            sys.exit()
        if maps['maps']['breeze'] not in all_agents['all_agents']:
            os.system('cls')
            print(Fore.RED + maps['maps']['breeze'] + " is not a valid agent." + Fore.WHITE)
            sys.exit()
        if maps['maps']['fracture'] not in all_agents['all_agents']:
            os.system('cls')
            print(Fore.RED + maps['maps']['fracture'] + " is not a valid agent." + Fore.WHITE)
            sys.exit()
        if maps['maps']['haven'] not in all_agents['all_agents']:
            os.system('cls')
            print(Fore.RED + maps['maps']['haven'] + " is not a valid agent." + Fore.WHITE)
            sys.exit()
        if maps['maps']['icebox'] not in all_agents['all_agents']:
            os.system('cls')
            print(Fore.RED + maps['maps']['icebox'] + " is not a valid agent." + Fore.WHITE)
            sys.exit()
        if maps['maps']['pearl'] not in all_agents['all_agents']:
            os.system('cls')
            print(Fore.RED + maps['maps']['pearl'] + " is not a valid agent." + Fore.WHITE)
            sys.exit()

    checkmap()




    def lock_in(agent):
        while True:
            try:
                sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                    print(Fore.GREEN + 'Agent Select Found')
                    client.pregame_select_character(all_agents['all_agents'][agent])
                    client.pregame_lock_character(all_agents['all_agents'][agent])
                    seenMatches.append(client.pregame_fetch_match()['ID'])
                    print(Fore.GREEN + 'Successfully Locked ' + agent.capitalize() + Fore.WHITE)
                    break
            except Exception as e:
                        print('', end='')

    os.system('cls')






    #brimstone  | = 12
    asc = len([ele for ele in maps['maps']['ascent'].capitalize() if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
    asc_calc = 10 - asc
    bind = len([ele for ele in maps['maps']['bind'].capitalize() if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
    bind_calc = 10 - bind
    breeze = len([ele for ele in maps['maps']['breeze'].capitalize() if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
    breeze_calc = 10 - breeze
    frac = len([ele for ele in maps['maps']['fracture'].capitalize() if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
    frac_calc = 10 - frac
    haven = len([ele for ele in maps['maps']['haven'].capitalize() if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
    haven_calc = 10 - haven
    icebox = len([ele for ele in maps['maps']['icebox'].capitalize() if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
    icebox_calc = 10 - icebox
    pearl = len([ele for ele in maps['maps']['pearl'].capitalize() if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
    pearl_calc = 10 - pearl

    space = ' '

    text = '                                            '
    underlined_text = "\x1B[4m" + text + "\x1B[0m"
    print(f'  {Fore.RED}Your Agents For Each Map{Fore.WHITE}')
    print('')
    print(f'''  ---------------------------
 |    {Fore.LIGHTBLUE_EX}Map{Fore.WHITE}     |    {Fore.GREEN}Agent{Fore.WHITE}     |
 |---------------------------|
 |   {Fore.LIGHTBLUE_EX}Ascent{Fore.WHITE}   |    {Fore.GREEN}{maps['maps']['ascent'].capitalize()}{asc_calc*space}{Fore.WHITE}|
 |   {Fore.LIGHTBLUE_EX}Bind{Fore.WHITE}     |    {Fore.GREEN}{maps['maps']['bind'].capitalize()}{bind_calc*space}{Fore.WHITE}|
 |   {Fore.LIGHTBLUE_EX}Breeze{Fore.WHITE}   |    {Fore.GREEN}{maps['maps']['breeze'].capitalize()}{breeze_calc*space}{Fore.WHITE}|
 |   {Fore.LIGHTBLUE_EX}Fracture{Fore.WHITE} |    {Fore.GREEN}{maps['maps']['fracture'].capitalize()}{frac_calc*space}{Fore.WHITE}|
 |   {Fore.LIGHTBLUE_EX}Haven{Fore.WHITE}    |    {Fore.GREEN}{maps['maps']['haven'].capitalize()}{haven_calc*space}{Fore.WHITE}|
 |   {Fore.LIGHTBLUE_EX}Icebox{Fore.WHITE}   |    {Fore.GREEN}{maps['maps']['icebox'].capitalize()}{icebox_calc*space}{Fore.WHITE}|
 |   {Fore.LIGHTBLUE_EX}Pearl{Fore.WHITE}    |    {Fore.GREEN}{maps['maps']['pearl'].capitalize()}{pearl_calc*space}{Fore.WHITE}|''')
    print('  ---------------------------')
    #print(underlined_text)
    print('')


    print(Fore.LIGHTMAGENTA_EX + "  Waiting for loading screen..." + Fore.WHITE)



    while 1:
        if pyautogui.locateOnScreen('img/saved_ascent.png', region=(680,460,560,185), grayscale=True, confidence=0.8) != None:
            print("")
            print(Fore.GREEN + 'Found Ascent')
            lock_in(agent = maps['maps']['ascent'])
            sys.exit()
        elif pyautogui.locateOnScreen('img/saved_bind.png', region=(680,460,560,185), grayscale=True, confidence=0.8) != None:
            print("")
            print(Fore.GREEN + 'Found Bind')
            lock_in(agent = maps['maps']['bind'])
            sys.exit()
        elif pyautogui.locateOnScreen('img/saved_breeze.png', region=(680,460,560,185), grayscale=True, confidence=0.8) != None:
            print("")
            print(Fore.GREEN + 'Found Breeze')
            lock_in(agent = maps['maps']['breeze'])
            sys.exit()
        elif pyautogui.locateOnScreen('img/saved_fracture.png', region=(680,460,560,185), grayscale=True, confidence=0.8) != None:
            print("")
            print(Fore.GREEN + 'Found Fracture')
            lock_in(agent = maps['maps']['fracture'])
            sys.exit()
        elif pyautogui.locateOnScreen('img/saved_haven.png', region=(680,460,560,185), grayscale=True, confidence=0.8) != None:
            print("")
            print(Fore.GREEN + 'Found Haven')
            lock_in(agent = maps['maps']['haven'])
            sys.exit()
        elif pyautogui.locateOnScreen('img/saved_icebox.png', region=(680,460,560,185), grayscale=True, confidence=0.8) != None:
            print("")
            print(Fore.GREEN + 'Found Icebox')
            lock_in(agent = maps['maps']['icebox'])
            sys.exit()
        elif pyautogui.locateOnScreen('img/saved_pearl.png', region=(680,460,560,185), grayscale=True, confidence=0.8) != None:
            print("")
            print(Fore.GREEN + 'Found Pearl')
            lock_in(agent = maps['maps']['pearl'])
            sys.exit()
except KeyboardInterrupt:
    sys.exit()
