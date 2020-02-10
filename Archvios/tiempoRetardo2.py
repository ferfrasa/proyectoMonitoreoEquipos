# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:56:14 2020

@author: user
"""

#Tiempo de envio y recepción con Scapy

from scapy.all import *

#definir la cantidad de intentos que necesita (paquetes)

cantidadPaquetes= 4

#Definir la dirección IP
direccionIP= '192.168.0.3'
#Construcción de la estructura para empaquetar la información
#/medio/direccion/protocolo

paquete = Ether()/ IP(dst= direccionIP)/ICMP()

#variable tiempo
tiempo = 0.0

#Estructura para enviar cierta cantidad de paquetes

for i in range(cantidadPaquetes):
    #la funcion SRP implementa el ARP ping y retorna la MAC del equipo de dst
    ans , unans = srp(paquete, iface="Wi-Fi", filter='icmp', verbose=0 , timeout=2)
    print(ans)
    print(unans)
    if(ans):
        #Esta ubicacion del arreglo contiene los campos relacionados con la
        #información que llega
        rx = ans[0][1]
        print(rx)
        #Esta ubicacion del arreglo contiene los campos relacionados con la
        #información que se envia
        tx = ans[0][0]
        print(tx)
        #Cada variable de información (enviada y de llegada) tiene varios campos,
        #entre ellos el tiempo de ida y vuekta
        diferenciaDeTiempo= abs (rx.time - tx.sent_time)
        print ("ping: "+ str(i)+ " "+ str(diferenciaDeTiempo))
        tiempo+= diferenciaDeTiempo
    else:
         print("No conectado")
print("Tiempo total "+ str(tiempo))         
        
        
        
        