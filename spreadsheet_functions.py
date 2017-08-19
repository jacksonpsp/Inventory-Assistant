import httplib2
from googleapiclient import discovery
import google_sheets as gs

_APICREDENTIALS_ = gs.get_credentials()
_HTTP_ = _APICREDENTIALS_.authorize(httplib2.Http())
_DISCOVERYURL_ = ('https://sheets.googleapis.com/$discovery/rest?' 'version=v4')
_SERVICE_ = discovery.build('sheets', 'v4', http=_HTTP_, discoveryServiceUrl=_DISCOVERYURL_)
_SPREADSHEETID_ = '1hkVBp5Gducx1SCa-nXcwCFznGr_SI5Mykg74rqUj9lc'

def getValues(range_, valueRenderOption="FORMATTED_VALUE", majorDimension="ROWS"):
    #range_ = "data range in A1 notation", valueRenderOption = "FORMATTED_VALUE", "UNFORMATTED_VALUE", "FORMULA"

    request = _SERVICE_.spreadsheets().values().get(_SPREADSHEETID_, range=range_, majorDimension=majorDimension, valueRenderOption=valueRenderOption)
    response = request.execute()

    return response["values"]




def formatData(data=[]):
    formattedData = {
    "majorDimension": "ROWS",
    "values":[]
    }

    for i in range(0, len(data)):
        formattedData["values"].append([data[i]])
    return formattedData






def setValues(data, range_, valueInputOption="RAW"):
    # data = array [1,2,3,4,5 etc], range_ = "A1 notation", valueInputOption = "RAW" "INPUT_VALUE_OPTION_UNSPECIFIED", "USER_ENTERED"
    newData = formatData(data)

    request = _SERVICE_.spreadsheets().values().update(spreadsheetId=_SPREADSHEETID_, range=range_, valueInputOption=valueInputOption, body=newData)
    response = request.execute()

setValues([1,2,3], "G5:G7")
