# Dans app.py
from flask import Flask, redirect, url_for
from auth.auth import auth
from user.user import user
from list.list import list

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(list)

# Page par défaut au lancement


if __name__ == '__main__':
    app.run(debug=True)