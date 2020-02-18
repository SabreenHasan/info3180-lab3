from flask import Flask, flash, redirect, render_template, request, url_for
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'l@b3p@$$w0rd'
app.config['MAI_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 
app.config['MAIL_PASSWORD'] = 

mail = Mail(app)
from app import views