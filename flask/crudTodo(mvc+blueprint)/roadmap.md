<!-- Phase 1 — Préparation & setup

Installer l’environnement

Crée un environnement virtuel Python.

Installe Flask et les packages nécessaires (MySQL connector, PyYAML, etc.).

Initialiser le projet

Crée l’arborescence projet avec app/, templates/, static/, models/, routes/.

Prépare les fichiers config.py, db.py, db.yaml.

<!-- Init Git

Nouvelle branche flask-todo.

Faire ton premier commit “project skeleton”.

Phase 2 — Configuration 

Configurer la BDD

Remplis db.yaml avec host, user, password, db.

Vérifie que db.py peut établir une connexion. -->

Configurer Flask

Paramètres de base (secret key, debug mode).

Intégration de la lecture YAML pour la config.

Phase 3 — Modèle (MVC)

Créer le modèle Todo

Liste les champs : id, titre, description, status, date de création.

Prévois des méthodes pour CRUD (insert, select, update, delete).

Test de modèle

Vérifie que tu peux te connecter à la BDD et récupérer/ajouter des données.

Phase 4 — Routes & Blueprints

Créer le Blueprint Todo

Organiser toutes les routes CRUD sous /todos.

Planifier les routes

Liste de todos

Ajouter un todo

Modifier un todo

Supprimer un todo

Tester les routes

Vérifie qu’elles renvoient bien des réponses ou redirections.

Phase 5 — Templates & Frontend

Créer un template de base

layout.html avec header/footer.

Créer les pages spécifiques

todo_list.html pour afficher tous les todos.

add_todo.html et edit_todo.html pour les formulaires.

Intégrer le templating

Passer les données depuis Flask vers les templates.

Boucle sur les todos pour affichage dynamique.

Phase 6 — CRUD complet

Lire la liste des todos

Afficher la table depuis la BDD.

Ajouter un todo

Formulaire + POST.

Modifier un todo

Formulaire pré-rempli + POST.

Supprimer un todo

Route qui supprime et redirige.

Phase 7 — Polissage

Styling

Ajouter CSS ou framework (Tailwind / Bootstrap).

Validation

Vérifier les champs du formulaire (non vide, caractères spéciaux…).

Test complet

Tester toutes les fonctionnalités CRUD.

Git

Commit final + push sur GitHub.

Phase 8 — Bonus (optionnel)

Ajouter un système de filtre/status (terminé/en cours).

Ajouter pagination si beaucoup de todos.

Ajouter login utilisateur pour gérer ses propres todos.




my_todo_app/
│
├─ app/
│   ├─ __init__.py        # Création de l'app Flask + registration des Blueprints
│   ├─ config.py          # Config Python (DB, secret key, etc.)
│   ├─ db.py              # Gestion de la connexion à la BDD
│   ├─ db.yaml            # Config YAML de la BDD (host, user, password, db)
│   │
│   ├─ models/
│   │   ├─ __init__.py
│   │   └─ todo.py        # Définition de la table Todo et méthodes CRUD
│   │
│   ├─ routes/
│   │   ├─ __init__.py
│   │   └─ todo_routes.py # Routes CRUD pour la todo list
│   │
│   ├─ templates/
│   │   ├─ layout.html
│   │   ├─ todo_list.html
│   │   ├─ add_todo.html
│   │   └─ edit_todo.html
│   │
│   └─ static/
│       ├─ css/
│       │   └─ style.css
│       └─ js/
│           └─ script.js
│
├─ run.py                # Lance l'app
├─ requirements.txt      # Flask, PyMySQL ou mysql-connector, PyYAML etc.
└─ README.md
