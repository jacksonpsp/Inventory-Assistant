from __future__ import print_function
from pprint import pprint
from googleapiclient import discovery
import sys
import httplib2
import os
import os.path
import json
import sys
sys.path.append('/Users/jacksonfoster/Code/inventory')
import google_sheets as gs

def main():
    apicredentials = gs.get_credentials()
    http = apicredentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1hkVBp5Gducx1SCa-nXcwCFznGr_SI5Mykg74rqUj9lc'
    range_ = 'G27:G30'
    request = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_, majorDimension="ROWS")
    response = request.execute()
    print(json.dumps(response, indent=4))
main()
