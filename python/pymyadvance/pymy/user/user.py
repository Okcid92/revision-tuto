from flask import Blueprint, render_template
import os

# chemin absolu vers templates/profile
TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'profile')

user = Blueprint("user", __name__, template_folder=TEMPLATES_PATH)

@user.route('/profileuser/<nom>/<prenom>/<username>', methods=['GET'])
def profileuser(nom, prenom, username):
    return render_template('profile/profile.html', nom=nom, prenom=prenom, username=username)