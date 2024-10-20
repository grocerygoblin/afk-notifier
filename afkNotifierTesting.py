from datetime import datetime
import pdb
import pyautogui
import time
import gspread
import ctypes
from google.oauth2.service_account import Credentials
# SCOPE = ['https://www.googleapis.com/auth/spreadsheets',
#          'https://www.googleapis.com/auth/drive']
# credentials = Credentials.from_service_account_file("C:\\afk-notifier-json\\afk-notifier-9e5a1837738d.json", scopes=SCOPE)
# client = gspread.authorize(credentials)
# sheet = client.open('afk-notifier-sheet').sheet1


print("AFK Notifier running... most likely, anyway.")
timeout = 30
last_move = time.time()
awayStatus = False




while True:
    for i in range(1, 4):
        time.sleep(1)
        ctypes.windll.kernel32.SetConsoleTitleW('AFK Notifier ' + str(i))
    x, y = pyautogui.position()
    current_time = datetime.now().strftime('%B %d, %Y %I:%M %p')
    
    if awayStatus == False:
        print('Printing to sheet:')
        print(['', 'Total activity time: ', uptime])

    if (x, y) != pyautogui.position(): # if mouse moved, last_move = current time
        last_move = time.time()
    
    if time.time() - last_move > timeout: # if last_move > 5 minutes
        awayStatus = True
        print('Inactive (AFK) @ ' + current_time + '\t (Checking again in 4 seconds...)')
        print('Printing to sheet:')
        print(['Inactive', 'Last seen: ', current_time])
        # sheet.update(values=[['Inactive', 'Last seen: ',current_time]], range_name='A1:C1')
    else:
        awayStatus = False
        activity_start = time.time()
        uptime = activity_start - time.time()
        print('Active @ ' + current_time + '\t (Checking again in 4 seconds...)')
        print('Printing to sheet:')
        print(['Active', 'Most recently at: ', current_time])
        # sheet.update(values=[['Active', 'Most recently at: ', current_time]], range_name='A1:C1')
        # sheet.update(values=[['', 'Total activity time: ', uptime]], range_name='A2:C2')




# To Do:
# Add a total uptime indicator thingy
# Look into formatting the cell(s)
# Add some other form of notification if the time has been long enough, like over 45 minutes or something
#   - Maybe a twitter bot?
# Possibly check for steaminput for controller stuff? (idr if i'm even using steaminput on this pc)