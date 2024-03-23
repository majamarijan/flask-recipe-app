from flask import render_template
import requests
import json
from app.modules.posts import getPosts, getPost
from . import postBp

@postBp.get("/")
def posts():
    postList = getPosts(requests, "https://dummyjson.com/recipes", "?limit=10").get(
        "recipes"
    )
    # print(postList.get('recipes'))
    return render_template("posts.html", title="Posts", posts=postList)

@postBp.get("/list")
# name of the function should match the endpoint in the template
def listLink():
    return render_template('test.html')

@postBp.get("/post/<int:post_id>")
def get_post(post_id):
    single_post = getPost(requests, "https://dummyjson.com/recipes/", str(post_id))
    return render_template("post.html", title="Post", post=single_post)