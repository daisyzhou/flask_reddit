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

first_user = User.query.filter_by(email='daisy.zdx@gmail.com').first()

clancycoin_subreddit = Subreddit.query.filter_by(name='clancycoin').first()
pinned_thread = Thread(title='Subreddit Rules', text='jk no rules here', link=None, user_id=first_user.id, subreddit_id=clancycoin_subreddit.id)

db.session.add(pinned_thread)
db.session.commit()
