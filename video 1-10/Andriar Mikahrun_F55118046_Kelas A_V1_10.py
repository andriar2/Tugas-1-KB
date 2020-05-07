# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Video ke 2 "Generate Individu"
from random import randint
def individual (length, min, max):
   
    #video ke 3 "Generate Population"
    return [randint(min,max) for x in range (length)]
def population (count, length, min, max):
    return [individual (length, min, max)for x in range (count)]

#video ke 4 "function dari individu"
from operator import add
from functools import reduce
def fitness(individual, target):
    sum = reduce (add, individual,0)
    return abs (target-sum)

#Video ke 5 "Function grade rata-rata fitness dari populasi"
def grade(pop, target):
    summed = reduce(add, (fitness(x, target) for x in pop),0)
    return summed / (len(pop) * 1.0) 

#video 6 "function mutate"
from random import random
def mutatex(ga):
    chance_to_mutate = 0.6
    print('g awal',ga)
    n=0
    for i in ga:
        r=random()
        n=n+1
        print('random',r)
        if chance_to_mutate > r:
            print('pada individu',n,'terjadi mutasi')
            place_to_modify = randint(0,len(i)-1)
            print('yaitu pada angka ke',place_to_modify)
            i[place_to_modify] = randint(min(i), max(i))
        ga[n]=i
        print(i)
    return ga


#video 7 "Memilih Parent Berdasarkan fitness terbaik"
target=200
pop = population(7,5,0,100)
retain=0.3
mutate=0.6
random_select=0.3   

gradeda = [(fitness(x, target), x) for x in pop]
graded = [ x[1] for x in sorted(gradeda)]
gradeda0 =[ x[0] for x in sorted(gradeda)]
retain_length = int(len(graded)*retain)
parents = graded[:retain_length]
print("parents hasil pilihan fitness terbaik",parents)
#print(parent)

#video 8 "Tambah Parent Dengan Genetic Diversity"
for individu in graded[retain_length]:
    if random_select > random():
        parents.append(individu)
print("print hasil pilihan fitness terbaik dan Tambahan Genetic Diversity",parents)

#video 9 "Mutasi Lanjutan"
for individu in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individu)-1)
            individu[pos_to_mutate] = randint(min(individu), max(individu))
print("parents lanjutan hasil mutasi", parents) 

#video 10 "CrossOver"
Parents_length = len(parents)
desired_length = len(pop) - Parents_length
children = []
while len(children) < desired_length:
    malenumber = randint(0, Parents_length-1)
    femalenumber = randint(0, Parents_length-1)
    if malenumber!= femalenumber:
        male = parents[malenumber]
        female = parents[femalenumber]
        half = round(len(male)/2)
        child = male[:half] + female[half:]
        children.append(child)
parents.extend(children)
print("parent tambah child hasil penambahan crossover",parents)