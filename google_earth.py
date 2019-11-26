import datetime
import os, time
import pyautogui
from pywinauto import Application, mouse
from pywinauto import keyboard

directory = 'D://Shakir//Timeline Images//'
file_name = 'DHA Office.kmz'  # write kml file name
no_of_images = 1  # no of screen shots
waiting_time_seconds = 15  # waiting time in seconds
kml_path = directory + file_name
os.startfile(kml_path)
time.sleep(waiting_time_seconds+10)  # wait for completely loading Google Earth
keyboard.send_keys('%V')
keyboard.send_keys('{DOWN 11}')
keyboard.send_keys('{ENTER}')
kml_name = file_name[:-4]
today = datetime.date.today().strftime('%d-%m-%y')
directory = directory + '/' + today
if not os.path.exists(directory):
    os.makedirs(directory)
for i in range(no_of_images):
    mouse.click(button='left', coords=(30, 113))
    time.sleep(waiting_time_seconds)
    x, y = pyautogui.size()
    # screen_shot = pyautogui.screenshot()
    screen_shot = pyautogui.screenshot(region=(0, 70, x, y - 140))
    screen_shot_name = kml_name + '_' + str(i + 1) + '.png'
    output_directory = directory + '/' + screen_shot_name
    screen_shot.save(output_directory)
