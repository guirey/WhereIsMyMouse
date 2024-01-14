#!/usr/bin/env python
# coding: utf-8

# In[8]:


#script para encontrar o mouse na tela

import pyautogui as pg
import PySimpleGUI as sg 
import time

pg.PAUSE = 2

out = 1

while out == 1:
    
    time.sleep(2)
    posicao = pg.position()


    font = ("Consolas", 12)        #tema         
    sg.set_options(font=font)      #tema  
    sg.theme('Green Mono')         #tema                   


    
    event, values = sg.Window('ReyMouse',
                        [[sg.T(f'O seu mouse está na posição: {posicao}')],
                        [sg.B('nova')],
                        [sg.Cancel('sair')]], element_justification='c').read(close=True) 
    
    if event == sg.WIN_CLOSED or event == 'sair':     
        out = 0
        break
        
    elif event == 'nova':
        out = 1
        time.sleep(1)
        window.refresh()
        
    window.close()


# In[ ]:




