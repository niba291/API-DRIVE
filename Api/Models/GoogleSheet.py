from googleapiclient.discovery import build
from google.oauth2 import service_account

class GoogleSheet:

    SPREADSHEET_ID  = None
    RANGE           = None
    CREDS           = None
    SERVICE         = None
    SHEET           = None
    KEY             = "E:/Proyectos/API-DRIVE/credentials.json"
    SCOPE           = ["https://www.googleapis.com/auth/spreadsheets"]

    def __init__(self, spreadsheetId, range):
        try:
            self.SPREADSHEET_ID = spreadsheetId
            self.RANGE          = range
            self.CREDS          = service_account.Credentials.from_service_account_file(self.KEY, scopes=self.SCOPE)
            self.SERVICE        = build("sheets", "v4", credentials=self.CREDS)
            self.SHEET          = self.SERVICE.spreadsheets()
        except Exception as e:
            print({
                "error"     : True,
                "response"  : e
            })
            exit(1)

    def get(self, filter = None):
        try:

            if filter != None:
                self.SHEET_NAME = "FILTER"
                auxRange        = self.RANGE.split(":")
                self.RANGE      = "B1"
                self.update(filter)
                self.RANGE      = f"{auxRange[0]}2:{auxRange[1]}"

            result              = self.SHEET.values().get(
                spreadsheetId   = self.SPREADSHEET_ID, 
                range           = self.RANGE
            ).execute()

            auxReturn           = []

            for element in result["values"][1:]:
                obj             = {}
                for index, item in enumerate(result["values"][0]):
                    obj[item]   = element[index]
                
                auxReturn.append(obj)

            return auxReturn
        except Exception as e:
            print({
                "error"     : True,
                "response"  : e
            })
            exit(1)

    def add(self, data):
        try:
            result               = self.SHEET.values().append(
                spreadsheetId    = self.SPREADSHEET_ID, 
                range            = self.RANGE, 
                valueInputOption = "USER_ENTERED", 
                body             = {"values": data}
            ).execute()
            return result
        except Exception as e:
            print({
                "error"     : True,
                "response"  : e
            })
            exit(1)

    def update(self, data):
        try:
            result               = self.SHEET.values().update(
                spreadsheetId    = self.SPREADSHEET_ID, 
                range            = self.RANGE, 
                valueInputOption = "USER_ENTERED", 
                body             = {"values": data}
            ).execute()
            return result
        except Exception as e:
            print({
                "error"     : True,
                "response"  : e
            })
            exit(1)

    def delete(self, idSheet):
        try:
            auxRange                = self.RANGE.split(":")
            result                  = self.SHEET.batchUpdate(
                spreadsheetId       = self.SPREADSHEET_ID, 
                body                = {
                    "requests"      : [
                        {
                            "deleteDimension": {
                                "range": {
                                    "sheetId"    : idSheet,
                                    "dimension"  : "ROWS",
                                    "startIndex" : auxRange[0],
                                    "endIndex"   : auxRange[1]
                                }
                            }
                        }
                    ]
                }
            ).execute()
            return result
        except Exception as e:
            print({
                "error"     : True,
                "response"  : e
            })
            exit(1)

    def info(self):
        return self.SHEET.sheets()