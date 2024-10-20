from datetime import datetime
import pyautogui
import time
import gspread
from google.oauth2.service_account import Credentials
SCOPE = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file("C:\\afk-notifier-json\\afk-notifier-9e5a1837738d.json", scopes=SCOPE)
client = gspread.authorize(credentials)
sheet = client.open('afk-notifier-sheet').sheet1


print("AFK Notifier running... probably.")
timeout = 300
last_move = time.time()

while True:
    x, y = pyautogui.position()
    time.sleep(40)
    current_time = datetime.now().strftime('%B %d, %Y %I:%M %p')

    if (x, y) != pyautogui.position(): # if mouse moved, last_move = current time
        last_move = time.time()
    
    if time.time() - last_move > timeout: # if last_move > 5 minutes
        print('Inactive (AFK) @ ' + current_time)
        sheet.update(values=[['PC Status', 'Inactive (AFK)', 'As of: ' + current_time]], range_name='A1:C1')
    else:
        print('Active @ ' + current_time)
        sheet.update(values=[['PC Status', 'Active', 'As of: ' + current_time]], range_name='A1:C1')

