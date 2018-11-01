import pdb
import numpy as np
from flask import Flask, render_template, flash, request, url_for, redirect
from content_management import Content
#import MySQLdb
#Automatic add html file for posts
TOPIC_DICT = Content()

app = Flask(__name__)
app.secret_key = b'A\x8by\xbdl\xbcpj>.EfWo,\xf2'
@app.route('/')
def homepage():
    try:
        return render_template("main.html")
    except Exception as e:
        return render_template("500.html", error = str(e))

@app.route('/dashboard/')
def dashboard():
    try:
        flash("FLASH TEST")
        if True:
            flash("flashing test")
        return render_template("dashboard.html",TOPIC_DICT = TOPIC_DICT)
    except Exception as e:
        return render_template("500.html", error = str(e))
@app.route('/python-basics/')
def python_basics():
    try:
        return render_template("python-basics.html")
    except Exception as e:
        return render_template("500.html", error = str(e))


@app.route('/contact-me/')
def contact_me():
    try:
        return render_template("contact-me.html")
    except Exception as e:
        return render_template("500.html", error = str(e))

@app.route('/login/', methods=["GET","POST"])
def login():
    error = ''
    try:	
        if request.method == "POST":
		
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            #flash(attempted_username)
            #flash(attempted_password)

            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('dashboard'))
				
            else:
                error = "Invalid credentials. Try Again."

        return render_template("login.html", error = error)

    except Exception as e:
        #flash(e)
        return render_template("login.html", error = error)

@app.route('/register/', methods=["GET","POST"])
def register():
    try:
        return render_template("register.html")
    except Exception as e:
        return render_template("500.html", error = str(e))

    
#if 404 error happens go to 404 page
@app.errorhandler(404)
def page_not_found(e):
    try:
        return render_template("404.html")
    except Exception as e:
        return render_template("500.html", error = str(e))		

if __name__ == "__main__":
    app.run()





