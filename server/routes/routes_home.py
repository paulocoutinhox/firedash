import os

from flask import render_template, Blueprint, send_from_directory, current_app

from config.data import config_data

routes_home = Blueprint("home", __name__)


@routes_home.route("/", defaults={"path": ""})
@routes_home.route("/<path:path>")
def action_catch_all(path):
    if config_data["web_cli_enabled"]:
        return render_template("index.html")
    else:
        return """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Firedash</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.5/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
  </head>
  <body>
  <section class="section">
    <div class="container has-text-centered">
      <p>
        <img src="https://github.com/prsolucoes/firedash/blob/master/extras/images/logo.png?raw=true" title="Firedash" style="width: 100px">
      </p>
      <h1 class="title">
        Firedash
      </h1>
      <p class="subtitle">
        Dashboards for general purposes with batteries included
      </p>      
    </div>
  </section>
  </body>
</html>
        """


@routes_home.route("/favicon.ico")
def action_favicon():
    return send_from_directory(
        os.path.join(current_app.root_path, "..", "..", "web-cli", "dist", "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )
