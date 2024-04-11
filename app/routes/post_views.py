from flask import render_template, make_response, url_for, request, jsonify
from app.modules.posts import getPosts, getPost, getAuthor
import requests
import json
from . import postBp
from urllib.request import urlopen
from PIL import Image
import os, sys
import base64

@postBp.get("/")
def posts():
    return render_template("posts.html", title="Posts")

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
    