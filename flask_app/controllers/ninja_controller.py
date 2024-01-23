from flask_app import app
from flask import render_template, request, redirect, url_for

from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja_models import Ninja
from flask_app.models.dojo_models import Dojo


# this route will create a new ninja and redirect to the ninja's new dojo page
@app.route("/create_ninja", methods = ["POST"])
def create_ninja():
    Ninja.add_ninja(request.form)
    dojo_id = request.form['dojo_id']
    return redirect(url_for('dojo_show',id = dojo_id))

