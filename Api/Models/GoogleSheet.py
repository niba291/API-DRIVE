from googleapiclient.discovery import build
from google.oauth2 import service_account

class GoogleSheet:

    SPREADSHEET_ID  = None
    SHEET_NAME      = None
    RANGE           = None
    CREDS           = None
    SERVICE         = None
    SHEET           = None
    KEY             = "E:/Proyectos/API-DRIVE/credentials.json"
    SCOPE           = ["https://www.googleapis.com/auth/spreadsheets"]

    def __init__(self, spreadsheet_id, sheet_name, range):
        try:
            self.SPREADSHEET_ID = spreadsheet_id
            self.SHEET_NAME     = sheet_name
            self.RANGE          = range
            self.CREDS          = service_account.Credentials.from_service_account_file(self.KEY, scopes=self.SCOPE)
            self.SERVICE        = build("sheets", "v4", credentials=self.CREDS)
            self.SHEET          = self.SERVICE.spreadsheets()
        except Exception as e:
            print(e)
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
                range           = f"{self.SHEET_NAME}!{self.RANGE}"
            ).execute()

            auxReturn           = []

            for element in result["values"][1:]:
                obj             = {}
                for index, item in enumerate(result["values"][0]):
                    obj[item]   = element[index]
                
                auxReturn.append(obj)

            return auxReturn
        except Exception as e:
            print(e)
            exit(1)

    def append(self, data):
        try:
            result               = self.SHEET.values().append(
                spreadsheetId    = self.SPREADSHEET_ID, 
                range            = f"{self.SHEET_NAME}!{self.RANGE}", 
                valueInputOption = "USER_ENTERED", 
                body             = {"values": data}
            ).execute()
            return result
        except Exception as e:
            print(e)
            exit(1)

    def update(self, data):
        try:
            result               = self.SHEET.values().update(
                spreadsheetId    = self.SPREADSHEET_ID, 
                range            = f"{self.SHEET_NAME}!{self.RANGE}", 
                valueInputOption = "USER_ENTERED", 
                body             = {"values": data}
            ).execute()
            return result
        except Exception as e:
            print(e)
            exit(1)

    def delete(self):
        try:
            result                  = self.SHEET.batchUpdate(
                spreadsheetId       = self.SPREADSHEET_ID, 
                body                = {
                    "requests"      : [
                        {
                            "deleteDimension": {
                                "range": {
                                    "sheetId"    : 1234651651,
                                    "dimension"  : "ROWS",
                                    "startIndex" : 1,
                                    "endIndex"   : 2
                                }
                            }
                        }
                    ]
                }
            ).execute()
            return result
        except Exception as e:
            print(e)
            exit(1)

    def info(self):
        return self.SHEET.sheets()