#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timezone
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_folder="public", template_folder="views")

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/api/hello")
def hello():
    return jsonify(greeting="hello API")

@app.route("/api/whoami")
def whoami():
    return jsonify(ipaddress=request.access_route[-1],
                   language=str(request.accept_languages),
                   software=str(request.user_agent))
        
if __name__ == "__main__":
    app.run()
