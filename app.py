from flask import Flask, render_template, request, session, redirect, url_for, send_file
from RSA import *
import pymysql
import json
from functools import wraps

# app = ResponsiveFlask(__name__)
app = Flask(__name__)
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(session['username'])
        if session['username'] is None:
            return redirect(url_for('sign_in', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def validate_user(new_email, new_user, pw1, pw2, new_name):
    hostname = 'rsadb.clm6gze49vii.us-west-2.rds.amazonaws.com'
    port = 33306
    username = 'cjmorale'
    password = 'Overland04'
    database = 'users'

    myConnection = pymysql.connect(host=hostname, user=username,
                                   passwd=password, db=database, port=port,
                                   autocommit=True)
    cur = myConnection.cursor()
    cur.execute("SELECT Login, Email_Address, Name from User_info;")
    Data = cur.fetchall()

    email = sum([int(new_email == Data[x][1]) for x in range(len(Data))])
    user_name = sum([int(new_user == Data[x][0]) for x in range(len(Data))])

    if(pw1 != pw2):
        message = 'Passwords do not match. Please Re-Enter Passwords'
        success = False
    elif(email > 0 and user_name > 0):
        message = 'Username and email address already in use.' \
                  'Choose another username and email address please.'
        success = False
    elif(user_name > 0):
        message = 'Username already in use. Choose another username please.'
        success = False
    elif(email > 0):
        message = 'Email address already in use.'\
                  'Choose another email address please.'
        success = False
    else:
        temp = "INSERT INTO User_info (Name, Login, Email_Address, Password)"
        temp2 = "VALUES ('"+str(new_user)+"','"+str(new_name)+"','" + \
                str(new_email)+"','"+str(pw1)+"');"
        cur.execute(temp+temp2)

        message = 'Account Setup Successful. Confirmation email sent.'
        success = True
    print(message)
    myConnection.close()
    return({'message': message, 'success': success})


def validate_login(user, pwd):
    hostname = 'rsadb.clm6gze49vii.us-west-2.rds.amazonaws.com'
    port = 33306
    username = 'cjmorale'
    password = 'Overland04'
    database = 'users'

    myConnection = pymysql.connect(host=hostname, user=username,
                                   passwd=password, db=database,
                                   port=port, autocommit=True)
    cur = myConnection.cursor()
    cur.execute("SELECT Login, Password from User_info;")
    Data = cur.fetchall()
    for x in range(len(Data)):
        print((Data[x][0], Data[x][1]))
    verify = [((user == Data[x][0]), (pwd == Data[x][1]))
              for x in range(len(Data))]
    print(verify)
    if((True, True) in verify):
        message = 'Username and email address are in database.'
        success = True
    else:
        message = 'Username and email address are not in database.'
        success = False
    print(message)
    myConnection.close()
    return({'message': message, 'success': success})


@app.route("/")
def main():
    return render_template('Home.html')


@app.route("/sign_in", methods=['POST', 'GET'])
def sign_in():
    error = None
    if request.method == 'POST':
        valid = validate_login(request.form['inputUsername'],
                               request.form['inputPassword'])
        print(valid)
        if valid['success'] is True:
            data = {'username': request.form['inputUsername']}
            print(data)
            user = request.form['inputUsername']
            session['username'] = user
            return redirect(url_for('home_page'))
            # return render_template('TEMPLATE.html', name=user)
        else:
            return render_template('sign_in_fail.html')
    else:
        return render_template('sign_in.html')


@app.route("/sign_up", methods=['POST', 'GET'])
def setup():
    if request.method == 'POST':
        valid = validate_user(request.form['inputEmail'],
                              request.form['inputName'],
                              request.form['inputPassword1'],
                              request.form['inputPassword2'],
                              request.form['inputUsername'],)
        print(valid)
        if valid['success'] is True:
            return render_template('sign_up_success.html')
        else:
            return render_template('sign_up_fail.html')
    else:
        return render_template('sign_up.html')


@app.route("/user_profile", methods=['POST', 'GET'])
@login_required
def user_profile():
        return render_template('user_profile.html')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('sign_in'))


@app.route('/home_page', methods=['POST', 'GET'])
def home_page():
        return render_template('TEMPLATE.html')


@app.route('/get_key', methods=['POST', 'GET'])
def get_key():
    rsa = RSA()
    try:
        print(request)
        key = rsa.generate_key(request.form['inputprime1'],
                               request.form['inputprime2'],
                               request.form['inputexp'])
        print(key)
        json.dump(key, open("key.txt", 'w'))
        print('Hello')
        return(send_file("key.txt", as_attachment=True))
        # return render_template('TEMPLATE.html')
    except:
        return render_template('get_key.html')


@app.route('/upload_key', methods=['POST', 'GET'])
def upload_key():
        return render_template('upload_key.html')


@app.route('/settings', methods=['POST', 'GET'])
def settings():
        return render_template('settings.html')


@app.route('/messages', methods=['POST', 'GET'])
def messages():
        return render_template('messages.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
