from flask_app import app
from flask import render_template, redirect, session,request
from flask_app.models.instrument import Instrument
from flask_app.models.user import User

# create
@app.route('/new_instrument')
def create_1():
    return render_template("create.html")

@app.route('/create_instrument', methods=['POST'])
def create_2():
    print(request.form)
    if not Instrument.validate_instrument(request.form):
        return redirect('/new_instrument')
    data = {
        'name' : request.form['name'],
        'brand' : request.form['brand'],
        'type' : request.form['type'],
        'price' : request.form['price'],
        'year' : request.form['year'],
        'user_id' : request.form['user_id']
    }
    Instrument.create_new_instru(data)
    return redirect('/dashboard')

# read
@app.route('/view/instrument/<int:instruments_id>')
def view_instru(instruments_id):
    instrument_data = {
        'id' : instruments_id
    }
    return render_template("show_instrument.html", insrument_user=Instrument.join_all(instrument_data))


# update
@app.route('/edit/instrument/<int:instruments_id>')
def edit_instrument(instruments_id):
    data = {
        'id' : instruments_id
    }
    return render_template("edit_instrument.html", one_instrument=Instrument.get_one(data))

@app.route('/update/instrument', methods=['POST'])
def update_instrument():
    print(request.form)
    if not Instrument.validate_instrument(request.form):
        return redirect('/dashboard')
    Instrument.update_instrument(request.form)
    return redirect('/dashboard')

# delete
@app.route('/delete/<int:instruments_id>')
def delete(instruments_id):
    data = {
        'id' : instruments_id
    }
    Instrument.delete_Instru(data)
    return redirect('/dashboard')
