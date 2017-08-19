import os

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    _PARSER_ = argparse.ArgumentParser(parents=[tools.argparser])
    _FLAGS_ = _PARSER_.parse_args([])
except ImportError:
    _FLAGS_ = None

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = '/Users/jacksonfoster/.credentials/client_secret.json'
APPLICATION_NAME = 'Inventory Assistant'


def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')

    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'inventory-assistant-credentials1.json')
    store = Storage(credential_path)
    credentials = store.get()

    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if _FLAGS_:
            credentials = tools.run_flow(flow, store, _FLAGS_)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
    print('Storing credentials to ' + credential_path)
    return credentials
