from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome", methods=['POST', 'GET'])
def welcome():
    print(request.method)
    username = request.args.get('username')
    return render_template('welcome-greeting.html', title="Welcome", username=username)

@app.route("/", methods=['POST'])
def validate():
    username = request.form['user_name']
    password = request.form['pass']
    verify_password = request.form['verify_pass']
    email = request.form['e_mail']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if len(username) == 0:
        username_error = 'No username entered'
        username = ''
    elif len(username) < 3 or len(username) > 20:
        username_error = 'Username out of 3-20 char range'
        username = ''
    elif " " in username:
        username_error = 'Username cannot contain spaces'
        username = ''


    if len(password) == 0:
        password_error = 'No password entered'
        password = ''
    elif len(password) < 3 or len(password) > 20:
        password_error = 'Password out of 3-20 char range'
        password = ''
    elif " " in password:
        password_error = 'Password cannot contain spaces'
        password = ''


    if len(verify_password) == 0:
        verify_password_error = 'No verification password entered'
        verify_password = ''
    elif len(verify_password) < 3 or len(verify_password) > 20:
        verify_password_error = 'Verification password out of 3-20 char range'
        verify_password = ''
    elif " " in verify_password:
        verify_password_error = 'Verification password cannot contain spaces'
        verify_password = ''
    elif verify_password != password:
        verify_password_error = 'Verification password entered does not match password'
        verify_password = ''


    if len(email) > 0:
        if len(email) < 3 or len(email) > 20:
            email_error = 'Email out of 3-20 char range'
            email = ''
        elif " " in email or "@" not in email or "." not in email:
            email_error = 'Email cannot contain spaces, and must have a "@" and a "."'
            email = ''



    if not username_error and not password_error and not verify_password_error and not email_error:
        
        return redirect('/welcome?username={0}'.format(username))
        
    else:
        return render_template('index.html', 
            username_error=username_error, 
            password_error=password_error, 
            verify_password_error=verify_password_error, 
            email_error=email_error, 
            username=username, password=password, 
            verify_password=verify_password, email=email)


@app.route("/")
def index():
    return render_template('index.html', title="Signup Page")

app.run()