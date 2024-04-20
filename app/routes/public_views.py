from flask import render_template, request
from . import public_route

@public_route.get('/')
def index():
  return render_template('index.html', title="Flask App")
#   return render_template(public_route.index, name="", title="Flask App")

@public_route.get("/about")
def about():
  return render_template("about.html", title="About")


# # escaping to prevent xss
# # @route.get('/<name>')
# # def username(name):
# #   return f'Hello, {escape(name)}!'


# # variable rules with <converterType:var_name>
# # converter types: int, string, float, path, uuid
@public_route.get("/user")
def user():
    return render_template("user.html", title="User")


@public_route.get("/user/<uuid:id>")
def user_id(id):
    return f"User ID: {id}"


@public_route.get("/login")
def login():
  return render_template("form.html", title="Login")


# @public_route.post("/login")
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

