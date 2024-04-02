# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
from flask                                                  import Flask
from flask_cors                                             import CORS

from api.routes.GoogleSheet                                 import google_sheet
from api.routes.GoogleDrive                                 import google_drive
# APP ============================================================================================================================
app                                                         = Flask(__name__)
# app.json.sort_keys                                          = False

CORS(app)

app.register_blueprint(google_sheet)
app.register_blueprint(google_drive)

if __name__ == "__main__": 
    app.run(debug = True)


    