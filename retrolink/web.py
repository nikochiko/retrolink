from . import rl

import requests
from flask import Flask, request
from kutty import html
from kutty.bootstrap import Layout, Page


app = Flask(__name__)
layout = Layout("retrolink")


@app.route("/", methods=["GET"])
def index():
    if "url" in request.args:
        url = request.args["url"]
        r = requests.get(url)
        r.raise_for_status()
        return rl.fix_html(r.text, url=url)
    else:
        page = Page("")
        page << html.h1("retrolink", class_="mt-3"),
        page << html.tag(
            "form",
            html.div(
                html.input("URL", name="url", type_="text").add_class("form-control mb-3"),
                html.button("Submit", type_="submit").add_class("btn btn-primary"),
                class_="form-group",
            ),
        )
        return layout.render_page(page)
