import os

from flask import render_template, Blueprint, send_from_directory, current_app

routes_home = Blueprint("home", __name__)


@routes_home.route("/", defaults={"path": ""})
@routes_home.route("/<path:path>")
def action_catch_all(path):
    return render_template("index.html")


@routes_home.route("/favicon.ico")
def action_favicon():
    return send_from_directory(
        os.path.join(current_app.root_path, "..", "..", "web-cli", "dist", "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )
