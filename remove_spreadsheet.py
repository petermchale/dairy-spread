import gspread
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import AuthorizedSession
import sys 
import os 

def remove_spreadsheet(url_path): 
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  credentials = Credentials.from_service_account_file('credentials.json', scopes=scope)
  # https://github.com/burnash/gspread/blob/0f22a5d9f9adea7db72c94273d9f69a5a7711398/gspread/client.py#L27
  # https://stackoverflow.com/a/59699007/6674256
  client = gspread.Client(auth=credentials)
  client.session = AuthorizedSession(credentials)

  with open(url_path, 'r') as f: 
    spreadsheet_id = f.readline().replace('https://docs.google.com/spreadsheets/d/','').strip()
  print('Removing spreadsheet with id {}'.format(spreadsheet_id), file=sys.stderr)  
  client.request('delete', 'https://www.googleapis.com/drive/v2/files/{}'.format(spreadsheet_id))
  os.remove(url_path) 
  print('This sheet will disappear from https://drive.google.com/drive/shared-with-me') 
 
if __name__ == '__main__': 
  remove_spreadsheet(sys.argv[1]) 

