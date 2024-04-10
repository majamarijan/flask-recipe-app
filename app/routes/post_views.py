from flask import render_template, make_response, url_for
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
    postList = getPosts(requests, "https://dummyjson.com/recipes", "?limit=10").get(
        "recipes"
    )

    if not os.path.isdir("app/static/images/thumbnails"):
        os.mkdir('app/static/images/thumbnails')
    
    imgFiles = os.listdir("app/static/images/")
    
    # for img in imgFiles:
    #     if img.split(".")[-1] != 'thumbnails':
    #         os.remove("app/static/images/" + img)
        
    for post in postList:
        url = post.get("image")
        img_name = url.split("/")[-1]
        image = urlopen(url)
        img = Image.open(image)
        img.thumbnail((320, 320))
        img.save("app/static/images/thumbnails/" + img_name)
        
        post.update({"thumbnail": img_name})
    
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
    