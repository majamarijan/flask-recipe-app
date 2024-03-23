@app.route('/<name>')
def username(name):
  return f'Hello, {escape(name)}!'