# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
from flask                                  import Blueprint, jsonify, request
from api.models.GoogleSheet                 import GoogleSheet
# BLUEPRINT =====================================================================================================================
google_sheet                                = Blueprint("google_sheet", __name__)
# ROUTE =========================================================================================================================
# def google_sheet_middleware() -> dict or None:
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

@google_sheet.route("/googlesheet/get", methods = ["POST"])
def google_sheet_get() -> dict:
    """
        Return data google sheet
        Return      : dict
    """
    return jsonify(GoogleSheet(request.json["spreadsheetId"], request.json["range"]).get([request.json["filter"]] if "filter" in request.json else None))

@google_sheet.route("/googlesheet/add", methods = ["POST"])
def google_sheet_add() -> dict:
    """
        Add element in sheet
        Return      : dict
    """
    return jsonify(GoogleSheet(request.json["spreadsheetId"], request.json["range"]).add(request.json["data"]))

@google_sheet.route("/googlesheet/update", methods = ["POST"])
def google_sheet_update() -> dict:
    """
        Update element in sheet
        Return      : dict
    """
    return jsonify(GoogleSheet(request.json["spreadsheetId"], request.json["range"]).update(request.json["data"]))

@google_sheet.route("/googlesheet/delete", methods = ["POST"])
def google_sheet_delete() -> dict:
    """
        Delete element in sheet
        Return      : dict
    """    
    return jsonify(GoogleSheet(request.json["spreadsheetId"], request.json["range"]).delete(request.json["data"]))