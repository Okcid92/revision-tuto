from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/listmovie")
def movie():
    movies = [
    {"titre": "Inception", "auteur": "Christopher Nolan", "annee": 2010},
    {"titre": "Parasite", "auteur": "Bong Joon-ho", "annee": 2019},
    {"titre": "The Matrix", "auteur": "Lana & Lilly Wachowski", "annee": 1999},
    {"titre": "Interstellar", "auteur": "Christopher Nolan", "annee": 2014},
    {"titre": "Pulp Fiction", "auteur": "Quentin Tarantino", "annee": 1994},
    {"titre": "The Godfather", "auteur": "Francis Ford Coppola", "annee": 1972},
    {"titre": "Spirited Away", "auteur": "Hayao Miyazaki", "annee": 2001},
    {"titre": "Fight Club", "auteur": "David Fincher", "annee": 1999},
    {"titre": "The Shawshank Redemption", "auteur": "Frank Darabont", "annee": 1994},
    {"titre": "The Dark Knight", "auteur": "Christopher Nolan", "annee": 2008}
]
    return render_template('listmovie.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)