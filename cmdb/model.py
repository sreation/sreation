# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Entries(Base):
    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    text = Column(String(255))
