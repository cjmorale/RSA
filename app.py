from flask import Flask, render_template, request
from RSA import *

import pymysql

app = Flask(__name__)

def validate_user(new_email,new_user,pw1,pw2):
    hostname = 'rsadb.clm6gze49vii.us-west-2.rds.amazonaws.com'
    port =33306
    username = 'cjmorale'
    password = 'Overland04'
    database = 'users'

    myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database, port=port )
    cur = myConnection.cursor()
    cur.execute( "SELECT Login, Email_Address from User_info;" )
    Data = cur.fetchall()

    email = sum([int(new_email==Data[x][1]) for x in range(len(Data))])
    name = sum([int(new_user==Data[x][0]) for x in range(len(Data))])

    if(pw1!=pw2):
        message ='Passwords do not match. Please Re-Enter Passwords'
        success = False
    elif(email > 0 and name>0):
        message ='Username and email address already in use. Choose another username and email address please.'
        success = False
    elif(name > 0):
        message ='Username already in use. Choose another username please.'
        success = False
    elif(email > 0):
        message ='Email address already in use. Choose another email address please.'
        success = False
    else:
        message ='Account Setup Successful. Check email for confirmation email'
        success = True
    print(message)
    myConnection.close()
    return({'message':message, 'success':success})

def validate_login(user,password):
    hostname = 'rsadb.clm6gze49vii.us-west-2.rds.amazonaws.com'
    port =33306
    username = 'cjmorale'
    password = 'Overland04'
    database = 'users'

    myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database, port=port )
    cur = myConnection.cursor()
    cur.execute( "SELECT Login, Password from User_info;" )
    Data = cur.fetchall()

    verify = [((user==Data[x][0]),(password==Data[x][1]) ) for x in range(len(Data))]

    if( (True,True) in verify ):
        message ='Username and email address are in database.'
        success = True
    else:
        message ='Username and email address are not in database.'
        success = False
    print(message)
    myConnection.close()
    return({'message':message, 'success':success})


@app.route("/")
def main():
    return render_template('Home.html')

@app.route("/sign_in", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        valid = validate_login(request.form['inputUsername'],
                              request.form['inputPassword'])
        print(valid)
        if valid['success'] is True:
            data = {'username': request.form['inputUsername']}
            print(data)
            user = request.form['inputUsername']
            return render_template('TEMPLATE.html', name=user)
        else:
            return render_template('sign_in_fail.html')
    else:
        return render_template('sign_in.html')


@app.route("/sign_up", methods=['POST', 'GET'])
def setup():
    error = None
    if request.method == 'POST':
        valid = validate_user(request.form['inputEmail'],
                              request.form['inputName'],
                              request.form['inputPassword1'],
                              request.form['inputPassword2'])
        print(valid)
        if valid['success'] is True:
            return render_template('sign_up_success.html')
        else:
            return render_template('sign_up_fail.html')
    else:
        return render_template('sign_up.html')

if __name__ == "__main__":
    app.run()
