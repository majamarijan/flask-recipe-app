from flask import render_template, make_response, url_for, request, jsonify
from app.modules.posts import getPosts, getPost, getAuthor
import requests
import json
from . import postBp
from urllib.request import urlopen
from PIL import Image
import os, sys
import base64
from app.mainCache import cache

@postBp.get("/")
@cache.cached(timeout=120)
def posts():
    print(request.args)
    posts = requests.get('http://localhost:5000/api/posts').json()
    if not len(posts) == 0:
        cache.set("posts", posts)
    response = make_response(render_template("posts.html", title="Posts", posts=cache.get('posts')))
    response.headers['Cache-Control'] = 'public, max-age=300'
    response.et
    return response

@postBp.get("/list")
# name of the function should match the endpoint in the template
def listLink():
    return render_template('test.html')

@postBp.get("/post/<int:post_id>")
def get_post(post_id):
    single_post = getPost(requests, "https://dummyjson.com/recipes/", str(post_id))
    post_author = ''
    if(single_post):
        post_author = getAuthor(requests, "https://dummyjson.com/users/", str(single_post.get("userId")))
    return render_template("post.html", title="Post", post=single_post, author=post_author)
    