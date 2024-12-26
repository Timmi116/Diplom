from flask import Blueprint, render_template, request, redirect, url_for, make_response
from app.models import User
from app import db
import base64
from datetime import datetime

bp = Blueprint('routes', __name__, template_folder='templates')

@bp.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        age = request.form['age']
        gender = request.form['gender']
        email = request.form['email']
        password = request.form['password']
        
        user = User(username=username, age=age, gender=gender, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        
        response = make_response(redirect(url_for('.profile')))
        response.set_cookie('email', email, max_age=3600 * 24 )
        return response
    return render_template('register.html', title='Регистрация')

@bp.route('/profile/', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        email = request.cookies.get('email')

        date_of_birth = request.form['date_of_birth']
        place_of_birth = request.form['place_of_birth']
        address = request.form['address']
        biography = request.form['biography']
        
        user = User.query.filter_by(email=email).first()
        user.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        user.place_of_birth = place_of_birth
        user.address = address
        user.biography = biography
        db.session.commit()
        
        response = make_response(redirect(url_for('.upload_photo')))
        response.set_cookie('email', email, max_age=3600 * 24 )
        return response
    return render_template('profile.html', title='Профиль')

@bp.route('/upload_photo/', methods=['GET', 'POST'])
def upload_photo():
    if request.method == 'POST':
        email = request.cookies.get('email')

        file = request.files['photo']
        data = file.read()
        encoded_data = base64.b64encode(data)
        
        user = User.query.filter_by(email=email).first()
        user.profile_picture = encoded_data
        db.session.commit()
        
        return redirect(url_for('.congratulations'))
    return render_template('upload_photo.html', title='Загрузка фотографии')

@bp.route('/congratulations/')
def congratulations():
    return render_template('congratulations.html', title='Поздравления!')
