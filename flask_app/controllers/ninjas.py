from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import dojo
from flask_app.models import ninja

@app.route('/ninjas')
def ninja_page():
    return render_template('ninja.html', dojos = dojo.Dojo.read_all()) # Why is it dojo.Dojo.read_all()?

@app.route('/create/ninjas', methods=['post'])
def create_ninja():
    ninja.Ninja.create(request.form) # Why is it ninja.Ninja? ninja = file and Ninja = class.
    return redirect('/')