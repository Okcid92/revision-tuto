from flask import Blueprint, render_template
from db_connector import connection

list = Blueprint("list", __name__, template_folder='templates/list')


@list.route("/liste", methods= ["GET", "POST"])
def alluser():
    conn = connection()
    mcursor = conn.cursor()
    mcursor.execute('SELECT * FROM our_user')
    liste = mcursor.fetchall()
    mcursor.close()
    conn.close()
    return render_template('listofall.html', liste=liste)