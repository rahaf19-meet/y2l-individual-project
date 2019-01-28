from databases import *
from flask import Flask, flash, render_template, url_for, redirect, request
from flask import session as login_session
# from flask.ext.session import Session
# from forgotpass import send_mail
# Starting the flask app

app = Flask(__name__)
app.secret_key = "VERY SECRET." 



@app.route('/', methods=['GET', 'POST'])
def home():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    return render_template('homee.html',log=log)

@app.route('/game', methods=['GET', 'POST'])
def game():
	return render_template('game_try.html')

@app.route('/tictactoe', methods=['GET', 'POST'])
def tictactoe():
	return render_template('tictactoe.html')

@app.route('/mines', methods=['GET', 'POST'])
def mines():
	return render_template('mines.html')

@app.route('/lovetest', methods=['GET', 'POST'])
def lovetest():
	return render_template('lovetest.html')

@app.route('/who', methods=['GET', 'POST'])
def who():
	return render_template('who.html')

@app.route('/lightsout', methods=['GET', 'POST'])
def lightsout():
	return render_template('lightsout.html')

@app.route('/hitdot', methods=['GET', 'POST'])
def hitdot():
	return render_template('hitdot.html')


@app.route('/signup',methods= ['GET','POST'])
def signup ():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        try:
            name = request.form['name']
            lastName = request.form['familyName']
            user = request.form['user']
            password = request.form['password']
            mail = request.form['mail']
            loc = request.form['loc']
        except:
            return render_template("signup.html", error="u r bad")
        add_student(user,password,mail,name,lastName,loc)
        return redirect(url_for('home'))


############################################ LOGIN ############################################

@app.route('/login',methods= ['GET','POST'])
def login():
    log = 0
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    print(log)
    if request.method == 'GET':
        return render_template('login.html',log=log)
    else:
        user = request.form['username']
        password = request.form['password']
        if check_account(user,password):
            login_session['logged_in'] = True
            login_session['username'] = request.form['username']

            # return redirect(url_for('show_prof',username=user))
            return redirect(url_for('home',log=log))

        else:
            return render_template('login.html', error = "username or password are not correct!")

@app.route('/logout')
def logout():
    login_session.clear()
    return redirect(url_for('home'))

@app.route('/forgetpwd',methods= ['GET','POST'])
def forget_pwd():
    if('username' in login_session):
        log = "true"
    else:
        log = "false"
    if request.method == 'GET':
        return render_template('forgetpwd.html',log=log)
    else:
        email = request.form['email']
        if if_account_exist(email):
            send_mail(email)
            return redirect(url_for("home",log=log))
        else:
            return render_template('forgetpwd.html',log=log)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
