#!/usr/bin/env python
#-*- coding: utf-8 -*-
import cherrypy
from quick_orm.core import Database
from jinja2 import Environment, FileSystemLoader
from app.models import Thing

env = Environment(loader=FileSystemLoader('app/views'))

class ThingsController(object):

  def __init__(self):
    self.db = Database('mysql://root:JcA0011@localhost/thing_development?charset=utf8')
    self.db.create_tables()
    #URL('firebird', 'SYSDBA', 'masterkey', '192.168.1.11', '3052', 'bdband')

  @cherrypy.expose
  def index(self):
    things = self.db.session.query(Thing)
    view = env.get_template('things/index.html')
    return view.render(things = things)

  @cherrypy.expose
  def new(self):
    view = env.get_template('things/new.html')
    return view.render(thing = None)

  @cherrypy.expose
  def edit(self, id=None):
    thing = self.db.session.query(Thing).get(id)
    view = env.get_template('things/edit.html')
    return view.render(id = thing.id, thing = thing)

  @cherrypy.expose
  def update(self, id=None, title=None, author=None, description=None):
    thing = Thing(id = id, title = title, author=author, description=description)
    self.db.session.merge(thing)
    #self.db.session.commit()
    raise cherrypy.HTTPRedirect("/index")

  @cherrypy.expose
  def destroy(self, id=None):
    thing = self.db.session.query(Thing).get(id)
    self.db.session.delete_then_commit(thing)
    raise cherrypy.HTTPRedirect("/index")

  @cherrypy.expose
  def show(self,id=None):
    thing = self.db.session.query(Thing).get(id)
    view = env.get_template('things/show.html')
    return view.render(thing=thing)

  @cherrypy.expose
  def create(self, id=None, title=None, author=None, description=None):
    thing = Thing(title = title, author = author, description = description)
    self.db.session.add_then_commit(thing)
    raise cherrypy.HTTPRedirect("/index")

  @cherrypy.expose
  def search(self, title=None):
    if (not title):
      things = self.db.session.query(Thing)
    else:
      things = self.db.session.query(Thing).filter_by(title = title)

    view = env.get_template('things/index.html')
    return view.render(things = things)
