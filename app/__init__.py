#!/usr/bin/env python

from flask import Flask, url_for, request, jsonify, redirect, render_template, make_response
from markupsafe import escape
import mimetypes
mimetypes.add_type('image/svg+xml', '.svg')
from dotenv import dotenv_values
import sys
import time
import logging
import os


PORT = int(os.environ.get("PORT", 5000))
# load_dotenv()  # take environment variables from .env.
config = dotenv_values(".env")
# print(config.get("DOMAIN_URL"))

# make application factory
# this file __init__.py contains the application factory and tells that the app folder is a package

def create_app():
  # instance_relative_config=True: load config from instance folder
  app = Flask(__name__, instance_relative_config=True)

  # add routes
  from .routes import public_views, post_views
 
  app.register_blueprint(public_views.public_route)
  app.add_url_rule("/", endpoint="index")
  app.add_url_rule("/about", endpoint="about")
  app.add_url_rule('/user', endpoint='user')
  app.add_url_rule('/login', endpoint='login')

  app.register_blueprint(post_views.postBp, url_prefix='/posts')
  app.add_url_rule('/', endpoint='posts')
  app.add_url_rule('/post/<int:post_id>', endpoint='post')

  @app.errorhandler(404)
  def not_found(error):
    return render_template("error.html", error=error), 404

  if __name__ == "__main__":
    app.run(port=PORT, debug=True)


  return app
  
    