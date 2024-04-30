"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, render_template_string, request
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
from deep_translator import GoogleTranslator

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


@app.route('/dashboard')
def dashboard():
    """Renders the about page."""
    return render_template(
        'dashboard.html',
        title='Dashboard',
        year=datetime.now().year,
        message='Your application description page.'

    )
@app.route('/dashboard', methods=['GET', 'POST'])
def upload_file():
    """
    Processes file uploads and interacts with the chatbot.
    """
    if request.method == 'POST':
        user_message = request.form.get('user_message')
        language = request.form.get('language_choice')
        
        #response = translate_user_message(user_message, language)
         
        translated_sentence = GoogleTranslator(source='auto', target=language).translate(user_message)
        return render_template('dashboard.html', translated_message=translated_sentence)
        
        # form = UploadFileForm(request.form, request.files)
        # if 'file' in request.files:
        #     if form.is_valid():
        #         uploaded_file = request.files['file']
        #         language = request.form.get('language')
        #         response = process_file_with_translator(uploaded_file, language)
        #         return render_template('dashboard.html', translated_message=response)
        #     elif request.form.get('user_message') != '':
        #         user_message = request.form.get('user_message')
        #         language = request.form.get('language')
        #         response = translate_user_message(user_message, language)
        #         return render_template('dashboard.html', translated_message=response)
        #     else:
        #         response = "No file was uploaded. Form is not valid"
        #         return render_template('dashboard.html', translated_message=response)
    else:
        response = "No file was uploaded"
        return render_template('dashboard.html', translated_message=response)
    
def process_file_with_translator(uploaded_file,language):
    # """
    # Processes file contents with the chatbot.
    # """
    # file_contents = uploaded_file.read().decode('utf-8')    
    # response = chat_with_bot_file(file_contents)
    return response

def translate_user_message(user_message,language):
     
    """
    Translates the input text to the selected language.

    Args:
        text (str): The text to translate.
    """
    print("HERE")
    try:
        # Initialize the translator
        translator = Translator()
        
        target_language = target_language_option(language)
        translated_sentence = GoogleTranslator(source='auto', target=target_language).translate(user_message)
        # translated_sentences = []
        # for sentence in nltk.sent_tokenize(user_message)[:10]:
        #     translated_sentence = GoogleTranslator(source='auto', target=target_language).translate(sentence)
        #     translated_sentences.append(translated_sentence)         
        return translated_sentence        
    except Exception as e:
        print("An error occurred while translating text:", e)
  
 
            