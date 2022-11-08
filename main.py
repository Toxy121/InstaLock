from pyautogui import *
import time
import keyboard
import win32con
import win32gui
from pynput.mouse import Button, Controller
import PySimpleGUI as sg
import random
import agents
import json
from requests import session
from valclient.client import Client
mouse = Controller()

regions = ["na", "eu", "latam", "br", "ap", "kr", "pbe"]
sg.theme('DarkAmber')
layout2 = [
    [sg.Button('NA', button_color='#999999'), 

    sg.Button('EU', button_color='#999999'), 
    sg.Button('LATAM', button_color='#999999'), 
    sg.Button('BR', button_color='#999999'), 
    sg.Button('AP', button_color='#999999'), 
    sg.Button('KR', button_color='#999999'), 
    sg.Button('PBE', button_color='#999999')],
]
playerRegion="na"
client = Client(region=playerRegion)
try:
    client.activate()
except:
    print("Valorant isn't open.")
    time.sleep(1)
    print("Would you like to run the script regardless?")
    while True:
        quesiton = input()
        if quesiton.lower() == "no" or quesiton.lower() == "n":
            sys.exit()
            break
        elif quesiton.lower() == "yes" or quesiton.lower() == "y":
            break
        else:
            print("Please enter yes or no.")
valid = False
all_agents = {}
seenMatches = []
with open('data.json', 'r') as f:
    all_agents = json.load(f)

window2 = sg.Window('Region', layout2, icon=r'img/val.ico', background_color='#232323', grab_anywhere=False)
while True:
    events2, values2 = window2.read()
    if events2 == 'NA':
        playerRegion = 'na'
        window2.close()
    elif events2 == 'EU':
        playerRegion = 'eu'
        window2.close()
    elif events2 == 'LATAM':
        playerRegion = 'latam'
        window2.close()
    elif events2 == 'BR':
        playerRegion = 'br'
        window2.close()
    elif events2 == 'AP':
        playerRegion = 'ap'
        window2.close()
    elif events2 == 'KR':
        playerRegion = 'kr'
        window2.close()
    elif events2 == 'PBE':
        playerRegion = 'pbe'
        window2.close()
    elif events2 == sg.WIN_CLOSED:
        break

    

    astra_pic = agents.astra_pic
    breach_pic = agents.breach_pic
    brim_pic = agents.brim_pic
    chamber_pic = agents.chamber_pic
    fade_pic = agents.fade_pic
    jett_pic = agents.jett_pic
    kj_pic = agents.kj_pic
    neon_pic = agents.neon_pic
    omen_pic = agents.omen_pic
    phoenix_pic = agents.phoenix_pic
    cypher_pic = agents.cypher_pic
    kayo_pic = agents.kayo_pic
    skye_pic = agents.skye_pic
    raze_pic = agents.raze_pic
    reyna_pic = agents.reyna_pic
    sage_pic = agents.sage_pic
    sova_pic = agents.sova_pic
    viper_pic = agents.viper_pic
    yoru_pic = agents.yoru_pic
    harbor_pic = agents.harbor_pic

    all_agentslist = []
    with open('data.json', 'r') as f:
        all_agentslist = json.load(f)

    sg.theme('DarkAmber')
    layout = [
        [sg.Text("Pick Your Valorant Agent                                                  ", text_color='#999999', font='Helvetica 12 bold', background_color='#232323'),
        sg.Button(' Instructions ', key='instructions', font='Helvetica 10 bold', button_color='#999999')],
        [sg.Button('', image_data=astra_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='astrapic'),
        sg.Button('', image_data=breach_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='breachpic'),
        sg.Button('', image_data=brim_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='brimpic'),
        sg.Button('', image_data=chamber_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='chamberpic'),
        sg.Button('', image_data=cypher_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='cypherpic'),
        sg.Button('', image_data=fade_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='fadepic'),
        sg.Button('', image_data=harbor_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='harborpic'),
        sg.Button('', image_data=jett_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='jettpic'),
        sg.Button('', image_data=kayo_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='kayopic'),
        sg.Button('', image_data=kj_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='kjpic')],
        [sg.Button('', image_data=neon_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='neonpic'),
        sg.Button('', image_data=omen_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='omenpic'),
        sg.Button('', image_data=phoenix_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='phxpic'),
        sg.Button('', image_data=raze_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='razepic'),
        sg.Button('', image_data=reyna_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='reynapic'),
        sg.Button('', image_data=sage_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='sagepic'),
        sg.Button('', image_data=skye_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='skyepic'),
        sg.Button('', image_data=sova_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='sovapic'),
        sg.Button('', image_data=viper_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='viperpic'),
        sg.Button('', image_data=yoru_pic,
        button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='yorupic')],
        [sg.Button(" Exit ", font='Helvetica 10 bold', button_color='#999999'),
        sg.Button("Toggle Display Mode", font='Helvetica 10 bold', button_color='#999999'),
        sg.Button("Roulette", font='Helvetica 10 bold', button_color='#999999'),
        sg.Checkbox("Auto Open Val", size=(11,30), key='-CHECKBOX-', font='Helvetica 10 bold', text_color='#999999', background_color='#232323')]
    ]


    #                                                Change this file to change the icon
    #                                                                v
    window = sg.Window("InstaLock", layout, icon=r'img/val.ico',background_color='#232323', grab_anywhere=False, margins= (5,10))


    def open_val():
        def windowEnumHandler(hwnd, top_windows):
            top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

        def bringToFront(window_name):
            top_windows = []
            win32gui.EnumWindows(windowEnumHandler, top_windows)
            for i in top_windows:
                if window_name.lower() == i[1].lower():
                    win32gui.ShowWindow(i[0], win32con.SW_SHOWNORMAL)
                    win32gui.SetForegroundWindow(i[0])
                    break
        if __name__ == "__main__":
            winname = "VALORANT  "
            bringToFront(winname)


    while True:
        event, values = window.read(timeout=500)


        if event == 'instructions':
            sg.popup('''                            
    After choosing an agent, the script will 
    automatically lock in the agent that 
    you picked. Hold 'E' after choosing ''', text_color='#999999', icon=r'img/val.ico', background_color='#111111', button_color='#999999', title='Instructions')
        
        
        if event == 'jettpic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'jett'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                    
                except Exception as e:
                    print('', end='')


        if event == 'astrapic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'astra'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')
        if event == 'breachpic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'breach'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')
        if event == 'brimpic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'brimstome'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')
        if event == 'chamberpic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'chamber'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')
        if event == 'cypherpic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'cypher'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')
        if event == 'fadepic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'fade'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')
        if event == 'kayopic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'kayo'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')
        if event == 'kjpic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'killjoy'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')

        if event == 'harborpic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'harbor'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')

        if event == 'omenpic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'omen'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')
        if event == 'sagepic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'sage'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')
        if event == 'skyepic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'skye'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')
        if event == 'sovapic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'sova'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')
        if event == 'viperpic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'viper'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')

        if event == 'razepic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'raze'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')

        if event == 'neonpic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'neon'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')
        if event == 'phxpic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'phoenix'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')
        if event == 'yorupic':  
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'yoru'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character(all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')
        if event == 'reynapic':
            if values['-CHECKBOX-'] == True:
                open_val()
            preferredAgent = 'reyna'
            while True:
                try:
                    window.refresh()
                    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']
                    if ((sessionState == "PREGAME") and (client.pregame_fetch_match()['ID'] not in seenMatches)):
                        print('Agent Select Found')
                        client.pregame_select_character( all_agents['all_agents'][preferredAgent])
                        client.pregame_lock_character(all_agents['all_agents'][preferredAgent])
                        seenMatches.append(client.pregame_fetch_match()['ID'])
                        print('Successfully Locked ' + preferredAgent.capitalize())
                        break
                except Exception as e:
                    print('', end='')

        if event == 'Roulette':
            if values['-CHECKBOX-'] == True:
                open_val()

            while keyboard.is_pressed('q') == False:
                if keyboard.is_pressed('e'):
                    random_agent = random.choice(agents.agents_list)
                    mouse.position = random_agent
                    time.sleep(0.01)
                    mouse.click(Button.left, 1)
                    time.sleep(0.02)
            window.refresh()

        if event == 'Toggle Display Mode' :
            open_val()

            keyboard.press_and_release('alt+enter')
            window.refresh()
        
        if event == sg.WIN_CLOSED or event == " Exit ":
            break
