#!/usr/bin/env python
#-*- coding: utf-8 -*-
from quick_orm.core import Database
from sqlalchemy import Column, String, Text

__metaclass__ = Database.DefaultMeta

class Thing(object):
    __metaclass__ = Database.DefaultMeta
    title = Column(String(80))
    description = Column(Text())
    author = Column(String(120))


Database.register()
