# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 16:50:19 2020

@author: loic binet
"""



# TD1

""" EXERCICE 1 """

x=1
y=6
z=3.2

print(x + y + z)
print(x - y - z)
print(x * y * z)
print(x%z)
print(y/z)
print(x ** z)

""" EXERCICE 2 """

s = 'je mange un oeuf'
t = ' dur'

print (s + t)
print(len(s)-1)


""" EXERCICE 3 """

a = 12 == 3 * 4
b = "général" > "colonel"
c = a != b

print (a)
print (b)
print(c)


""" EXERCICE 4 """

prenom = 'Loic'
nom = 'Binet'
nom_complet = prenom + ' ' + nom + ' '
initial = prenom[0] + nom[0] + ' '

print(nom_complet * 10)
print(initial * 10)


""" EXERCICE 5 """

p=input("quel est votre prenom ? ")
n=input("Quel est votre nom ? ")
print(p+' '+n)
print(p[0]+'.'+' '+n[0]+'.')
print("Premiere lettre du nom de famille: " + n[0])


""" EXERCICE 6 """

Temp = float(input("Quelle est la température ? "))

Fahrenheit = 9.0/5.0 * Temp + 32
print (Temp, "C = ", Fahrenheit, " F")

Celsius = (Temp - 32) * 5.0/9.0
print (Temp, "F = ", Celsius, " C")


""" EXERCICE 7 """

A=input('Entrer une valeur de verite pour A (entrer False ou True): ')
B=input('Entrer une valeur de verite pour B (entrer False ou True): ')
C=input('Entrer une valeur de verite pour C (entrer False ou True): ')

expression_bol=input('Entrer une expression Bolenne avec des "non", "ou", "et", et des parentheses: ')
expression_bol.replace('non', 'not')
expression_bol.replace('et', 'and')
expression_bol.replace('ou', 'or')
print (bool(expression_bol))





# TD2

""" Exercice 1 - 1 et 2 """

c = "X44bf38j23jdjgfjh737nei47"
c_num = ""
c_alpha = ""
for caracters in c:
    if str.isdigit(caracters) == True:
        c_num += caracters
    else:
        c_alpha += caracters

print(c_num, c_alpha)


"""" Exercice 1 - 3 """

cherche = "j23"
c.find(cherche)
if c.find(cherche) != -1:
    remplace = c.replace(cherche, "j24")
    print(remplace)


"""" Exercice 1 - 4 """

list = ["f","3","7"]
for i in list:
    indice = c.find(i)
    print(indice)
print("\n")


""" Exercice 2 - 1 """

# vérifier le text
texte = "We introduce here the Python language"
compteur = 0
for i in texte:
    compteur += 1
if compteur == len(texte):
    print("bon")
else:
    print("pas bon")

# compte caracteres sans compter espace
compteur_lettre = 0
for lettre in texte:
    if lettre == " ":
        pass
    else:
        compteur_lettre += 1
print(compteur_lettre)

# Compte les mots 
mots = len(texte.split())
print(mots)


"""" Exercice 2 - 2 """

# Oui toujours valable car utilisation de la méthode split
texte2 = "We introduce here the Python language. To learn more about the language, \
consider going through the excellent tutorial https://docs.python.org/ \
tutorial. Dedicated books are also available, such as \
http://www.diveintopython.net/."
mots = len(texte2.split())
print(mots)


""" Exercice 3 """

# tri mots ordre alphabétique

n = input("Entrer des mots separes par un espace : ")
mots_list = n.split()
trie = sorted(mots_list)
print(trie)


""" Exercice 4 """

Couleurs = ["Pique", "Trefle", "Carreau", "Coeur"]
valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi", "as"]
jeu = []
for c in Couleurs:
   for v in valeurs:
       carte = str(v) + " " + str(c)
       jeu.append(carte)


from random import shuffle
shuffle(jeu)
print(jeu)

joueur1 = []
joueur2 = []
joueur3 = []
joueur4 = []
for index in range(13):
    joueur1.append(jeu[index])
    joueur2.append(jeu[index + 1])
    joueur3.append(jeu[index + 2])
    joueur4.append(jeu[index + 3])

print(" J1 = " + str(joueur1))
print(" J2 = " + str(joueur2))
print(" J3 = " + str(joueur3))
print(" J4 = " + str(joueur4))



""" Exercice 5 """

print("\n\n")
with open('diamonds.csv', 'r') as f:
    diamants = f.readlines()
    print(len(diamants))
    print(diamants[0:3])
num_ligne = 0
for lines in diamants:
    num_ligne += 1
    final = lines.split(",")
    print(final, num_ligne)
f.close()

with open('diamonds.csv', 'r') as f:
    diamants_100 = [next(f) for i in range(100)]
    (diamants_100[0:20])
f.close()

with open('diamonds.csv', 'r') as f:
    diamants_prix = []
    diamants = f.readlines()
    for lines in diamants:
        data = lines.split(",")
        data = [i.replace('"', '').replace("\n", "") for i in data]
        try:
            diamants_prix += [float(data[4])]
        except ValueError:
            pass
f.close()
print(diamants_prix[0:20])


""" Exercice 6 - 1 """

id = input("Entrer prenom, nom et matricule étudiant séparés par un espace : ")
list = id.split(" ")
tuple = tuple(list)
print(tuple)
list_prin = []


""" Exercice 6 - 2 """



""" Exercice 6 - 3 """

for etudiant in list_prin:
    print(etudiant[0])


""" Exercice 7 - 1 à 4 """

fr_an = {
    "maison": "house",
    "voiture": "car",
    "canape": "sofa",
    "cerveau": "brain"
    }
for cle, valeur in fr_an.items():
    if cle == "cerveau":
        print(valeur)
    else:
        pass

an_fr = {}
for cle, valeur in fr_an.items():
    an_fr[valeur] = cle  
print(an_fr)


""" "Exercice 7 - 5 """

if "brain" in (an_fr): 
    print("bon")


""" "Exercice 7 - 6 """

for cle, valeur in an_fr.items():
    if an_fr[cle] == "cerveau":
        print("cle = " + cle, "valeur = " + valeur)


""" Exercice 7 - 7 à 10 """

new = {
    "maison": ["house", "home"],
    "voiture": ["car", "vehicle"],
    "canape": ["sofa", "couch"],
    "cerveau": ["brain", "mind"],
    "chemin" : ["path", "way"]
    }

for cle, valeur in new.items():
    if cle == "chemin":
        print ("la deuxième traduction du mot chemin est : " + valeur[1])

del new["chemin"]
print(new)


""" "Exercice 8 - 1 à 2 """



""" "Exercice 8 - 3 """



""" "Exercice 8 - 4 """



""" "Exercice 8 - 5 """



""" "Exercice 8 - 6 """