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


#Creates the cargo table for this Final Project

create_cargo_table="""CREATE TABLE IF NOT EXISTS cargo(
                id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                weight VARCHAR(20),
				cargotype VARCHAR(20),
				departure VARCHAR(10),
                arrival VARCHAR(10),
                shipid INT,
                FOREIGN KEY (shipid) REFERENCES spaceship(id)
            );
            """
cursor.execute(create_cargo_table)


#---------------------------------------CRUD (CREATE) --------------------------------------------------------------------------


#Inserts a new record of Cargo into the table
def insert_cargo(weight, cargotype, departure, arrival, shipid):
    db = mydb
    cursor = db.cursor()
    #the SQL statemtent for the operation
    cursor.execute("INSERT INTO cargo(weight, cargotype, departure, arrival, shipid) VALUES (%s, %s, %s, %s, %s)",(weight, cargotype, departure, arrival, shipid))
    db.commit()
    return True


#---------------------------------------CRUD (UPDATE) --------------------------------------------------------------------------


# Updates the values of an existing cargo record in the table
def update_cargo(weight, cargotype, departure, arrival, shipid):
    db = mydb
    cursor = db.cursor()
    statement = ("UPDATE cargo SET (weight, cargotype, departure, arrival, shipid) WHERE id = exact value; VALUES (%s, %s, %s, %s, %s)", (weight, cargotype, departure, arrival, shipid))
    cursor.execute(statement, [weight, cargotype, departure, arrival, shipid])
    db.commit()
    return True


# #---------------------------------------CRUD (DELETE) --------------------------------------------------------------------------


# #deletes a cargo record from the table with the matching ID
def delete_cargo(id):
    db = mydb
    cursor = db.cursor()
    statement = ("DELETE FROM cargo WHERE id = exact value")
    cursor.execute(statement, [id])
    db.commit()
    return True


# #---------------------------------------CRUD (READ) --------------------------------------------------------------------------


# #Gets the cargo record by ID and displays it with the rest of the details
def get_by_id(id):
    db = mydb
    cursor = db.cursor()
    statement = ("SELECT FROM cargo WHERE id = exact value; (weight, cargotype, departure, arrival, shipid) VALUES (%s, %s, %s, %s, %s)")
    cursor.execute(statement, [id])
    return cursor.fetchone()

# #Gets the cargo information
def get_cargo():
    db = mydb
    cursor = db.cursor()
    query = ("SELECT FROM cargo (id, weight, cargotype, departure, arrival, shipid) VALUES (%s, %s, %s, %s, %s, %s)")
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




