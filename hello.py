
from flask import Flask

app = Flask(__name__)

@app.route("/newpath")
def new_route():
    return "Hello, World!"