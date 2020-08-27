import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
from main.important_files.ExcelTopics import Topics

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(r'important_files/client_secret.json', scope)

client = gspread.authorize(creds)
t0 = time.time()
sheet = client.open("test spreadsheet").sheet1
teams = []
teamsRows = []
n = sheet.get_all_records()
print(type(n[0].get(Topics.TeamNumber.value)))
print(str(Topics.TeamNumber.value))
print(n[0].get(str(Topics.TeamNumber.value)))
