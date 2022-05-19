#1. log view
from flask import Blueprint,render_template


#from website.models import User

views = Blueprint('views',__name__)    

@views.route('/')
@views.route('/home')

def home():
    return render_template("home.html")

@views.route('/credit')

def credit():
    return render_template("credit.html")


@views.route('/result')

def result():
    return render_template("result.html")