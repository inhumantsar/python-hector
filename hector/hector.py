# -*- coding: utf-8 -*-

"""Hector watches for GitLab Merge Requests and nags people about the ones that go stale."""

import logging
import os
import time

from datetime import timedelta
from datetime import datetime

from flask import Flask, redirect, url_for, session, request, jsonify
from flask_dance.contrib.gitlab import make_gitlab_blueprint, gitlab

from hector import config

app = Flask(__name__)

# set up logging and log levels
app.debug = True if config.LOG_LEVEL == logging.DEBUG else False
handler = logging.StreamHandler()
handler.setLevel(config.LOG_LEVEL)
app.logger.handler = handler

# set up gitlab oauth
app.secret_key = 'mootoothree'
blueprint = make_gitlab_blueprint(
    client_id=config.OAUTH2_CLIENT_ID,
    client_secret=config.OAUTH2_CLIENT_SECRET,
    redirect_url=config.OAUTH2_REDIRECT_URL,
    hostname=config.OAUTH2_BASE_URL
)
app.register_blueprint(blueprint, url_prefix="/login")

merge_requests = None

@app.route('/')
def index():
    if not gitlab.authorized:
        return redirect(url_for("gitlab.login"))

    if not merge_requests:
        return redirect(url_for("start_watcher"))

    return """
<html>
<head>
    <meta http-equiv="refresh" content="30">
<head>
<body>
Merge Requests:
<pre>
{merge_requests}
</pre>
</body>
</html>
"""

@app.route('/start_watcher')
def start_watcher():
    if not gitlab.authorized:
        return redirect(url_for("gitlab.login"))
    while True:
        created_before = datetime.now() - timedelta(days=1)
        resp = gitlab.get("/api/v4/merge_requests?state=opened")
        assert resp.ok
        merge_requests = resp.json()
        print(f"updated mrs: {merge_requests}")
        time.sleep(1)
    # return redirect(url_for("index"))
    # return f"You are {resp.json()['username']} on GitLab"



if __name__ == '__main__':    
    app.run(threaded=1)