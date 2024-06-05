from flask import Flask, url_for

app = Flask(__name__)

from app import routes

if __name__ == '__main__':
    app.run(debug=True)