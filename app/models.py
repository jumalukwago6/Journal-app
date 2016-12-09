import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

Base =declarative_base()
Base.create_all();
class User(Base):
	__tablename__='users'
	id = Column(Integer, primary_key=True)
	username = Column(String(64), unique=True, index=True)
	firstname= Column(String(64))
	lastname= Column(String(64))
	password=Column(String(64))

    
class Journal(Base):
    '''
    Creates a table model that will store all the journals of the users grouped by username
    Date, body, tags
    '''
    __tablename__ = 'journal'

    id = Column(Integer, primary_key=True)
    date_created = Column(DateTime, nullable = False, default=datetime.datetime.utcnow)
    updated_on = Column(DateTime)
    body = Column(String(1500), nullable=False)
    tags = Column(String(50), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    jour = relationship('User')


    def __init__(self, body, tags, user_id):
        self.body = body
        self.tags = tags
        self.user_id = user_id


    def __repr__(self):
        return '<Journal %r>' % self.body

engine = create_engine("sqlite:///database.db")
Base.metadata.create_all(engine) # Creates the tables using the connection engine