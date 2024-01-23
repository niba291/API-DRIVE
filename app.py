# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
from flask                                                  import Flask
from flask_cors                                             import CORS
# APP ============================================================================================================================
app                                                         = Flask(__name__)
app.json.sort_keys                                          = False

CORS(app)

if __name__ == "__name__": 
    app.run(debug = True)


    