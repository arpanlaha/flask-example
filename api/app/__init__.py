from flask import Flask, send_from_directory
from app.bp import bp

app = Flask(__name__, static_url_path="")
app.register_blueprint(bp)


@app.route("/")
def root():
    return app.send_static_file("index.html")


@app.route("/<path:path>")
def send_cra(path):
    print("Hello")
    return send_from_directory("static", path)

