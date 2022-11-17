import pyautogui as auto
import time

while True:
    #Esperar 0.5 segundos
    time.sleep(0.5)
    #Combinacion de teclas alt + tab
    with auto.hold('alt'):
        auto.press(['tab'])
    #Esperar 0.2 segundos
    time.sleep(0.2)
    #Teclear enter
    auto.press('enter')
    #Esperar 0.2 segundos
    time.sleep(0.2)
    #Teclear enter
    auto.press('enter')
    #Esperar 0.2 segundos
    time.sleep(0.4)
    #Combinacion de teclas alt + tab + tab
    with auto.hold('alt'):
        auto.press(['tab', 'tab', 'tab'])
    #Esperar 0.5 segundos
    time.sleep(0.5)
    #Teclear enter
    auto.press('enter')
    #Esperar 6 segundos
    time.sleep(6)
    #Combinacion de teclas alt + tab + tab
    with auto.hold('alt'):
        auto.press(['tab', 'tab', 'tab'])