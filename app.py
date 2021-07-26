import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

projects = mongo.db.projects


@app.route("/")
def index():
    return render_template("pages/index/index.html")


@app.route("/portfolio")
def portfolio():
    projects_all = list(projects.find())
    return render_template("pages/projects/projects_all/projects_all.html",
                           projects = projects_all)


@app.route("/portfolio/<project_url_slug>")
def portfolio_project(project_url_slug):
    project = projects.find_one({"url_slug": project_url_slug})
    print(project_url_slug)

    return render_template("pages/projects/projects_single/projects_single.html",
                           project = project)


@app.route("/contact")
def contact():
    return render_template("pages/contact/contact.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
