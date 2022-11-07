from pyautogui import *
import time
import keyboard
import win32con
import win32gui
from pynput.mouse import Button, Controller
import PySimpleGUI as sg
import random
import agents
mouse = Controller()


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

    checkbox = values['-CHECKBOX-']

    if event == 'instructions':
        sg.popup('''                            
After choosing an agent, holding 'W' will 
start the script, letting go of 'W' will stop 
it. Press 'Q' to choose a new agent.
Tick the checkbox to automatically open 
valorant when you select an agent.''', text_color='#999999', icon=r'img/val.ico', background_color='#111111', button_color='#999999', title='Instructions')
    
    if event == 'jettpic':
        if checkbox == True:
            open_val()
        
        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.jett_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()

    if event == 'astrapic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.astra_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()
    if event == 'breachpic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.breach_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()
    if event == 'brimpic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.brim_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()
    if event == 'chamberpic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.chamber_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()
    if event == 'cypherpic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.cypher_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()
    if event == 'fadepic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.fade_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()
    if event == 'kayopic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.kayo_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()
    if event == 'kjpic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.kj_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()

    if event == 'harborpic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.harbor_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()

    if event == 'omenpic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.omen_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()
    if event == 'sagepic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.sage_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()
    if event == 'skyepic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.skye_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()
    if event == 'sovapic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.sova_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()
    if event == 'viperpic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.viper_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()

    if event == 'razepic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.raze_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()

    if event == 'neonpic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.neon_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()
    if event == 'phxpic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.phoenix_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()
    if event == 'yorupic':  
        if checkbox == True:  
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.yoru_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()
    if event == 'reynapic':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'): 
                mouse.position = agents.reyna_coords
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()

    if event == 'Roulette':
        if checkbox == True:
            open_val()

        while keyboard.is_pressed('q') == False:
            if keyboard.is_pressed('w'):
                random_agent = random.choice(agents.agents_list)
                mouse.position = random_agent
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
                mouse.position = agents.lock_in
                time.sleep(0.01)
                mouse.click(Button.left, 1)
                time.sleep(0.04)
            window.refresh()

    if event == 'Toggle Display Mode' :
        open_val()

        keyboard.press_and_release('alt+enter')
        window.refresh()
    
    if event == sg.WIN_CLOSED or event == " Exit ":
        break
