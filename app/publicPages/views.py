from flask import render_template
import requests
import json
from app.modules.posts import getPosts, getPost
from . import public_pages

@public_pages.get('/')
def index():
  return render_template('layout.html', name="", title="Flask App")
#   return render_template(public_pages.index, name="", title="Flask App")

@public_pages.get("/about")
def about():
  return render_template("about.html", title="About")


# # escaping to prevent xss
# # @view_pages.get('/<name>')
# # def username(name):
# #   return f'Hello, {escape(name)}!'


# # variable rules with <converterType:var_name>
# # converter types: int, string, float, path, uuid
@public_pages.get("/user")
def user():
    return render_template("user.html", title="User")


# @public_pages.get("/user/<uuid:id>")
# def user_id(id):
#     return f"User ID: {id}"


@public_pages.get("/login")
def login():
  return render_template("form.html", title="Login")


# @public_pages.post("/login")
# def login_action():
#     addUser(request.get_json(), users)
#     print(users)
#     if request.is_json:
#         with open("data/db.json", "w") as file:
#             file.writelines(json.dumps(users))
#             # file.write(str(request.data).replace('b\'', '').replace('\'', ''))
#         # flash('You were successfully logged in')
#         return redirect(url_for("index"))
#     return redirect(url_for("index"), code=302, Response=None)




# building urls for the templates

#     print(url_for('about'))
#     print(url_for('user_id', id='550e8400-e29b-41d4-a716-446655440000'))
