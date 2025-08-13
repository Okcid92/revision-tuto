from xmlrpc.client import TRANSPORT_ERROR
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calcul():
    if request.method == "GET":
        return render_template('calculatrice.html')
    else: 
        nmba = request.form['nmb1']
        nmbb = request.form['nmb2']
        operation = request.form['operation']
        return redirect( url_for('result', a = nmba, b = nmbb, op = operation))


@app.route('/result/<int:a>/<int:b>/<op>', methods=["GET", "POST"])
def result(a,b,op):
    if op == "+":
        return f'the result of {a} + {b} is res = {a + b}'
    elif op == "-":
        return f'the result of {a} - {b} is res = {a - b}'
    elif op == "*":
        return f'the result of {a} * {b} is res = {a * b}'
    elif op == "/":
       return f'the result of {a} / {b} is res = {a / b}'
    else:
        return 'syntaxe error'
    

if __name__ == "__main__":
    app.run(debug=True)