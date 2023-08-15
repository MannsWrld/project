from flask_app import app
from flask import render_template, redirect, request, session
from flask import flash
from flask_app.models.user import User
from flask_app.models.instrument import Instrument
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def hello():
    return render_template("user.html")

@app.route('/dashboard')
def welcome():
    data = {
        'id' : session["user_id"]
    }
    return render_template("welcome.html", user=User.get_one_user(data),instrument=Instrument.all_instruments())

@app.route('/register', methods=['POST'])
def reg():
    print(request.form)
    if not User.validate_registration(request.form):
        return redirect('/')
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "password": pw_hash
        }
        session["user_id"] = User.insert_new_user(data)
        session["first_name"] = request.form['first_name']
        session['user_id'] = User.one_email(data).id
    return redirect("/dashboard")

@app.route('/login', methods=["POST"])
def log():
    if not User.validate_login(request.form):
        return redirect('/')
    else:
        data = {
            "email" : request.form["email"]
        }
        session['user_id'] = User.one_email(data).id
        return redirect('/dashboard')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
    

