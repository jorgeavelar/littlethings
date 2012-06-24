#!/usr/bin/env python
#-*- coding: utf-8 -*-
from quick_orm.core import Database
from sqlalchemy import Column, String

__metaclass__ = Database.DefaultMeta

class Thing(object):
    __metaclass__ = Database.DefaultMeta
    title = Column(String(30))

Database.register()
