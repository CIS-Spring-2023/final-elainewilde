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


#Creates the spaceship table for this Final Project


create_spaceship_table="""CREATE TABLE IF NOT EXISTS spaceship(
                id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                maxweight VARCHAR(20),
				captainid INT,
                FOREIGN KEY (captainid) REFERENCES captain(id)
            )
            """
cursor.execute(create_spaceship_table)

#---------------------------------------CRUD (CREATE) --------------------------------------------------------------------------


#Inserts a new record of Snowboard into the table
def insert_spaceship(maxweight, captainid):
    db = mydb
    cursor = db.cursor()
    #the SQL statemtent for the operation
    cursor.execute("INSERT INTO spaceship(maxweight, captainid) VALUES (%s, %s)",(maxweight, captainid))
    db.commit()
    return True


#---------------------------------------CRUD (UPDATE) --------------------------------------------------------------------------


#Updates the values of an existing spaceship record in the table
def update_spaceship(maxweight, captainid):
    db = mydb
    cursor = db.cursor()
    statement = ("UPDATE spaceship SET (maxweight, captainid) WHERE id = exact value; VALUES (%s, %s)", (maxweight, captainid))
    cursor.execute(statement, [maxweight, captainid, id])
    db.commit()
    return True


#---------------------------------------CRUD (DELETE) --------------------------------------------------------------------------


#deletes a spaceship record from the table with the matching ID
def delete_spaceship(id):
    db = mydb
    cursor = db.cursor()
    statement = ("DELETE FROM spaceship WHERE id = exact value")
    cursor.execute(statement, [id])
    db.commit()
    return True


#---------------------------------------CRUD (READ) --------------------------------------------------------------------------


#Gets the spaceship by ID and displays it with the rest of the details
def get_by_id(id):
    db = mydb
    cursor = db.cursor()
    statement = ("SELECT FROM spaceship WHERE id = exact value; (maxweight, captainid) VALUES (%s, %s)")
    cursor.execute(statement, [id])
    return cursor.fetchone()

#Gets the spaceship information
def get_spaceship():
    db = mydb
    cursor = db.cursor()
    query = ("SELECT FROM spaceship (id, maxweight, captainid) VALUES (%s, %s, %s)")
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










