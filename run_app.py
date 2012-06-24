#!/usr/bin/env python
#-*- coding: utf-8 -*-
import cherrypy

from app import *

conf = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8000,
    }
}

cherrypy.quickstart(ThingsController(), '/', conf)
