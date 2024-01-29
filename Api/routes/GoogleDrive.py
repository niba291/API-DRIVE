# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
from flask                                  import Blueprint, jsonify, request
from api.models.GoogleDrive                 import GoogleDrive
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

@google_drive.route("/googlesheet/get", methods = ["POST"])
def google_drive_get_file() -> dict:
    """
        Return data google sheet
        Return      : dict
    """
    return jsonify(GoogleDrive().getFile(request.json["idFile"]))