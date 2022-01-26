import time
import pyautogui
import os
import subprocess
from python_imagesearch.imagesearch import imagesearch #pip3 install python-imagesearch


def img_open():
    pos = imagesearch("open.png")
    if pos[0] != -1:
        print("Pozice : ", pos[0], pos[1]) #Debug
        pyautogui.click(button='left', x=pos[0] + 10,y=pos[1] + 10, clicks=10) #Poté Else stat.
    else:
        return False

def process_exists(process_name):
    progs = str(subprocess.check_output('tasklist'))
    if process_name in progs:
        #print('True') #Debug
        return True
    else:
        #print('False') #Debug
        return False

def process_run_check():
    while process_exists('dontstarve_steam_x64.exe') == False:
        print('Proces neběží') #Debug
    else:
        print('Proces běží, spouštím definici gift_open_check') #Debug
        gift_open_check()

def runonce():
    os.system("dst.url")

def killprocess():
    os.system("taskkill /IM dontstarve_steam_x64.exe /F")

def gift_open_check():
    while img_open() == False:
        print('Box Nenalezen') #Debug
        time.sleep(2)
    else:
        print('Box Nalezen') #Debug
        time.sleep(5)
        pyautogui.screenshot('my_screenshot.png')
        time.sleep(5)
        killprocess()

runonce()
process_run_check()


