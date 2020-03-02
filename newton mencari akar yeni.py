
import math
iterasi= 80
x=3   #nilai tebakan
fx=x**3 - 12
batas=0.0001
i=0

while (i<=iterasi and abs (fx)>batas):
    fx=x**3 - 12
    ft=4**2 + 2
    x=x-(fx/ft)
    print ('x =',x,      'fx = ',fx)
    i=i+1
print ('akarnya adalah',x,'dengan iterasi sebanyak',i,'kali')