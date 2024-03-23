#!/usr/bin/env python

from flask import Flask, url_for, request, jsonify, redirect, render_template, make_response, flash
from markupsafe import escape
import mimetypes
import json
import requests
from .modules.usersList import addUser
from .modules.posts import getPosts, getPost

mimetypes.add_type('image/svg+xml', '.svg')

users= []
app = Flask(__name__)


@app.get('/')
def index():
  return render_template('index.html', name='', title='Flask App' )

@app.get('/about')
def about():
  print(__name__)
  return render_template('about.html', title='About')

# escaping to prevent xss
# @app.get('/<name>')
# def username(name):
#   return f'Hello, {escape(name)}!'

# variable rules with <converterType:var_name>
# converter types: int, string, float, path, uuid
@app.get('/user')
def user():
  return render_template('user.html', title='User')

@app.get('/user/<uuid:id>')
def user_id(id):
  return f'User ID: {id}'

@app.get('/posts')
def posts():
  postList = getPosts(requests, 'https://dummyjson.com/recipes', '?limit=10').get('recipes')
  # print(postList.get('recipes'))
  return render_template('posts.html', title='Posts', posts=postList)

@app.get('/post/<int:post_id>')
def get_post(post_id):
  single_post = getPost(requests, 'https://dummyjson.com/recipes/', str(post_id))
  return render_template('post.html', title='Post', post=single_post)


@app.get('/login')
def login():
  return render_template('form.html', title='Login')

@app.post('/login')
def login_action():
  addUser(request.get_json(), users)
  print(users)
  if(request.is_json):
    with open('data/db.json', 'w') as file:
      file.writelines(json.dumps(users))
      # file.write(str(request.data).replace('b\'', '').replace('\'', ''))
    # flash('You were successfully logged in')
    return redirect(url_for('index'))
  return redirect(url_for('index'), code=302, Response=None)
  


@app.errorhandler(404)
def not_found(error):
  return render_template('error.html', error=error), 404


# building urls for the templates
with app.test_request_context():
  url_for('static', filename='style.css')
  url_for('index', filename='index.html')
  print(url_for('about'))
  print(url_for('user_id', id='550e8400-e29b-41d4-a716-446655440000'))
  