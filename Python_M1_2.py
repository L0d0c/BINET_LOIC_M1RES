# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:32:10 2021

@author: loic binet
"""

import pandas as pd
import numpy as np

test = pd.read_csv('mower_market_snapshot.csv',sep=';') #lire CSV

test = test.replace('unknown', np.nan) #remplace unknow par NaN
test['prod_cost'] = pd.to_numeric(test['prod_cost']) #change le dtype au format float64 (argument en numérique)
test['prod_cost'] = test['prod_cost'].replace(np.nan, test['prod_cost'].mean())#remplace NaN par la moyenne des valeurs de la colonne 
print(test['prod_cost'])


test['warranty'] = pd.to_numeric(test['warranty'].str[0])
print(test['warranty'])    


test = pd.get_dummies(test.product_type, prefix='product_type')
print(test.head())

print(' ')
print(' ')


test2 = pd.read_csv('mower_market_snapshot.csv', sep=";")
test2.product_type = pd.Categorical(test2.product_type)
test2['product_type'] = test2.product_type.cat.codes
test2['product_type'] = pd.factorize(test2['product_type'])[0] + 1
print(test2['product_type'])


for numbers in test2.price:
        if numbers <= float(300):
            print(numbers, "1")
        elif numbers >= float(301) and numbers <= float(500):
            print(numbers, "2")
        else:
            print(numbers, "3")
            
            
            
### FONCTIONS ###

def F1(arg):
    test = pd.read_csv('mower_market_snapshot.csv',sep=';') #lire CSV
    test = test.replace('unknown', np.nan) #remplace unknow par NaN
    test[arg] = pd.to_numeric(test[arg]) #change le dtype au format float64 (argument en numérique)
    test[arg] = test[arg].replace(np.nan, test[arg].mean())#remplace NaN par la moyenne des valeurs de la colonne 
    print(test[arg])
F1('prod_cost')


def F2(arg):
    test = pd.read_csv('mower_market_snapshot.csv',sep=';')
    test[arg] = pd.to_numeric(test[arg].str[0])
    print(test[arg]) 
F2('warranty')    


def F3(arg):
    test = pd.read_csv('mower_market_snapshot.csv', sep=";")
    test.product_type = pd.Categorical(test.product_type)
    test[arg] = test.product_type.cat.codes
    test[arg] = pd.factorize(test[arg])[0] + 1
    print(test[arg])
F3('product_type')