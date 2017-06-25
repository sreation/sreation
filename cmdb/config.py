# -*- coding: utf-8 -*-


class Config(object):
    DEBUG = False


class DefaultConfig(Config):
    pass


class ProductConfig(Config):
    pass


class DeployConfig(Config):
    DEBUG = True
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
