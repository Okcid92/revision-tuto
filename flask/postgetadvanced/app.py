import os
import uuid
import pandas as pd
from flask import Flask, Response, render_template, request, send_from_directory

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'dicko' and password == '12345':
            return 'success'
        else:
            return 'failure'
        

@app.route('/file_upload', methods=['GET','POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    else:
        return 'no content'
    
@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']
    df = pd.read_csv(file)
    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={
            'Content-Disposition' : 'attachment ; filename = fichier.csv'
        }
    )
    return response

@app.route('/convert_csv_two', methods=["POST"])
def convert_csv_two():
    file =request.files['file']
    df = pd.read_csv(file)
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    filename = f'{uuid.uuid4}.csv'
    df.to_csv(os.path.join('downloads', filename))

    return render_template('download.html', filename=filename)


@app.route('/download<filename>')
def download(filename):
    return send_from_directory('downloads', filename, download_name='result.csv')

if __name__ == "__main__":
    app.run(debug=True)