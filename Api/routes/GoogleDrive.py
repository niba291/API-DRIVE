# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
from utils.env                              import ENV
from json                                   import loads
from flask                                  import Blueprint, jsonify, request
from GoogleNb.GoogleDrive                   import GoogleDrive
# BLUEPRINT =====================================================================================================================
google_drive                                = Blueprint("google_drive", __name__)
# ROUTE =========================================================================================================================
# def google_drive_middleware() -> dict or None:
#     if "Authorization" not in request.headers:
#         return jsonify({
#             "error"     : True,
#             "response"  : "Not exist 'Authorization' element in header"
#         })

#     token               = Token().check(request.headers["Authorization"].replace("Bearer ", ""), {
#         "module"        : User().module
#     })

#     if token["error"]:
#         return jsonify(token), 401

@google_drive.route("/googledrive/getfile/<string:id>", methods = ["GET"])
def google_drive_get_file(id = "") -> dict:
    """
        Return data google drive
        Return      : dict
    """    
    return jsonify(loads(GoogleDrive(ENV["PATH_CREDENTIALS"]).getFile(id).decode("utf8")))