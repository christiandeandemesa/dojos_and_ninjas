from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def link():
    return redirect('/dojos')

@app.route('/dojos')
def dojo_page():
    return render_template('dojo.html', dojos = Dojo.read_all())

@app.route('/create/dojos', methods=['post'])
def create_dojo():
    #data = {
    #    'name': request.form['name']
    #    }
    #Dojo.create(data)
    Dojo.create(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def dojo_show(id):
    data = {
        'id': id
    }
    return render_template('dojo_show.html', dojo=Dojo.read_one_with_ninjas(data))