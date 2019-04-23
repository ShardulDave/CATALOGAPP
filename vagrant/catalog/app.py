#!/usr/bin/env python3

#Backend code using Flask framework

from flask import Flask, render_template, request, redirect, url_for, jsonify

from sqlalchemy import create_engine  
from sqlalchemy import Column, String, ForeignKey, Integer  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker, relationship
from database_setup import Base, User, Category, Item

app = Flask(__name__)

engine = create_engine("postgres:///catalogdb")  
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# JSON APIs Endpoints to view Categories and the items within each categories

@app.route('/category/<int:category_id>/item/JSON')
def categoryItemJSON(category_id):
    items = session.query(Item).filter_by(category_id=category_id).all()
    return jsonify(Items=[i.serialize for i in items])

@app.route('/category/<int:category_id>/item/<int:item_id>/JSON')
def itemJSON(category_id, item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    return jsonify(Item=item.serialize)

@app.route('/category/JSON')
def categoryJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[r.serialize for r in categories])

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)