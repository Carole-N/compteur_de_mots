# Message de bienvenue
print("Bienvenue dans le compteur de mots ! C'est une bien belle journée pour compter les mots, ne trouves-tu pas ?")

# Demander le texte à l'utilisateur
texte = input("Entrer ici le texte à analyser : ")

# Diviser le texte pour obtenir les mots
liste_mots = texte.split()

# Compter les mots
nombre_mots = len(liste_mots)

# Afficher le résultat
print("Nombre de mots :", nombre_mots)
