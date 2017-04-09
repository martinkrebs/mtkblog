# -*- coding: utf-8 -*-
from .base import *


DEBUG = False

ALLOWED_HOSTS = [
    'www.martintkrebs.com',
    'martintkrebs.com',
]

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
