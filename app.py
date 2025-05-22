from flask import flask
import random

app = Flask(__name__)

quotes = [
      "zycie to nie bajka kiedy musisz pisac skrypty"
      "php to rak..."
      "nienawidze informatyki"
]

@app.route('/')
def hello():
    return random.choice(quotes)
    
if __name__ == '__main__':
    app.run()
