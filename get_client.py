import gspread
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import AuthorizedSession

def get_client(args):
  scopes = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  if args.credentials.endswith('.json'):
    credentials = Credentials.from_service_account_file(args.credentials, scopes=scopes)
  else:
    print('credentials files must be in json format', file=sys.stderr)
    sys.exit()
  # https://github.com/burnash/gspread/blob/0f22a5d9f9adea7db72c94273d9f69a5a7711398/gspread/client.py#L27
  # https://stackoverflow.com/a/59699007/6674256
  client = gspread.Client(auth=credentials)
  client.session = AuthorizedSession(credentials)
  return client
