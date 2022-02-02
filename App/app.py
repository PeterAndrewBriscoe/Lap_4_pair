from flask import Flask, render_template, request, flash, jsonify
# from . import db
from flask_sqlalchemy import SQLAlchemy
import json
from werkzeug import exceptions



views = Flask(__name__)
views.config['SECRET_KEY'] = '5204956a60384b5685e8ce01e34235517b576fc6a461ff13'
views.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
views.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(views)


@views.route('/')
def home():
    return render_template('home.html', title ='home')

@views.route('/shortener', methods=['GET', 'POST'])
def shortener():
    if request.method == 'POST':
        original_url =request.form['original_url']
        return render_template('shortener.html', title='shortener', result = 'result')
    else:
        return render_template('shortener.html', title='shortener')




@views.errorhandler(exceptions.NotFound)
def handle_404(err):
    return render_template('errors/404.html'), 404

@views.errorhandler(exceptions.BadRequest)
def handle_405(err):
    return render_template('errors/405.html'), 405


@views.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return render_template('errors/500.html'), 500


if __name__ == '__main__':
    views.run(debug=True)