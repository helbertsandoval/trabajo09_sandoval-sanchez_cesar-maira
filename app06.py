import libreria
import os

x=int(os.sys.argv[1])
y=int(os.sys.argv[2])
z=int(os.sys.argv[3])
q=int(os.sys.argv[4])

a=(x*y)
b=(z*q)

cantidad_mayor=libreria.cantidad_menor(a,b)
print("El mayor entre", a, " y", b, " es:", cantidad_menor)
