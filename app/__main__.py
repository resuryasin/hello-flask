"""This is the main module of the app"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index() -> str:
    """This is the index route"""
    return 'Hello World'

if __name__ == '__main__':
    app.run()
