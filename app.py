# -*- coding: utf-8 -*-

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/1006")
def hello():
    return "1006 homepage"

#start the server
if __name__ == "__main__":
    app.run()