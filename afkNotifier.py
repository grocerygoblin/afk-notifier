from datetime import datetime
import pyautogui
import time
import gspread
from google.oauth2.service_account import Credentials

SCOPE = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
# Load service account credentials
credentials = Credentials.from_service_account_file("C:\\afk-notifier-json\\afk-notifier-9e5a1837738d.json", scopes=SCOPE)
# Authenticate with Google Sheets
client = gspread.authorize(credentials)


sheet = client.open('afk-notifier-sheet').sheet1
print("AFK Notifier running... probably.")
timeout = 300
last_move = time.time()


# To Do:
# Add a loop that counts seconds between status updates
# Add a total uptime indicator thingy
# Look into formatting the cell(s)
# Possibly check for steaminput for controller stuff? (idr if i'm even using steaminput on this pc)


while True:
    x, y = pyautogui.position()
    time.sleep(40)
    current_time = datetime.now().strftime('%B %d, %Y %I:%M %p')

    if (x, y) != pyautogui.position():
        last_move = time.time()
    
    if time.time() - last_move > timeout:
        print('Inactive (AFK) @ ' + current_time)
        sheet.update(values=[['PC Status', 'Inactive (AFK)', 'As of: ' + current_time]], range_name='A1:C1')
    else:
        print('Active @ ' + current_time)
        sheet.update(values=[['PC Status', 'Active', 'As of: ' + current_time]], range_name='A1:C1')