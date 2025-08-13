from flask import Flask, redirect, render_template, request, url_for
import random

app = Flask(__name__)

# Base de données des citations
citations = {
    "Motivation": [
        "Ne baisse jamais les bras, le début est toujours le plus difficile.",
        "Les rêves ne fonctionnent que si tu travailles dur.",
        "L'échec est seulement l'occasion de recommencer plus intelligemment.",
        "Si tu peux le rêver, tu peux le faire.",
        "Petit à petit, l'oiseau fait son nid."
    ],
    "Humour": [
        "Pourquoi les programmeurs confondent Halloween et Noël ? Parce que OCT 31 = DEC 25.",
        "Si tu veux rire, regarde ton code d'il y a 6 mois.",
        "Mon lit et moi, c’est une histoire d’amour… mais mon réveil est jaloux.",
        "Les pizzas, c’est comme le code : meilleures quand c’est bien fait.",
        "Si le plan A ne marche pas, il reste 25 autres lettres."
    ],
    "Vie": [
        "La vie, c'est comme une bicyclette, il faut avancer pour ne pas perdre l'équilibre.",
        "Ne compte pas les jours, fais que les jours comptent.",
        "Profite de chaque instant, il ne reviendra pas.",
        "Les petits bonheurs font les grands souvenirs.",
        "Sois toi-même, tous les autres sont déjà pris."
    ],
    "Succès": [
        "Le succès, c’est tomber sept fois et se relever huit.",
        "Travaille en silence, laisse ton succès faire du bruit.",
        "Le succès n’est pas la clé du bonheur, le bonheur est la clé du succès.",
        "Le succès n'arrive pas par hasard, il est le résultat d'efforts constants.",
        "L'action est la clé fondamentale de tout succès."
    ],
    "Amour": [
        "Aimer, ce n'est pas se regarder l'un l'autre, c'est regarder ensemble dans la même direction.",
        "L'amour est la poésie des sens.",
        "Un seul être vous manque, et tout est dépeuplé.",
        "L’amour ne consiste pas à se regarder, mais à regarder ensemble dans la même direction.",
        "L'amour est la seule chose qui grandit quand on le partage."
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("citation.html")
    
    type_citation = request.form.get("type")
    action = request.form.get("action")

    if action == "random":
        return redirect(url_for("randomcitation", type=type_citation))
    
    return render_template("tout.html", type=citations.get(type_citation, []))

@app.route("/randomcitation/<type>")
def randomcitation(type):
    if type in citations:
        return random.choice(citations[type])
    return "Erreur : catégorie non trouvée"

if __name__ == "__main__":
    app.run(debug=True)
