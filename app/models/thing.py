#!/usr/bin/env python
#-*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, Text

Base = declarative_base()

class Thing(Base):
    __tablename__ = 'things'
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    description = Column(Text())
    author = Column(String(120))
