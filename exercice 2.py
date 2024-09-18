def somme_liste(liste):
    somme = 0
    for abc in liste:
        somme = somme + abc
    return somme

print(somme_liste([1, 2, 3, 4])) # Affiche 10