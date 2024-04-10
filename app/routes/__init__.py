from flask import Blueprint

# __name__ is the name of the current module
public_route = Blueprint("public", __name__, template_folder="templates", static_folder="static")
postBp = Blueprint("posts", __name__, template_folder="templates", static_folder="static")
apiBp = Blueprint("api", __name__, template_folder="templates", static_folder="static")