import string

with open("file handling/name.txt", "r", encoding="utf-8") as f:
    contenu = f.read()

# On met tout en minuscule pour éviter que "Bonjour" et "bonjour" soient comptés comme deux mots
contenu = contenu.lower()

# On enlève toute la ponctuation (.,!? etc.)
for char in string.punctuation:
    contenu = contenu.replace(char, "")

# On découpe en mots
mots = contenu.split()

# Résultat
print(mots)
print(f"Le nombre de mots est {len(mots)}")
