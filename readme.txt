For creating of this program, I was using Windows 10.
I cannot guarantee normal work on other operating systems like MAC or Linux based OSes.


To start using it, u will need to create a database. 
I used PostgreSQL 14 for it.

Below are 2 queries that will help you create DB.

First query:
CREATE DATABASE numberguessinggame;

Second query (must be used in query tool of 'numberguessinggame' DB):
CREATE TABLE leader_board
(
	username CHARACTER VARYING(15),
	userscore SMALLINT DEFAULT 0
);
CREATE TABLE users
(
	username CHARACTER VARYING(15),
	userpassword CHARACTER VARYING(20)
);


After you create database, you will need to create a file in the folder of this game with the name "database.ini".

[postgresql]
host=localhost
dbname=numberguessinggame
user=*name_of_ser_which_can_change_DB*
password=*password_of_your_user'

The file should contain information relevant to you. 
You can see an example above.


Also, you will need installed python at your PC and 2 packages for it.
I think that you can install Python yourself.

With the help of the 2 commands below, you can install the necessary packages (use them in CMD):
python pip install psycopg2
python pip install configparser

After that you can run "main.py" by the help of python in CMD and play.
