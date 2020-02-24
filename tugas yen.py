# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:58:11 2020

@author: asus
"""

import math

def f(x):
    return math.exp(x) - 8*x**3*x**4  

a = 2
b = 3
e = 0.001
N = 1000
if f(a)*f(b)>0:
    print ("Nilai yang dimasukkan tidak mengurung akar persamaan")
    a = int (input("Masukkan nilai batas bawah = "))
    b = int (input("Masukkan nilai batas atas = "))
iterasi = 0

print ('=========================')
print ('   c              f(c)')
print ('=========================')


while True:
    iterasi +=1
    c = (a+b)/2
    if f(a)*f(c) <0:
        b=c
    else:
        a=c
    print ('{:7.5f}\t {:+15.10f}'. format (c, f(c))) #\t memindahkan 1 tab
    if abs (f(c)) < e or iterasi >= N:
        break

print ('=========================')