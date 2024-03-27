from flask import render_template, make_response, url_for
from app.modules.posts import getPosts, getPost, getAuthor
import requests
import json
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
    post_author = ''
    if(single_post):
        post_author = getAuthor(requests, "https://dummyjson.com/users/", str(single_post.get("userId")))
    return render_template("post.html", title="Post", post=single_post, author=post_author)
    