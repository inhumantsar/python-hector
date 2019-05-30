import logging
import os

"""Defines module level constants using ENV vars and defaults."""

LOG_LEVEL = logging.getLevelName(os.environ.get('HECTOR_LOG_LEVEL', 'INFO'))

SLACK_WEBHOOK = os.environ.get('SLACK_WEBHOOK')

OAUTH2_CLIENT_ID = os.environ.get('OAUTH2_CLIENT_ID', '99487ef605fe914cf0c8a42fcf61d7a9b013f86591e7e23abf542ba17f8208ba')
OAUTH2_CLIENT_SECRET = os.environ.get('OAUTH2_CLIENT_SECRET', 'fefdb04cbecb298580fa113ed8c50cdf2967a97997a57057d0f251797ca39244')
OAUTH2_REDIRECT_URL = os.environ.get('OAUTH2_REDIRECT_URL', 'http://local.wlnpcc.ca/login/gitlab/authorized')
OAUTH2_APP_NAME = os.environ.get('OAUTH2_APP_NAME', 'gitlab')
OAUTH2_BASE_URL = os.environ.get('OAUTH2_BASE_URL', 'gitlab.com')
OAUTH2_TOKEN_URL = os.environ.get('OAUTH2_TOKEN_URL', f"{OAUTH2_BASE_URL}/oauth/token")
OAUTH2_AUTHORIZE_URL = os.environ.get('OAUTH2_AUTHORIZE_URL', f"{OAUTH2_BASE_URL}/oauth/authorize")     