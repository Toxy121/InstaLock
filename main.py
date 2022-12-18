from pyautogui import *
import sys
from pynput.mouse import Button, Controller
import json
from requests import session
from valclient.client import Client
import os
from os import system
from colorama import Fore
import string
import edit_agents
mouse = Controller()




try:
    with open('json/data.json', 'r') as f:
        data = json.load(f)
        all_agents = data['all_agents']
        maps = data['maps']
        map_codes = data['map_codes']
        region = data['region']


    system("title " + "InstaLock")
    playerRegion=region
    if playerRegion == '':
        os.system('cls')
        print(' Make Sure You Have Entered Your Region Correctly')
        enter_region = input(" Would You Like To Enter Your Region Now? ")
        if enter_region.lower() == 'yes' or enter_region.lower() == 'y':
            print('')
            edit_agents.region()
        elif enter_region.lower() == 'no' or enter_region.lower() == 'n':
            sys.exit()
        else:
            print(Fore.RED + 'Invalid Input' + Fore.WHITE)
            sys.exit()

    client = Client(region=playerRegion)
    try:
        client.activate()
    except:
        print("Make sure you have Valorant open.")
    valid = False
    #all_agents = {}
    seenMatches = []
   


    def checkmap():
        if maps['ascent'] == "" and maps['bind'] == "" and maps['breeze'] == "" and maps['fracture'] == "" and maps['haven'] == "" and maps['icebox'] == "" and maps['pearl'] == "":
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
        if maps['ascent'] == "" or maps['bind'] == "" or maps['breeze'] == "" or maps['fracture'] == "" or maps['haven'] == "" or maps['icebox'] == "" or maps['pearl'] == "":
            os.system('cls')
            print(Fore.RED + "You do not have an agent for the following map(s):")
            dash = '-'
            print(Fore.WHITE+ dash*50)
        if maps['ascent'] == "":
            print(Fore.BLUE +"Ascent" + Fore.WHITE)
        if maps['bind'] == "":
            print(Fore.GREEN + "Bind" + Fore.WHITE)
        if maps['breeze'] == "":
            print(Fore.YELLOW + "Breeze" + Fore.WHITE)
        if maps['fracture'] == "":
            print(Fore.CYAN + "Fracture" + Fore.WHITE)
        if maps['haven'] == "":
            print(Fore.LIGHTMAGENTA_EX + "Haven" + Fore.WHITE)
        if maps['icebox'] == "":
            print(Fore.LIGHTRED_EX + "Icebox" + Fore.WHITE)
        if maps['pearl'] == "":
            print(Fore.LIGHTCYAN_EX + "Pearl" + Fore.WHITE)
        if maps['ascent'] == "" or maps['bind'] == "" or maps['breeze'] == "" or maps['fracture'] == "" or maps['haven'] == "" or maps['icebox'] == "" or maps['pearl'] == "":
            sys.exit()
        if maps['ascent'] not in all_agents:
            os.system('cls')
            print(Fore.RED + maps['ascent'] + " is not a valid agent." + Fore.WHITE)
            sys.exit()
        if maps['bind'] not in all_agents:
            os.system('cls')
            print(Fore.RED + maps['bind'] + " is not a valid agent." + Fore.WHITE)
            sys.exit()
        if maps['breeze'] not in all_agents:
            os.system('cls')
            print(Fore.RED + maps['breeze'] + " is not a valid agent." + Fore.WHITE)
            sys.exit()
        if maps['fracture'] not in all_agents:
            os.system('cls')
            print(Fore.RED + maps['fracture'] + " is not a valid agent." + Fore.WHITE)
            sys.exit()
        if maps['haven'] not in all_agents:
            os.system('cls')
            print(Fore.RED + maps['haven'] + " is not a valid agent." + Fore.WHITE)
            sys.exit()
        if maps['icebox'] not in all_agents:
            os.system('cls')
            print(Fore.RED + maps['icebox'] + " is not a valid agent." + Fore.WHITE)
            sys.exit()
        if maps['pearl'] not in all_agents:
            os.system('cls')
            print(Fore.RED + maps['pearl'] + " is not a valid agent." + Fore.WHITE)
            sys.exit()

    checkmap()




    def lock_in():
        while True:
            try:
                sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                matchID = client.pregame_fetch_match()['ID']
                if ((sessionState == "PREGAME") and (matchID not in seenMatches)):
                    matchInfo = client.pregame_fetch_match(matchID)
                    mapName = matchInfo["MapID"].split('/')[-1].lower()
                    print(Fore.GREEN + f'Found {map_codes[mapName].capitalize()}' + Fore.WHITE)
                    print(Fore.GREEN + 'Agent Select Found' + Fore.WHITE)
                    client.pregame_select_character(all_agents[maps[map_codes[mapName].lower()]])
                    client.pregame_lock_character(all_agents[maps[map_codes[mapName].lower()]])
                    print(Fore.GREEN + 'Successfully Locked ' + maps[map_codes[mapName]] + Fore.WHITE)
                    seenMatches.append(client.pregame_fetch_match()['ID'])
                    #break
                    sys.exit()
            except Exception as e:
                        print('', end='')

    os.system('cls')






    #brimstone  | = 12
    asc = len([ele for ele in maps['ascent'].capitalize() if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
    asc_calc = 10 - asc
    bind = len([ele for ele in maps['bind'].capitalize() if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
    bind_calc = 10 - bind
    breeze = len([ele for ele in maps['breeze'].capitalize() if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
    breeze_calc = 10 - breeze
    frac = len([ele for ele in maps['fracture'].capitalize() if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
    frac_calc = 10 - frac
    haven = len([ele for ele in maps['haven'].capitalize() if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
    haven_calc = 10 - haven
    icebox = len([ele for ele in maps['icebox'].capitalize() if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
    icebox_calc = 10 - icebox
    pearl = len([ele for ele in maps['pearl'].capitalize() if ele in string.ascii_uppercase or ele in string.ascii_lowercase])
    pearl_calc = 10 - pearl

    space = ' '

    text = '                                            '
    underlined_text = "\x1B[4m" + text + "\x1B[0m"
    print(f'  {Fore.RED}Your Agents For Each Map{Fore.WHITE}')
    print(f"\n  Region: {region.upper()}")
    print(f'''  ---------------------------
 |    {Fore.LIGHTBLUE_EX}Map{Fore.WHITE}     |    {Fore.GREEN}Agent{Fore.WHITE}     |
 |---------------------------|
 |   {Fore.LIGHTBLUE_EX}Ascent{Fore.WHITE}   |    {Fore.GREEN}{maps['ascent'].capitalize()}{asc_calc*space}{Fore.WHITE}|
 |   {Fore.LIGHTBLUE_EX}Bind{Fore.WHITE}     |    {Fore.GREEN}{maps['bind'].capitalize()}{bind_calc*space}{Fore.WHITE}|
 |   {Fore.LIGHTBLUE_EX}Breeze{Fore.WHITE}   |    {Fore.GREEN}{maps['breeze'].capitalize()}{breeze_calc*space}{Fore.WHITE}|
 |   {Fore.LIGHTBLUE_EX}Fracture{Fore.WHITE} |    {Fore.GREEN}{maps['fracture'].capitalize()}{frac_calc*space}{Fore.WHITE}|
 |   {Fore.LIGHTBLUE_EX}Haven{Fore.WHITE}    |    {Fore.GREEN}{maps['haven'].capitalize()}{haven_calc*space}{Fore.WHITE}|
 |   {Fore.LIGHTBLUE_EX}Icebox{Fore.WHITE}   |    {Fore.GREEN}{maps['icebox'].capitalize()}{icebox_calc*space}{Fore.WHITE}|
 |   {Fore.LIGHTBLUE_EX}Pearl{Fore.WHITE}    |    {Fore.GREEN}{maps['pearl'].capitalize()}{pearl_calc*space}{Fore.WHITE}|''')
    print('  ---------------------------')
    #print(underlined_text)
    print('')


    print(Fore.LIGHTMAGENTA_EX + "  Waiting for loading screen..." + Fore.WHITE)



    while True:
        lock_in()
except KeyboardInterrupt:
    sys.exit()
