from flask import Blueprint, request, redirect, render_template, url_for
from db_connector import connection
import os

TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'auth')

auth = Blueprint("auth", __name__, template_folder=TEMPLATES_PATH, url_prefix='/auth')

@auth.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('auth/index.html')
    else: 
        nom = request.form['nom']
        prenom = request.form['prenom']
        username = request.form['username']
        password = request.form['password']
        conn = connection()
        mcursor = conn.cursor()
        mcursor.execute('INSERT INTO our_user (nom, prenom, username, password) VALUES (%s, %s, %s, %s)', (nom, prenom, username, password))
        conn.commit()
        mcursor.close()
        conn.close()
        return redirect(url_for('user.profileuser', nom=nom, prenom=prenom, username=username))
  