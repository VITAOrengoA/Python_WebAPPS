"""
Routes and views for the flask application.
"""

from datetime import datetime
from re import I
from urllib import response
from flask import Flask, render_template, render_template_string, request, session
from flask_session import Session
from flask.templating import _render
from Lab7 import app
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
from googletrans import Translator
from django import forms
from .forms import UploadFileForm
import os
import string
import psycopg2 
import json
import csv
import io
from PIL import Image
import pdfplumber
import hashlib
import secrets
from deep_translator import GoogleTranslator
from datetime import timedelta

app.secret_key = "session"
 
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
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

@app.route('/blackboard-temp')
def blackboard_temp():
    """Renders the Blackboard page."""
    return render_template(
        'blackboard-temp.html',
        title='Blackboard',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/self-service-temp')
def self_service():
    """Renders the Self-Service page."""
    return render_template(
        'self-service-temp.html',
        title='Self-Service',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/contact-temp')
def contact_temp():
    """Renders the contact page."""
    return render_template(
        'contact-temp.html',
        title='Contact',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/news-temp')
def news_temp():
    """Renders the news page."""
    return render_template(
        'news-temp.html',
        title='News',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/events-temp')
def events_temp():
    """Renders the event page."""
    return render_template(
        'events-temp.html',
        title='Events',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/map-temp')
def map_temp():
    """Renders the map page."""
    return render_template(
        'map-temp.html',
        title='Map',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/register')
def register():
    """Renders the register page."""
    return render_template(
        'register.html',
        title='Registration',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/successfull-registration')
def successfull_registration():
    """Renders the about page."""
    return render_template(
        'successfull-registration.html',
        title='Successfull Registration',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/dashboard')
def dashboard():
    """Renders the about page."""
    if "user" in session:
        return render_template(
            'dashboard.html',
            title='Dashboard',
            year=datetime.now().year,
            message='Your application description page.')    
    else:
        return render_template('login.html')
    
@app.route('/login')
def login_page():
    """Renders the about page."""
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Your application description page.'

    )
def decode_file(file: bytes, filename: str) -> str:
    """Decode a single file based on the extension."""
    if filename.endswith('.txt'):
        return file.decode('utf-8')
    elif filename.endswith('.csv'):
        decoded_csv = csv.reader(io.StringIO(file.decode('utf-8')))
        return '\n'.join([', '.join(row) for row in decoded_csv])
    elif filename.endswith('.json'):
        return json.dumps(json.loads(file.decode('utf-8')), indent=4)
    elif filename.endswith('.jpg') or filename.endswith('.png'):
        image = Image.open(io.BytesIO(file))
        return f"Image: {filename}, size: {image.size}"
    elif filename.endswith('.pdf'):
        pdf = pdfplumber.open(io.BytesIO(file))
        pages_text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
        return pages_text
    else:
        raise ValueError(f"Unsupported file type: {filename}")

@app.route('/dashboard', methods=['GET', 'POST'])
def upload_file():
    """
    Processes file uploads and interacts with the chatbot.
    """
    if request.method == 'POST':              
        language = request.form.get('language_choice')         
        error_lang = "Invalid Language Selection"
        error_user_message = "Invalid input"

        # Check if file is uploaded
        if 'file' in request.files:
            uploaded_file = request.files['file']
            if uploaded_file.filename != '' and language is not None:
                if language == "0":
                    return render_template('dashboard.html', translated_message=error_lang)
                else:
                    try:
                        user_message_file = decode_file(uploaded_file.read(), uploaded_file.filename)
                        translated_sentence = GoogleTranslator(source='auto', target=language).translate(user_message_file)
                        return render_template('dashboard.html', translated_message=translated_sentence)
                    except ValueError as e:
                        return render_template('dashboard.html', translated_message=str(e))
            else:
                user_message = request.form.get('user_message')             
                if language == "0":
                    return render_template('dashboard.html', translated_message=error_lang)
                elif user_message == "":
                    return render_template('dashboard.html', translated_message=error_user_message)            
                else:
                    translated_sentence = GoogleTranslator(source='auto', target=language).translate(user_message)
                    return render_template('dashboard.html', translated_message=translated_sentence)  
    else:
        response = "No file was uploaded"
        return render_template('dashboard.html', translated_message=response)

#DATABASE CONNECTION
#Login Action
@app.route('/dashboard-login',methods=['GET', 'POST'])
def login_manager():    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        password = encrypt(username,password)
        # Connect to the database 
        conn = psycopg2.connect(database="dbvita", 
                                user="dbvita_user", 
                                password="a1nTA6Rw06fZrFwEFw9J29MkaYwrIEcn", 
                                host="dpg-co6tf4fsc6pc738bpj70-a.oregon-postgres.render.com", port="5432") 
  
        # create a cursor 
        cur = conn.cursor() 
  
        # Select all products from the table 
        cur.execute("SELECT * FROM public.\"Students\" WHERE student_id = %s AND password = %s", [username, password])  
        # Fetch the data 
        data = cur.fetchone()
        if data:
            first_name = data[1]
             
            session["user"] = first_name
            return render_template('dashboard.html')
        else:
            print("error1")
            return render_template('login.html')       # close the cursor and connection 
        cur.close() 
        conn.close() 
  
        return render_template(request, 'index.html', {'error': 'Invalid username or password'}) 
#Register Action   
@app.route('/registration-login',methods=['GET', 'POST'])
def registration_login():    
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        print("here reg")
        if password1 == password2 and len(student_id) == 7 and student_id.isnumeric():     
            print("here reg")
            password1 = encrypt(student_id,password1)
            # Connect to the database 
            conn = psycopg2.connect(database="dbvita", 
                                    user="dbvita_user", 
                                    password="a1nTA6Rw06fZrFwEFw9J29MkaYwrIEcn", 
                                    host="dpg-co6tf4fsc6pc738bpj70-a.oregon-postgres.render.com", port="5432") 
  
            # create a cursor 
            cur = conn.cursor()   
            # Insert into student table
            sql = "INSERT INTO public.\"Students\" (student_id, first_name, last_name, password) VALUES(%s,%s,%s,%s)"
            val = (student_id, first_name, last_name, password1)
            #Execut query
            cur.execute(sql, val)
            #Commit to database
            conn.commit()  
            #Close database connection
            conn.close() 
            return render_template('successfull-registration.html')
        else:
            return render_template('register.html')
    else:       
            
        return render_template(request, 'index.html', {'error': 'Invalid username or password'}) 
    



def encrypt(student_id,password):
    # Generate a random salt using the secrets module
    

    # Hash the password using the salt and the SHA-256 algorithm
    salted_string = student_id.encode('utf-8') + password.encode('utf-8')

    # Get the hexadecimal representation of the hash
    sha512_hash = hashlib.sha512(salted_string).hexdigest()

    # Store the salt and hash_hex in your database
    return sha512_hash


def decrpyt(student_id,password):
    # Generate a random salt using the secrets module
    salt = student_id.token_hex(16)

    # Hash the password using the salt and the SHA-256 algorithm
    salted_string = salt + password.encode('utf-8')

    # Get the hexadecimal representation of the hash
    sha512_hash = hashlib.sha512(salted_string).hexdigest()

    # Store the salt and hash_hex in your database
    return sha512_hash
