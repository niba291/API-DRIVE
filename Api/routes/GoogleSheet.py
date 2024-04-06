# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
from utils.env                              import ENV
from utils.status                           import HTTP_200_OK, HTTP_400_BAD_REQUEST
from flask                                  import Blueprint, jsonify, request
from GoogleNb.GoogleSheet                   import GoogleSheet
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

@google_sheet.route("/googlesheet/get/<string:id>/<string:rangeSheet>", methods = ["GET"])
def google_sheet_get(rangeSheet = "", id = "") -> dict:
    """
        Return data google sheet
        Return      : dict
    """
    response            = GoogleSheet(ENV["PATH_CREDENTIALS"]).get(
        spreadsheetId   = id, 
        ranges          = rangeSheet.split(";")
    )
    return jsonify(response), HTTP_200_OK if not ("error" in response) else HTTP_400_BAD_REQUEST
    
@google_sheet.route("/googlesheet/add", methods = ["POST"])
def google_sheet_add() -> dict:
    """
        Add element in sheet
        Return      : dict
    """
    response            = GoogleSheet(ENV["PATH_CREDENTIALS"]).add(
        spreadsheetId   = request.json["id"], 
        range           = request.json["range"],
        data            = request.json["data"]
    ) 
    return jsonify(response), HTTP_200_OK if not ("error" in response) else HTTP_400_BAD_REQUEST

@google_sheet.route("/googlesheet/update", methods = ["PUT"])
def google_sheet_update() -> dict:
    """
        Update element in sheet
        Return      : dict
    """
    response            = GoogleSheet(ENV["PATH_CREDENTIALS"]).update(
        spreadsheetId   = request.json["id"], 
        range           = request.json["range"],
        data            = request.json["data"]
    )
    return jsonify(response), HTTP_200_OK if not ("error" in response) else HTTP_400_BAD_REQUEST

@google_sheet.route("/googlesheet/delete/<string:id>/<string:range>/<string:idSheet>", methods = ["DELETE"])
def google_sheet_delete(range = "", id = "", idSheet = "") -> dict:
    """
        Delete element in sheet
        Return      : dict
    """
    response            = GoogleSheet(ENV["PATH_CREDENTIALS"]).delete(
        spreadsheetId   = id, 
        range           = range,
        idSheet         = idSheet
    )
    return jsonify(response), HTTP_200_OK if not ("error" in response) else HTTP_400_BAD_REQUEST

# @google_sheet.route("/googlesheet/formating/<string:id>", methods = ["GET"])
# def google_sheet_formating(id = "") -> dict:
#     """
#         Delete element in sheet
#         Return      : dict
#     """
#     response            = GoogleSheet(ENV["PATH_CREDENTIALS"]).conditional_formatting(
#         spreadsheetId   = id, 
#     )
#     return jsonify(response), HTTP_200_OK if not ("error" in response) else HTTP_400_BAD_REQUEST