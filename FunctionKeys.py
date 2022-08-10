# gesture control python program for controlling certain functions in windows pc

import serial                                      # add Serial library for serial communication
import pyautogui                                   # add pyautogui library for programmatically controlling the mouse and keyboard.

Arduino_Serial = serial.Serial('ENTER_SERIAL_NUMBER',ENTER_BAUD_RATE)        # Initialize serial and Create Serial port object called Arduino_Serial
 
while 1:
    incoming_data = str (Arduino_Serial.readline()) # read the serial data and print it as line
    print(incoming_data)                            # print the incoming Serial data

    if 'play/pause' in incoming_data:              # if incoming data is 'play/pause'
        pyautogui.typewrite(['space'],0.2)         # performs "space" operation which play and pause the video

    if 'rewind' in incoming_data:                  # if incoming data is 'rewind'
        pyautogui.hotkey('ctrl','left')            # perform "crtl+left arrow" operation which moves the video back

    if 'forward' in incoming_data:                  # if incoming data is 'forward'
        pyautogui.hotkey('ctrl','right')            # perform "crtl+right arrow" operation which moves the video forward
    
    if 'next' in incoming_data:                    # if incoming data is 'next'
        pyautogui.hotkey('ctrl', 'pgdn')           # perform "ctrl+pgdn" operation which moves to the next tab
        
    if 'previous' in incoming_data:                # if incoming data is 'previous'
        pyautogui.hotkey('ctrl', 'pgup')           # perform "ctrl+pgup" operation which moves to the previous tab

    if 'down' in incoming_data:                    # if incoming data is 'down'
        #pyautogui.press('down')                   # performs "down arrow" operation which scrolls down the page
        pyautogui.scroll(-100) 
         
    if 'up' in incoming_data:                      # if incoming data is 'up'
        #pyautogui.press('up')                     # performs "up arrow" operation which scrolls up the page
        pyautogui.scroll(100)
        
    if 'change' in incoming_data:                  # if incoming data is 'change'
        pyautogui.keyDown('alt')                   # performs "alt+tab" operation which switches the tab
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
        
    incoming_data = "";                            # clears the data
