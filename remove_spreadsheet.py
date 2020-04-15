import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sys 
import os 

def remove_spreadsheet(url_path): 
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
  # https://github.com/burnash/gspread/blob/0f22a5d9f9adea7db72c94273d9f69a5a7711398/gspread/client.py#L27
  client = gspread.authorize(credentials)

  with open(url_path, 'r') as f: 
    spreadsheet_id = f.readline().replace('https://docs.google.com/spreadsheets/d/','').strip()
  print('Removing spreadsheet with id {}'.format(spreadsheet_id), file=sys.stderr)  
  client.request('delete', 'https://www.googleapis.com/drive/v2/files/{}'.format(spreadsheet_id))
  os.remove(url_path) 
  print('This sheet will disappear from https://drive.google.com/drive/shared-with-me') 
 
if __name__ == '__main__': 
  remove_spreadsheet(sys.argv[1]) 

