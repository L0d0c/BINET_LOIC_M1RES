# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

""" EXERCICE 1 """

x=1
y=6
z=3.2

print(x%z)


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