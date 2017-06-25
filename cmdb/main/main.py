# -*- coding: utf-8 -*-
import sys
from flask import Blueprint, url_for, \
    render_template, request, flash, redirect, current_app, app
from sreation.cmdb import load_config
from sreation.cmdb.model import Entries
from sreation.common.db.dbo import Dbo

bp_main = Blueprint(
    'main',
    __name__,
    template_folder='./template',
)

my_cfg = load_config()
db_dinggo = Dbo('dinggo', my_cfg.__dict__)
dinggo_s = db_dinggo.get_session()


@bp_main.route('/', methods=['GET'])
def index():
    print dinggo_s.query(Entries).filter().all()
    return '<h1>Hello dinggo cm2db!</h1>'
