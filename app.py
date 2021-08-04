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

keywords = mongo.db.keywords
keywords_all = list(keywords.find())
languages = mongo.db.languages
languages_all = list(languages.find())
projects = mongo.db.projects
projects_all = list(projects.find())


@app.route("/")
def index():
    return render_template("pages/index/index.html",
                           languages = languages_all,
                           projects = projects_all)


@app.route("/portfolio")
def portfolio():
    return render_template("pages/projects/projects_all/projects_all.html",
                           keywords = keywords_all,
                           languages = languages_all,
                           projects = projects_all)


@app.route("/portfolio/<project_url_slug>")
def portfolio_project(project_url_slug):
    project = projects.find_one({"url_slug": project_url_slug})

    return render_template("pages/projects/projects_single/projects_single.html",
                           projects = projects_all,
                           project = project)


@app.route("/portfolio_search", methods=["GET", "POST"])
def portfolio_search():
    query = request.form.get("query")
    query_split = query.split('&')

    print(query)
    print(query_split)
    # query_search = query_split[0]
    # query_keywords = query_split[1]
    # query_languages = query_split[2]

    # print(query_keywords)
    # print(query_languages)

    projects_search = list(projects.find({"$text": {"$search": f"\"{query}\""}}))

    return render_template("pages/projects/projects_all/projects_all.html",
                           keywords = keywords_all,
                           languages = languages_all,
                           projects = projects_search)


@app.route("/contact")
def contact():
    return render_template("pages/contact/contact.html",
                           projects = projects_all)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
