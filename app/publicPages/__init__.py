from flask import Blueprint


# __name__ is the name of the current module
public_pages = Blueprint("public", __name__, template_folder="templates", static_folder="static")