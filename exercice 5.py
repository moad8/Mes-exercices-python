def est_palindrome(mot):
    longueur = len(mot)
    test = i
    test = test + longueur # test = test + len(mot)
    test = test - 1
    for in i range(o, 4):
        if mot[i] != mot[test]:
            return False
        test = test - 1
    return True

print(est_palindrome("radar")) # Affiche True