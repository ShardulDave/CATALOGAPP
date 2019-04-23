#!/usr/bin/env python3


from sqlalchemy import create_engine  
from sqlalchemy import Column, String, ForeignKey, Integer  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker, relationship

from database_setup import User, Category, Item

db_string = "postgres:///catalogdb"

db = create_engine(db_string)  
Base = declarative_base()

Session = sessionmaker(db)  
session = Session()

#Adding dummy data

user1=User(name='Shardul Dave',email='daveshardul@gmail.com',picture='https://www.facebook.com/photo.php?fbid=1890698061058107&set=a.103967993064465&type=3&theater')
session.add(user1)
session.commit()

category1=Category(name='Football',user_id=1)
session.add(category1)
session.commit()

item1=Item(name='Soccer',description='Played in the world',category_id=1,user_id=1)
session.add(item1)
session.commit()

#deleting the data
#cats=session.query(Item).filter_by(id=3).one()

#session.commit()

#looping through the data
#items=session.query(Item).all()
#for item in items:
    #print(item.id)