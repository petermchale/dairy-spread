import sys 
import os 
import argparse
from get_url_path import get_url_path
from get_client import get_client

def parse():
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('--bed', type=str, help='')
  parser.add_argument('--credentials', type=str, help='')
  return parser.parse_args()

def remove_spreadsheet(args): 
  client = get_client(args) 
  url_path = get_url_path(args)
  with open(url_path, 'r') as f: 
    spreadsheet_id = f.readline().replace('https://docs.google.com/spreadsheets/d/','').strip()
  print('Removing spreadsheet with id {}'.format(spreadsheet_id), file=sys.stderr)  
  client.request('delete', 'https://www.googleapis.com/drive/v2/files/{}'.format(spreadsheet_id))
  os.remove(url_path) 
  print('This sheet will disappear from https://drive.google.com/drive/shared-with-me') 
 
if __name__ == '__main__': 
  remove_spreadsheet(parse())

