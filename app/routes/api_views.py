import requests
import json
from . import apiBp
from flask import jsonify, url_for
from app.modules.posts import getPosts
from PIL import Image
from urllib.request import urlopen
import base64
import os
from app.mainCache import cache

@apiBp.get("/posts")
def posts():
  postList = getPosts(requests, "https://dummyjson.com/recipes", "?limit=10").get("recipes")
  
  if not os.path.isdir("app/static/images/thumbnails"):
    os.mkdir('app/static/images/thumbnails')
    
  imgFiles = os.listdir("app/static/images/thumbnails")
  print(len(imgFiles))
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
      
      im = Image.open("app/static/images/thumbnails/" + img_name)
      # update post with thumbnail
      post.update({"thumbnail": img_name})
    
  return jsonify(postList)
  