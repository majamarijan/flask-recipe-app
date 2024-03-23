from flask import Blueprint

postBp = Blueprint("posts", __name__, template_folder="templates", static_folder="static")