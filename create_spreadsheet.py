import gspread
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import AuthorizedSession
from pathlib import Path
from fetch_igv_urls_annotations import fetch_igv_urls_annotations
import sys 
import argparse

def spreadsheet_already_exists(args):
  if Path(get_url_filename(args)).exists():
    print('Spreadsheet already exists for\n{}'.format(args.bed), file=sys.stderr)
    print('Please run remove script first!' , file=sys.stderr)
    return True
  else: 
    return False

def get_url_filename(args): 
  bed_path = args.bed 
  if bed_path.endswith('.bed'):
    return bed_path[:-4] + '.url'
  else:
    print('input file must be in bed format', file=sys.stderr)
    sys.exit()

def create_spreadsheet(args):
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

  if args.credentials.endswith('.json'): 
    credentials = Credentials.from_service_account_file(args.credentials, scopes=scope)
  else: 
    print('credentials files must be in json format', file=sys.stderr) 
    sys.exit()

  # https://github.com/burnash/gspread/blob/0f22a5d9f9adea7db72c94273d9f69a5a7711398/gspread/client.py#L27
  # https://stackoverflow.com/a/59699007/6674256
  client = gspread.Client(auth=credentials)
  client.session = AuthorizedSession(credentials)

  # https://github.com/burnash/gspread/blob/0f22a5d9f9adea7db72c94273d9f69a5a7711398/gspread/models.py#L39
  spreadsheet = client.create(args.title)
 
  spreadsheet.values_update(
    range='Sheet1!A1',
    params={
      'valueInputOption': 'USER_ENTERED'
    },
    body={
      'values': [['source file:' + args.bed]]
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
      'values': [['locus', args.column_heading]]
    }
  )
  
  igv_urls, annotations = fetch_igv_urls_annotations(args.bed) 
 
  spreadsheet.values_update(
    range='Sheet1!A3',
    params={
      'valueInputOption': 'USER_ENTERED'
    },
    body={
      'values': igv_urls 
    }
  )
 
  spreadsheet.values_update(
    range='Sheet1!B3',
    params={
      'valueInputOption': 'USER_ENTERED'
    },
    body={
      'values': annotations 
    }
  )
 
  # share spreadsheet url with others via google drive 
  spreadsheet.share(args.email, perm_type='user', role='writer', notify=False)

  # enable removal of spreadsheet
  with open(get_url_filename(args), 'w') as f:
    url = 'https://docs.google.com/spreadsheets/d/{}'.format(spreadsheet.id)
    f.write(url + '\n')
    print(url, file=sys.stderr) 
    print("This sheet can also be seen at https://drive.google.com/drive/shared-with-me", file=sys.stderr)

def parse(): 
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('--title', type=str, help='')
  parser.add_argument('--bed', type=str, help='')
  parser.add_argument('--column_heading', type=str, help='')
  parser.add_argument('--email', type=str, help='')
  parser.add_argument('--credentials', type=str, help='')
  return parser.parse_args()
 
if __name__ == '__main__': 
 
  if not spreadsheet_already_exists(parse()): 
    create_spreadsheet(parse())

