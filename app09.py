import libreria
import os
#se calcula el monto de dinero que se necesita para la compra de autos

ca=int(os.sys.argv[1])
u=int(os.sys.argv[2])

msg=libreria.compra_de_autos(ca,u)
print("el dinero necesario para la compra es:", msg)
