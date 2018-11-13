# -*- coding: utf-8 -*-
"""
Created on 16_09_2018
@author: 10042994
"""
#impoort Math libary 
import math as m
from functools import reduce 
 

def add(values):
    #checkc if the input are numbers otherwise return error
        return reduce(lambda x, y: x+y, values)
            
def divide(values):
    return reduce(lambda x, y: x/y, values)


def exponent(values):
    #return first ** second
    return reduce(lambda x, y: x**y, values)


def multiply(values):
    return reduce(lambda x, y: x*y, values)

def subtract(values):
    return reduce(lambda x, y: x-y, values)

def square_root(values):
    #return m.sqrt(first)
    return list(map(lambda x: m.sqrt(x), values))

def square(values):
    sqr = list(map(lambda x : x**2, values))
    return sqr

  #Returns x raised to the power y
def power(values):
    #return m.pow(first, second)
    return reduce(lambda x,y: m.pow(x, y), values)

def cube(values):
    cube = list(map(lambda x : x*x*x, values))
    return cube

def factorial(values):
    #return m.factorial(first)
    return list(map(lambda x: m.factorial(x), values))

def city_generator():
    yield("Konstanz")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")
    
#generate number * 2  
def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
   
def getOddNum(values):
    odd_numbers = list(filter(lambda x: x % 2, values))
    return odd_numbers
    
'''
print(add([1, 2, 3, 4])) 

print(divide([16, 4, 2, 1])) 

print(exponent([16, 4, 2, 1])) 


print(multiply([1, 2, 3, 4])) 

print(subtract([16, 4, 2, 1]))

print(power([1, 2, 3, 4])) 

print(square([1, 2, 3, 4])) 
print(cube([1, 2, 3, 4])) 

print(square_root([16, 4, 2, 1]))

print(factorial([5, 4, 2, 1]))

print(list(PowTwoGen(4)))
print(getOddNum([1,3,4,6,8]))
'''

