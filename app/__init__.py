from flask import Flask
from app.bp import bp

app = Flask(__name__)
app.register_blueprint(bp)


@app.route("/")
def hello_world():
    return "Hello, World!"

