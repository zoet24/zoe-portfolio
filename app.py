import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("pages/index/index.html")


@app.route("/projects")
def projects():
    return render_template("pages/projects/projects_all/projects_all.html")


@app.route("/contact")
def contact():
    return render_template("pages/contact/contact.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
