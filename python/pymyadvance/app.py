from os import close
import config 
import mysql.connector
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

app.config.from_object(config)

def connection():
    return mysql.connector.connect(
        host = config.DB_CONFIG['host'],
        user = config.DB_CONFIG['user'],
        password = config.DB_CONFIG['password'],
        database = config.DB_CONFIG['database']
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
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
        return redirect(url_for("profileuser", nom=nom, prenom=prenom, username=username))
    

@app.route('/profileuser/<nom>/<prenom>/<username>')
def profileuser(nom, prenom, username):
    return render_template("profile.html", nom=nom, prenom=prenom, username=username)


@app.route("/liste", methods= ["GET", "POST"])
def alluser():
    conn = connection()
    mcursor = conn.cursor()
    mcursor.execute('SELECT * FROM our_user')
    liste = mcursor.fetchall()
    mcursor.close()
    conn.close()
    return render_template('listofall.html', liste=liste)

if __name__ == '__main__':
    app.run(debug=True)