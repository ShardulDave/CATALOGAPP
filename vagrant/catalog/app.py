#!/usr/bin/env python3

#Backend code using Flask framework

from flask import Flask, render_template, request, redirect, url_for, jsonify

from sqlalchemy import create_engine  
from sqlalchemy import Column, String, ForeignKey, Integer  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker, relationship
from database_setup import User, Category, Item

app = Flask(__name__)

db_string = "postgres:///catalogdb"

db = create_engine(db_string)  
Base = declarative_base()

Session = sessionmaker(db)  
session = Session()


@app.route('/')
@app.route('/category/')
def showCategory():
	categories = session.query(Category).all()
	return render_template('category.html', categories=categories)

@app.route('/category/<int:category_id>/')
def showItems(category_id):
	category=session.query(Category).filter_by(id=category_id).one()
	items=session.query(Item).filter_by(category_id=category_id).all()
	return render_template('item.html', category=category,items=items)


if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)