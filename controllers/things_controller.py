#-*- coding: utf-8 -*-
import cherrypy
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('views'))

class ThingsController(object):
  @cherrypy.expose
  def index(self):
      things = [{'title' : "Cherrypy"},{'title' : "Django"},{'title' : "Webpy"}]
      view = env.get_template('things/index.html')
      return view.render(things = things)

  @cherrypy.expose
  def new(self):
      view = env.get_template('things/new.html')
      return view.render()

  @cherrypy.expose
  def edit(self):
      view = env.get_template('things/edit.html')
      return view.render()

  @cherrypy.expose
  def destroy(self):
      view = env.get_template('things/index.html')
      return view.render()

  @cherrypy.expose
  def show(self):
      view = env.get_template('things/show.html')
      return view.render()

  @cherrypy.expose
  def create(self):
      view = env.get_template('things/index.html')
      return view.render()

  @cherrypy.expose
  def search(self):
      view = env.get_template('things/index.html')
      return view.render()
