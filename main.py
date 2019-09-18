from flask import  Flask, escape, url_for, render_template, request, redirect
import sqlite3
import database

app = Flask(__name__)
database.create_db()

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/registration', methods =['GET','POST'])
def registration(): 
    if request.method =='GET':
        return render_template('registration.html')
    else:
        name= request.form['name'] 
        email = request.form['email']
        password = request.form['password']
        if (database.insert_user(name,email,password)):
            print("user inserted")
        return  render_template('login.html')



app.run(host='localhost' ,port=8000, debug= True)