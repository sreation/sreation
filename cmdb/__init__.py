# -*- coding: utf-8 -*-
import os


def load_config():
    """load config by environ"""
    # mode = os.environ.get('MODE')
    mode = 'deploy'
    try:
        if mode == 'product':
            from config import ProductConfig
            return ProductConfig
        elif mode == 'deploy':
            from config import DeployConfig
            return DeployConfig

    except ImportError, e:
        from config import DefaultConfig
        return DefaultConfig
