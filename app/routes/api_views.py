import requests
import json
from . import apiBp
from flask import jsonify, url_for
from app.modules.posts import getPosts
from PIL import Image
from urllib.request import urlopen
import base64
import io

@apiBp.get("/posts")
def posts():
  postList = getPosts(requests, "https://dummyjson.com/recipes", "?limit=10").get(
        "recipes"
  )
  for post in postList:
      url = post.get("image")
      img_name = url.split("/")[-1]
      image = urlopen(url)
      img = Image.open(image)
      img.thumbnail((320, 320))
      img.save("app/static/images/thumbnails/" + img_name)
      
      im = Image.open("app/static/images/thumbnails/" + img_name)
      # update post with thumbnail
      post.update({"thumbnail": url_for('static', filename='images/thumbnails/' + img_name)})
    
  return jsonify(postList)