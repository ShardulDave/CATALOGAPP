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
@app.route('/Category/<int:category_id>/menu')
def restaurantMenu(category_id):
	restaurant = session.query(Category).filter_by(id = category_id).one()
	items = session.query(Item).filter_by(category_id = category_id)
	return render_template('menu.html', restaurant=restaurant, items = items, restaurant_id = restaurant_id)




@app.route('/restaurants/<int:restaurant_id>/new', methods=['GET','POST'])
def newMenuItem(restaurant_id):
	
	if request.method == 'POST':
		newItem = MenuItem(name = request.form['name'], description = request.form['description'], price = request.form['price'], course = request.form['course'], restaurant_id = restaurant_id)
		session.add(newItem)
		session.commit()
		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
	else:
		return render_template('newmenuitem.html', restaurant_id = restaurant_id)




@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit', methods = ['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
	editedItem = session.query(MenuItem).filter_by(id = menu_id).one()
	if request.method == 'POST':
		if request.form['name']:
			editedItem.name = request.form['name']
		if request.form['description']:
			editedItem.description = request.form['name']
		if request.form['price']:
			editedItem.price = request.form['price']
		if request.form['course']:
			editedItem.course = request.form['course']
		session.add(editedItem)
		session.commit()
		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
	else:
		
		return render_template('editmenuitem.html', restaurant_id = restaurant_id, menu_id = menu_id, item = editedItem)
	


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete', methods = ['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
	itemToDelete = session.query(MenuItem).filter_by(id = menu_id).one() 
	if request.method == 'POST':
		session.delete(itemToDelete)
		session.commit()
		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
	else:
		return render_template('deleteconfirmation.html', item = itemToDelete)



if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)