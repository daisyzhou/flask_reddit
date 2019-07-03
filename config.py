#!/usr/bin/env python2.7
"""
app_config.py will be storing all the module configs.
Here the db uses mysql.
"""

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['your_email_here@email.com'])
SECRET_KEY = os.environ.get('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
DATABASE_CONNECT_OPTIONS = {}

CSRF_ENABLED = True
CSRF_SESSION_KEY = ""

BRAND = "/r/CLANCYCOIN"
DOMAIN = "YOUR_DOMAIN_HERE"
ROOT_URL = "http://reddit.clancycoin..com"

STATIC_ROOT = "{}/flask_reddit".format(_basedir)
STATIC_URL = ROOT_URL + "/static/"
PROPAGATE_EXCEPTIONS = True
