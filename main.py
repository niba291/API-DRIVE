# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
from flask                                                  import Flask
from flask_cors                                             import CORS

from api.routes.GoogleSheet                                 import google_sheet
# APP ============================================================================================================================
app                                                         = Flask(__name__)
# app.json.sort_keys                                          = False

CORS(app)

app.register_blueprint(google_sheet)

if __name__ == "__main__": 
    app.run(debug = True)


    