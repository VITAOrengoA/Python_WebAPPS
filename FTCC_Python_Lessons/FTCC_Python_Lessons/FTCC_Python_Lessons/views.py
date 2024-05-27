"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, request, session
from flask_session import Session
from datetime import datetime
from flask import render_template
from FTCC_Python_Lessons import app
import os
import string
import psycopg2 
import hashlib

app.secret_key = "session"

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/login')
def login_page():
    """Renders the login page."""
    return render_template('login.html', title='Login', year=datetime.now().year, message='Your application description page.')

@app.route('/dashboard')
def dashboard():
    if "user" in session:
        return render_template('dashboard.html', title='Dashboard', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-1-1')
def python_course_1_1():
    if "user" in session:
        return render_template('python-course-1-1.html', title='python-course-1-1', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-1-2')
def python_course_1_2():
    if "user" in session:
        return render_template('python-course-1-2.html', title='python-course-1-2', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-1-3')
def python_course_1_3():
    if "user" in session:
        return render_template('python-course-1-3.html', title='python-course-1-3', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-2-1')
def python_course_2_1():
    if "user" in session:
        return render_template('python-course-2-1.html', title='python-course-2-1', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-2-2')
def python_course_2_2():
    if "user" in session:
        return render_template('python-course-2-2.html', title='python-course-2-2', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-2-3')
def python_course_2_3():
    if "user" in session:
        return render_template('python-course-2-3.html', title='python-course-2-3', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-3-1')
def python_course_3_1():
    if "user" in session:
        return render_template('python-course-3-1.html', title='python-course-3-1', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-3-2')
def python_course_3_2():
    if "user" in session:
        return render_template('python-course-3-2.html', title='python-course-3-2', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-3-3')
def python_course_3_3():
    if "user" in session:
        return render_template('python-course-3-3.html', title='python-course-3-3', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-4-1')
def python_course_4_1():
    if "user" in session:
        return render_template('python-course-4-1.html', title='python-course-4-1', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-4-2')
def python_course_4_2():
    if "user" in session:
        return render_template('python-course-4-2.html', title='python-course-4-2', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-4-3')
def python_course_4_3():
    if "user" in session:
        return render_template('python-course-4-3.html', title='python-course-4-3', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-5-1')
def python_course_5_1():
    if "user" in session:
        return render_template('python-course-5-1.html', title='python-course-5-1', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-5-2')
def python_course_5_2():
    if "user" in session:
        return render_template('python-course-5-2.html', title='python-course-5-2', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-5-3')
def python_course_5_3():
    if "user" in session:
        return render_template('python-course-5-3.html', title='python-course-5-3', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-index-1')
def python_course_index_1():
    if "user" in session:
        return render_template('python-course-index-1.html', title='python-course-index-1', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-index-2')
def python_course_index_2():
    if "user" in session:
        return render_template('python-course-index-2.html', title='python-course-index-2', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')

@app.route('/python-course-index-3')
def python_course_index_3():
    if "user" in session:
        return render_template('python-course-index-3.html', title='python-course-index-3', year=datetime.now().year, message='Your application description page.')
    else:
        return render_template('login.html')



@app.route('/dashboard-login', methods=['GET', 'POST'])
def login_manager():    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password = encrypt(username, password)

        # Connect to the database 
        conn = psycopg2.connect(database="dbvita", user="dbvita_user", password="a1nTA6Rw06fZrFwEFw9J29MkaYwrIEcn", host="dpg-co6tf4fsc6pc738bpj70-a.oregon-postgres.render.com", port="5432")
        cur = conn.cursor() 
  
        # Select all products from the table 
        cur.execute("SELECT * FROM public.\"Students\" WHERE student_id = %s AND password = %s", [username, password])  
        data = cur.fetchone()
        if data:
            first_name = data[1]
            session["user"] = first_name
            return render_template('dashboard.html')
        else:
            return render_template('login.html') 

        cur.close() 
        conn.close() 
  
        return render_template(request, 'index.html', {'error': 'Invalid username or password'}) 

@app.route('/registration-login', methods=['GET', 'POST'])
def registration_login():    
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if password1 == password2 and len(student_id) == 7 and student_id.isnumeric():     
            password1 = encrypt(student_id, password1)

            # Connect to the database 
            conn = psycopg2.connect(database="dbvita", user="dbvita_user", password="a1nTA6Rw06fZrFwEFw9J29MkaYwrIEcn", host="dpg-co6tf4fsc6pc738bpj70-a.oregon-postgres.render.com", port="5432")
            cur = conn.cursor()   
            # Insert into student table
            sql = "INSERT INTO public.\"Students\" (student_id, first_name, last_name, password) VALUES(%s,%s,%s,%s)"
            val = (student_id, first_name, last_name, password1)
            cur.execute(sql, val)
            conn.commit()  
            conn.close() 
            return render_template('successful-registration.html')
        else:
            return render_template('register.html')
    else:       
        return render_template(request, 'index.html', {'error': 'Invalid username or password'}) 

def encrypt(student_id, password):
    salted_string = student_id.encode('utf-8') + password.encode('utf-8')
    sha512_hash = hashlib.sha512(salted_string).hexdigest()
    return sha512_hash
 