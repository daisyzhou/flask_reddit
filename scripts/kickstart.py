#!/usr/bin/env python2.7
"""
This script instantiates critical components of our webapps.
We need at least one home subreddit to get things going.
We also need a first user to admin our first subreddit.
"""
import os
import sys
import readline
from pprint import pprint

from flask import *
from werkzeug import check_password_hash, generate_password_hash

from flask_reddit import *
from flask_reddit.users.models import *
from flask_reddit.threads.models import *
from flask_reddit.subreddits.models import *

db.drop_all()
db.create_all()

first_user = User(username='root', email='daisy.zdx@gmail.com', \
        password=generate_password_hash('Yh9lfd0y8Byt'))

db.session.add(first_user)
db.session.commit()

clancycoin_subreddit = Subreddit(name='clancycoin', desc='ClancyCoin, the hottest new cryptocurrency!', admin_id=first_user.id)

db.session.add(clancycoin_subreddit)
db.session.commit()
