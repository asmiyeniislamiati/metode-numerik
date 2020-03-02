import math as m

def inputData():
    a = float(input("Masukkan nilai batas awal a : "))
    b = float(input("Masukkan nilai batas awal B : "))
    p = float(input("Masukkan tingkat presisi : "))
    return (a,b,p)

def f(x):
    return 1/((x-3)**2+0.01)- 1/((x-0.8)**2+0.04)

def checkSyarat(a,b):
    if(f(a)*f(b)<=0):
        return True
    else:
        return False

def updateBatas(a,b):
    c = b - f(b)*((b-a)/(f(b)-f(a)))
    if(f(a)*f(c)<0):
        return (a,c)
    else:
        return (c,b)

def process(a,b,presisi):
    while(abs(f(a))>presisi and abs(f(b))>presisi):
        a,b=updateBatas(a,b)

    if(abs(f(a))>abs(f(b))):
        return b
    else:
        return a

def main():
    a,b,p=inputData()
    if(checkSyarat(a,b)):
        hasil=process(a,b,p)
        print("hasilnya adalah "+str(hasil)+" ,dengan nilai f(x) "+str(f(hasil)))
    else:
        print("Sorry Wrong A and B")


main()