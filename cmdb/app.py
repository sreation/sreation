# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))
from flask import Flask, render_template
from sreation.cmdb import load_config
from main.main import bp_main


def create_app(config_filename, bp_init, prefix=''):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    if not isinstance(bp_init, list):
        bp_init = [bp_init]

    for bp in bp_init:
        app.register_blueprint(bp, url_prefix=prefix)
    return app

if __name__ == '__main__':
    my_app = create_app(load_config(), bp_main, '/main')
    my_app.run(**{
            'host': '127.0.0.1',
            'port': 5000,
            'debug': True
    })

