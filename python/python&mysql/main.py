from datetime import date
import email
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'dicko',
    password = 'mon926732@',
    database = 'gestion_user'
)

mycursor = mydb.cursor()



def afficher():
    mycursor.execute('SELECT * FROM user')
    for user in mycursor:
        print (user)

def ajouter():
    nom = input('entrer le nom: ')
    email = input("entre l'adresse mail: ")
    date_creation = input('entrer la date de creation: ')
    mycursor.execute('INSERT INTO user (nom, email, date_creation) VALUE (%s, %s, %s);', (nom, email, date_creation))
    mydb.commit()

def suprimer():
    mycursor.execute('SELECT * FROM user')
    for user in mycursor:
        print (user)

    id = int(input('entrer id du user a supprimer: '))
    mycursor.execute('DELETE FROM user WHERE id = %s', (id, ))
    mydb.commit()

def main():
    print('\n1. afficher\n2. ajouter\n3.supprimer\n4. quitter\n')
while True:
    main()
    choice = int(input("enter your choice here: "))
    match choice:
        case 1:
            afficher()
            continue
        case 2:
            ajouter()
            continue
        case 3:
            suprimer()
            continue
        case 4:
            break
