from flask import Flask, render_template
from app.dbconnect import connectdb


app = Flask(__name__)

@app.route('/')
def index():
    conn = connectdb()
    return f"{conn}"

if __name__ == "__main__":
    app.run(debug=True)



