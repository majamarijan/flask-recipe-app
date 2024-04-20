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
from datetime import datetime
from app.mainCache import cache

PORT = int(os.environ.get("PORT", 5000))
# load_dotenv()  # take environment variables from .env.
config = dotenv_values(".env")
# print(config.get("DOMAIN_URL"))
CACHE_CONFIG = {
  "CACHE_TYPE": "SimpleCache",
  "CACHE_DEFAULT_TIMEOUT": 5,
  "DEBUG": True
}
# make application factory
# this file __init__.py contains the application factory and tells that the app folder is a package

def create_app():
  # instance_relative_config=True: load config from instance folder
  app = Flask(__name__, instance_relative_config=True)
  cache.init_app(app, config=CACHE_CONFIG)
  with app.app_context():
    # set headers
    @app.after_request
    def set_response_headers(response):
      # register domain on https://hstspreload.org/ to prevent third party attacks and ensure https ; the list of domains that will browser download to use https
      response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
      response.headers['Access-Control-Allow-Origin'] = 'same-origin'
      response.headers['Content-Security-Policy'] = "default-src 'self' cdnjs.cloudflare.com; font-src 'self' fonts.gstatic.com fonts.googleapis.com cdnjs.cloudflare.com; style-src 'self' fonts.googleapis.com cdnjs.cloudflare.com unpkg.com 'unsafe-inline'; script-src 'self' cdnjs.cloudflare.com esm.sh"
      response.headers['X-Content-Type-Options'] = 'nosniff'
      response.headers['X-Frame-Options'] = 'SAMEORIGIN'
      response.headers['X-XSS-Protection'] = '1; mode=block'
      response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
      return response
  # add routes
  from .routes import public_views, post_views, api_views
 
  app.register_blueprint(public_views.public_route)
  app.add_url_rule("/", endpoint="index")
  app.add_url_rule("/about", endpoint="about")
  app.add_url_rule('/user', endpoint='user')
  app.add_url_rule('/login', endpoint='login')
  

  app.register_blueprint(post_views.postBp, url_prefix='/posts')
  app.add_url_rule('/', endpoint='posts')
  app.add_url_rule('/post/<int:post_id>', endpoint='post')

  app.register_blueprint(api_views.apiBp, url_prefix='/api')
  app.add_url_rule('/', endpoint='api')


  @app.get('/timer')
  @cache.cached(timeout=10)
  def timer():
    return jsonify({'time': datetime.now()})
  
  @app.errorhandler(404)
  def not_found(error):
    return render_template("error.html", error=error), 404

  if __name__ == "__main__":
    app.run(port=PORT, debug=True)


  return app
  
    