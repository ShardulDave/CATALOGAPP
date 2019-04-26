# Catalog_Application

A web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. 

## Technologies which will be used


|Flask|SQLAlchemy|PostgreSQL|
|--|--|--|
|[![mdb](http://flask.pocoo.org/docs/1.0/_images/logo-full.png)](http://flask.pocoo.org/)|[![mdb](https://www.sqlalchemy.org/img/sqla_logo.png)](https://www.sqlalchemy.org/)|[![mdb](https://www.postgresql.org/media/img/about/press/elephant.png)](https://www.postgresql.org/)
|Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions.|The SQLAlchemy SQL Toolkit and Object Relational Mapper is a comprehensive set of tools for working with databases and Python.|PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.|
  * Flask 1.0.2 
  * SQLAlchemy 1.3
  * PostgreSQL 9.5.14
  * Vagrant
  * VirtualBox
  * HTML5, CSS3, JavaScript(ES6), Python
  
This web application is a project under the Udacity's Full Stack Nanodegree program.

## Steps to run the application
### Part 1
1) [Download Vagrant](https://www.vagrantup.com/downloads.html)
2) [Download VirtualBox](https://www.virtualbox.org/)

### Part 2
1) Go to https://developers.facebook.com/
2) Log-In into it
3) go to My Apps-> Add New App
4) Write a name into display name and click on Create App ID
5) Now on the top left corner click the drop down box(where the app name will be written)
6) Click Create Test App and then again Create Test App
7) Now in the left navigation bar click on PRODUCTS and click Facebook Login
8) Click on Web
9) Set the url as http://localhost:8000
10) Now in the left navigation bar go to Settings and click Basic
11) Save the App ID and App Secret.

### Part 4
1) Clone the repository
```sh
$ git clone https://github.com/ShardulDave/Catalog_Application.git
```
2) cd into the follwing folder
```sh
$ cd [directory]/Catalog_Application/vagrant/catalog
```
3) Open fb_client_secrets.json and add the App ID and App Secret into it and save it

4) Open template/login.html and App ID where its written 'Add you App ID here' and save it

5) Run the follwing command into the terminal
```sh
$ cd [directory]/Catalog_Application/vagrant
$ vagrant up
$ vagrant ssh
```
6) Once into the vagrant machine run the following command
```sh
$ cd /vagrant/catalog
```
7) Now we will need to create a database
```sh
$ psql
vagrant=> create database catalogdb
vagrant=> \q
```
8) Now run the files
```sh
$ python database_setup.py
$ python app.py
```
9) Now open a web browser and run http://localhost:5000/

## References

### Reference for the project
* https://docs.google.com/document/d/e/2PACX-1vT7XPf0O3oLCACjKEaRVc_Z-nNoG6_ssRoo_Mai5Ce6qFK_v7PpR1lxmudIOqzKo2asKOc89WC-qpfG/pub?embedded=true

### Reference for database setup
* https://www.compose.com/articles/using-postgresql-through-sqlalchemy/
* https://docs.sqlalchemy.org/en/latest/dialects/postgresql.html

## Citation
* https://github.com/udacity/ud330/tree/master/Lesson4/step2
