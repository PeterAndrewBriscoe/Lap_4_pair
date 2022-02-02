from flask import Blueprint, redirect, render_template, request, flash, jsonify
from . import db
import json
from werkzeug import exceptions
from .models import Urls



views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html', title ='home')

@views.route('/new_link', methods = ['POST'])
def new_link():
    url = request.form.get('url')
    link = Urls(url=url)
    db.session.add(link)
    db.session.commit()

    return render_template('new_link.html', new_link = link.shortened_url, url=link.url)

@views.route('/<shortened_url>')
def to_new_link():
    link = Url.query.filter_by(shortened_url=shortened_url).first_or_404()
    return redirect(link.url)



@views.errorhandler(exceptions.NotFound)
def handle_404(err):
    return render_template('errors/404.html'), 404

@views.errorhandler(exceptions.BadRequest)
def handle_405(err):
    return render_template('errors/405.html'), 405


@views.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return render_template('errors/500.html'), 500