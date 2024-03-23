def getPosts(requests, url, q):
  res=requests.get(url+q)
  return res.json()


def getPost(requests, url, id):
  res=requests.get(url+id)
  return res.json()