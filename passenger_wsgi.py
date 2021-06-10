# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, '/var/www/u0480764/data/www/mnemchinov.ru/orders')
sys.path.insert(1, '/var/www/u0480764/data/venv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'orders.settings'
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
