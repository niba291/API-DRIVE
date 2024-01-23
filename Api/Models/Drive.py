import json
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

class GoogleDrive:

    CREDS           = None
    SERVICE         = None
    KEY             = "E:/Proyectos/API-DRIVE/credentials.json"
    SCOPE           = ["https://www.googleapis.com/auth/drive"]

    def __init__(self):
        try:
            self.CREDS          = service_account.Credentials.from_service_account_file(self.KEY, scopes=self.SCOPE)
            self.SERVICE        = build("drive", "v3", credentials=self.CREDS)
        except Exception as e:
            print(e)
            exit(1)

    def getFileJson(self, id):
        try:
            request                 = self.SERVICE.files().get_media(fileId = id)
            file                    = io.BytesIO()
            downloader              = MediaIoBaseDownload(file, request)
            done                    = False
            while done is False:
                status, done = downloader.next_chunk()
            return json.loads(file.getvalue().decode("utf8").replace("'", '"'))
        except Exception as e:
            print(e)
            exit(1)
