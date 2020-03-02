import math

def f(x):
    return math.exp(x) - 8*x**3*x**2  

a = 3
b = 4
e = 0.0001
N = 100
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