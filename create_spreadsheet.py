import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pathlib import Path
from fetch_igv_urls import fetch_igv_urls
import sys 
import os

def spreadsheet_already_exists(url_filename): 
  if Path(url_filename).exists():
    print('Spreadsheet already exists!', file=sys.stderr)
    print('Please run remove script first' , file=sys.stderr)
    return True
  else: 
    return False

def create_spreadsheet(bed_path, url_filename): 
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
  # https://github.com/burnash/gspread/blob/0f22a5d9f9adea7db72c94273d9f69a5a7711398/gspread/client.py#L27
  client = gspread.authorize(credentials)
  
  # https://github.com/burnash/gspread/blob/0f22a5d9f9adea7db72c94273d9f69a5a7711398/gspread/models.py#L39
  spreadsheet = client.create('Missing SVs')
 
  bed_filename = os.path.basename(bed_path)
  data_set_name = bed_filename.replace('.bed', '') + '.sampled' 

  spreadsheet.values_update(
    range='Sheet1!A1',
    params={
      'valueInputOption': 'USER_ENTERED'
    },
    body={
      'values': [[data_set_name]]
    }
  )

  # https://github.com/burnash/gspread/blob/0f22a5d9f9adea7db72c94273d9f69a5a7711398/gspread/models.py#L88
  # make column headings bold
  request_body = {
    'requests': [
      { 
        'repeatCell': {
          'range': {
            'startRowIndex': 1, 
            'endRowIndex': 2
          },
          'cell': {
            'userEnteredFormat': {
              'textFormat': {'bold': True}
            }
          },
          'fields': 'userEnteredFormat.textFormat.bold',
        }
      }
    ]
  }
  spreadsheet.batch_update(request_body)
 
  spreadsheet.values_update(
    range='Sheet1!A2',
    params={
      'valueInputOption': 'USER_ENTERED'
    },
    body={
      'values': [['IGV']]
    }
  )
   
  igv_urls = fetch_igv_urls(bed_path) 
  spreadsheet.values_update(
    range='Sheet1!A3',
    params={
      'valueInputOption': 'USER_ENTERED'
    },
    body={
      'values': igv_urls 
    }
  )
  
  # share spreadsheet url with others via google drive 
  spreadsheet.share('peter.thomas.mchale@gmail.com', perm_type='user', role='writer', notify=False)

  # avoid overwriting spreadsheet and enable removal of spreadsheet
  with open(url_filename, 'w') as f:
    url = 'https://docs.google.com/spreadsheets/d/{}'.format(spreadsheet.id)
    f.write(url + '\n')
    print(url, file=sys.stderr) 
    print("This sheet can also be seen at https://drive.google.com/drive/shared-with-me", file=sys.stderr)

if __name__ == '__main__': 
  if not spreadsheet_already_exists(sys.argv[2]): 
    create_spreadsheet(sys.argv[1], sys.argv[2]) 

