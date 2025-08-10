nmbr = []

def choisir():
    i=1
    nombre= int(input('entrer le nombre de chiffre a classer: ')) 
    while i <= nombre :
        nbr = int(input(f'entrer le nombre n{i}: '))
        nmbr.append(nbr)
        i += 1
    print (nmbr) 
    nmbr.sort()
    print (nmbr)
    nmbr.reverse()
    print (nmbr)

choisir()