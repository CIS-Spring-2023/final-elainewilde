#This was taken directly from the notes in class
#I'm not sure if I'm understanding this well enough or not to have it in my application but going to try

import hashlib
#imports the datetime to be used in the authentication process later when logging in
import datetime
import time
import flask
from flask import jsonify
from flask import request, make_response


#setting up an application name
app = flask.Flask(__name__) #sets up the application
app.config["DEBUG"] = True #allows to show errors in browser the same from All_APIs

# password and username to login with
masterPassword = "Dustylaw95931337!m33pNowAy"
masterUsername = 'admin'
validTokens = {
    "100", "200", "300", "400"
}

# basic http authentication, prompts username and password upon contacting the endpoint
# 'password' as plaintext should not be used to verify authorization to access. 
# the password should be hashed and the hash should be compared to the stored password hash in the database
@app.route('/authenticatedroute', methods=['GET'])
def auth_example():
    if request.authorization:
        encoded=request.authorization.password.encode() #unicode encoding
        hashedResult = hashlib.sha256(encoded) #hashing
        if request.authorization.username == masterUsername and hashedResult.hexdigest() == masterPassword:
            return '<h1> WE ARE ALLOWED TO BE HERE </h1>'
    return make_response('COULD NOT VERIFY!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

# token submission as part of the url
@app.route('/api/token/<token>', methods=['GET'])
def auth_token(token):
    for validToken in validTokens:
        if token == validToken: #check if token is valid, compares against a set of valid tokens in a database table
            return '<h1> Congratulations, Authentication successful! </h1>'
    return 'INVALID ACCESS TOKEN'

# token submission that has expiration date and authorization is given only if token is not expired yet
@app.route('/api/timetoken/<timetoken>', methods=['GET']) #token is part of the url -> must be retrieved from somewhere first
def auth_timetoken(timetoken):
    if float(timetoken) > time.time(): #check if the token we have is valid still valid beyond right now (in practice you wouldn't use clearview raw time stamp, you would hash it together with a private key)
        return '<h1> Your time token is still valid! Wonderful! </h1>'
    return 'Your time token has expired!'

# valid encrypted token: 7573824000
# invalid encrypted token: 6563980800
# encryption with bitshift << 2 and >> 2 to shift bits by 2 locations
@app.route('/api/timetokenencrypted/<timetoken>', methods=['GET']) #token is part of the url -> must be retrieved from somewhere first
def auth_encrypted_timetoken(timetoken):
    encryptedToken = int(timetoken)
    decryptedToken = encryptedToken >> 2
    if decryptedToken > time.time(): #check if the token is valid or valid beyond right now 
        return '<h1> Your time token is still valid! Wonderful! </h1>'
    return 'Your time token has expired!'

authorizedusers = [
    {
        # default user
        'username': 'admin',
        'password': 'Dustylaw95931337!m33pNowAy',
        'role': 'admin',
        'token': '0',
        'admininfo': 'default user login for the sake of this project'
    },
    {
        #admin user
        'username': 'otto',
        'password': 'admin',
        'role': 'admin',
        'token': '1234657890',
        'admininfo': 'something super secret nobody can know'
    },
]

# this is the route to authenticate with username and password against a dataset
@app.route('/api/usernamepw', methods=['GET'])
def usernamepw_example():
    username = request.headers['username'] #gets header parameters. Requested headers are interpreted as dictionaries which makes access direct & easily understood
    pw = request.headers['password']
    for au in authorizedusers: #loops through users & finds one that is authorized for access
        if au['username'] == username and au['password'] == pw: #found authorized user
            sessiontoken = au['token']
            adminInfo = au['admininfo']
            returnInfo = []
            returnInfo.append(au['role'])
            returnInfo.append(sessiontoken)
            returnInfo.append(adminInfo)

            return jsonify(returnInfo)
    return 'SECURITY ERROR' #never give away too many details what went wrong, just saying error is preferred

app.run()#runs the application

#---------------------------------------SOURCES / REFERENCES----------------------------------------------
# table database & connection creation taken from Homework1
# https://www.geeksforgeeks.org/python-sqlite-crud-operations/
# https://dev.to/ayabouchiha/sending-get-post-put-delete-requests-in-python-45o8
# Some code is modeled after the example we did in class from the Notes (crudops nots, (crudops.py, sql.py,creds.py))
# API Tutorial https://www.youtube.com/watch?v=GMppyAPbLYk
# Code is largely modeled after this example & helped me understand better  https://parzibyte.me/blog/en/2020/11/12/creating-api-rest-with-python-flask-sqlite3/
#https://www.youtube.com/watch?v=CLG0ha_a0q8
# longin / security notes from class notes 03/04/2023