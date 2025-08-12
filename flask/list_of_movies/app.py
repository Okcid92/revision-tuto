from flask import Flask

app=Flask(__name__)

@app.route("/<name>")
def great(name):
    return f'hey {name}'

if __name__ == "__main__" :
    app.run(debug=True)