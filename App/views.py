from flask import Blueprint, render_template, request, flash, jsonify
from . import db
import json
from werkzeug import exceptions



views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html', title ='home')




@views.errorhandler(exceptions.NotFound)
def handle_404(err):
    return render_template('errors/404.html'), 404

@views.errorhandler(exceptions.BadRequest)
def handle_405(err):
    return render_template('errors/405.html'), 405


@views.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return render_template('errors/500.html'), 500