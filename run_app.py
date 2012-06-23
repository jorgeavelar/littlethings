#-*- coding: utf-8 -*-
import cherrypy

#from controllers.articles_controller import ArticlesController
from controllers import ThingsController

conf = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8000,
    }
}

cherrypy.quickstart(ThingsController(), '/', conf)
