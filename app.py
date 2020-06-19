"""A web app displaying various restaurants and their menus.

Usage: flask run
"""

from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
