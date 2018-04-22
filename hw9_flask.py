from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

file = open('/home/khm2120/hw9/inspiration.txt', 'r') 
data = file.readlines()

@app.route('/')
def give_quote():
    return render_template(
            'hw9template.html',
            quote=random.choice(data),
            )