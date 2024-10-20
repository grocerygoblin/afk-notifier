from datetime import datetime
import pyautogui
import time
import gspread
from google.oauth2.service_account import Credentials

SCOPE = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
# Load service account credentials
credentials = Credentials.from_service_account_file("afk-notifier-9e5a1837738d.json", scopes=SCOPE)
# Authenticate with Google Sheets
client = gspread.authorize(credentials)


sheet = client.open('afk-notifier-sheet').sheet1
current_time = datetime.now().strftime('%B %d, %Y %I:%M %p')
timeout = 300
last_move = time.time()

while True:
    x, y = pyautogui.position()
    time.sleep(40)

    if (x, y) != pyautogui.position():
        last_move = time.time()
    
    if time.time() - last_move > timeout:
        print('Inactive (AFK)')
        sheet.update(values=[['PC Status', 'Inactive (AFK)', 'As of: ' + current_time]], range_name='A1:C1')
    else:
        print('Active')
        sheet.update(values=[['PC Status', 'Active', 'As of: ' + current_time]], range_name='A1:C1')