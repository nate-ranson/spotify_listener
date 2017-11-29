#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/spotify/")

from spotify import app as application
application.secret_key = 'Pogi#The#Pup123'

