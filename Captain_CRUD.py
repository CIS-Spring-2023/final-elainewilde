#more concise way to code for CRUD & APIs from parizbyte, so starting new file instead of referencing notes so much
#originally used the example in class but liked this better due to being more concise

#---------------------------------------CONNECTION---------------------------------------------

#This is from my Homework 1 which I'll go ahead and source too

import mysql.connector

#making the connection with mysql connector & inserting my database info in
mydb = mysql.connector.connect(
   user='admin', password='Dustylaw95931337!m33pNowAy', host='cis3368spring.clhkjoaevkn8.us-east-2.rds.amazonaws.com', database='cis3368springdb'
)                                                             

#Making the cursor object & using the cursor method
cursor = mydb.cursor()

#---------------------------------------CREATES TABLE------------------------------------------

#Creates the captain table for this Final Project

create_captain_table="""CREATE TABLE IF NOT EXISTS captain(
                id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                firstname VARCHAR(20),
				lastname VARCHAR(20),
				captainrank VARCHAR(10),
                homeplanet VARCHAR(10)
            )
            """
cursor.execute(create_captain_table)

#---------------------------------------CRUD (CREATE) --------------------------------------------------------------------------


#Inserts a new record of Snowboard into the table
def captain(firstname, lastname, captainrank, homeplanet):
    db = mydb
    cursor = db.cursor()
    #the SQL statemtent for the operation
    cursor.execute("INSERT INTO captain(firstname, lastname, captainrank, homeplanet) VALUES (%s, %s, %s, %s)",(firstname, lastname, captainrank, homeplanet))
    db.commit()
    return True


#---------------------------------------CRUD (UPDATE) --------------------------------------------------------------------------


#Updates the values of an existing snowboard record in the table
def update_captain(firstname, lastname, captainrank, homeplanet):
    db = mydb
    cursor = db.cursor()
    statement = ("UPDATE captain SET (firstname, lastname, captainrank, homeplanet) WHERE id = exact value; VALUES (%s, %s, %s, %s)", (firstname, lastname, captainrank, homeplanet))
    cursor.execute(statement, [firstname, lastname, captainrank, homeplanet, id])
    db.commit()
    return True


#---------------------------------------CRUD (DELETE) --------------------------------------------------------------------------


#deletes a captain record from the table with the matching ID
def delete_captain(id):
    db = mydb
    cursor = db.cursor()
    statement = ("DELETE FROM captain WHERE id = exact value")
    cursor.execute(statement, [id])
    db.commit()
    return True


#---------------------------------------CRUD (READ) --------------------------------------------------------------------------


#Gets the captain by ID and displays it with the rest of the details
def get_by_id(id):
    db = mydb
    cursor = db.cursor()
    statement = ("SELECT FROM captain WHERE id = exact value; (firstname, lastname, captainrank, homeplanet) VALUES (%s, %s, %s, %s)")
    cursor.execute(statement, [id])
    return cursor.fetchone()

#Gets the captain information
def get_captain():
    db = mydb
    cursor = db.cursor()
    query = ("SELECT FROM captain (id, firstname, lastname, captainrank, homeplanet) VALUES (%s, %s, %s, %s, %s)")
    cursor.execute(query)
    return cursor.fetchall()

#---------------------------------------SOURCES / REFERENCES----------------------------------------------
# table database & connection creation taken from Homework1
# https://www.geeksforgeeks.org/python-sqlite-crud-operations/
# https://dev.to/ayabouchiha/sending-get-post-put-delete-requests-in-python-45o8
# Some code is modeled after the example we did in class from the Notes (crudops nots, (crudops.py, sql.py,creds.py))
# API Tutorial https://www.youtube.com/watch?v=GMppyAPbLYk
# Code is largely modeled after this example & helped me understand better  https://parzibyte.me/blog/en/2020/11/12/creating-api-rest-with-python-flask-sqlite3/
#https://www.youtube.com/watch?v=CLG0ha_a0q8



