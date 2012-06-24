#!/usr/bin/env python
#-*- coding: utf-8 -*-
import cherrypy
from jinja2 import Environment, FileSystemLoader
from app.models import Thing

env = Environment(loader=FileSystemLoader('app/views'))

class ThingsController(object):
  @cherrypy.expose
  def index(self):
    things = [{'id':1,'title' : 'Cherrypy'},{'id':2,'title' : "Django"},{'id':3,'title' : "Webpy"}]
    view = env.get_template('things/index.html')
    return view.render(things = things)

  @cherrypy.expose
  def new(self):
    view = env.get_template('things/new.html')
    return view.render(thing = None)

  @cherrypy.expose
  def edit(self, id=None):
    thing = Thing()
    thing.id = 1
    thing.title = 'teste'
    view = env.get_template('things/edit.html')
    return view.render(id = thing.id, thing = thing)

  @cherrypy.expose
  def update(id=None, title=None):
    raise cherrypy.HTTPRedirect("/index")

  @cherrypy.expose
  def destroy(self, id=None):
     raise cherrypy.HTTPRedirect("/index")

  @cherrypy.expose
  def show(self,id=None):
    thing = {'id':id,'title' : "Cherrypy"}
    view = env.get_template('things/show.html')
    return view.render(thing=thing)

  @cherrypy.expose
  def create(self, title=None):
    things = [{'title' : title}]
    view = env.get_template('things/index.html')
    return view.render(things = things)

  @cherrypy.expose
  def search(self, title=None):
    view = env.get_template('things/index.html')
    return view.render()
