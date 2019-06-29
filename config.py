#!/usr/bin/env python2.7
"""
app_config.py will be storing all the module configs.
Here the db uses mysql.
"""

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['your_email_here@email.com'])
SECRET_KEY = ''

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
DATABASE_CONNECT_OPTIONS = {}

CSRF_ENABLED = True
CSRF_SESSION_KEY = ""

BRAND = "reddit"
DOMAIN = "YOUR_DOMAIN_HERE"
ROOT_URL = "http://YOUR_URL_HERE"

STATIC_ROOT = "/path/to/your/static/root/"
STATIC_URL = ROOT_URL + "/static/"
