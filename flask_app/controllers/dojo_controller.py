from flask_app import app
from flask import render_template, request, redirect

from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.dojo_models import Dojo
from flask_app.models.ninja_models import Ninja

@app.route('/')
def dojo_hub():
    return render_template('dojo_hub.html', full_dojo_list = Dojo.get_all())


@app.route("/add_dojo", methods = ["POST"])
def add_dojo():
    Dojo.add_dojo(request.form)
    return redirect('/')


@app.route("/dojo_show/<int:id>")
def dojo_show(id):
    return render_template('dojo_show.html', dojo = Dojo.get_one(id), ninja_list = Ninja.get_ninjas_in_dojo(id))


# this route directs to a page where you can create a new ninja
@app.route("/add_ninja_page")
def add_ninja_page():
    return render_template("add_ninja_page.html", full_dojo_list= Dojo.get_all())

