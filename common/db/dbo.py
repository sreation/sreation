# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class Dbo(object):
    engine = None
    db_session = None
    base = None

    def __init__(self, db_name, config_dict):
        self.engine = create_engine("mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8".format(
            config_dict['MYSQL_USER'],
            config_dict['MYSQL_PASSWORD'],
            config_dict['MYSQL_HOST'],
            config_dict['MYSQL_PORT'],
            db_name
        ), encoding="utf-8", echo=config_dict['DEBUG'])

        self.db_session = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )()

    def get_session(self):
        return self.db_session
