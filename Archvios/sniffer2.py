# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:40:16 2020

@author: user
"""

#Se determina el origen de un paquete

#Ejemplo de deteccion de circulacion de paquetes
from scapy.all import *
#Define interface a través de la cual se realiza el escaneo
interface1 = "Ethernet"
interface2 ="Wi-Fi"

#Función para ejecutar el sniffer

def imprimirInformacion(paquete):
    #ip es un parametro heredado de la red
    ipLayer= paquete.getlayer(IP)
    print("Informacion del paquete: {src}: \n"
          .format(src=ipLayer.src))
    if ipLayer.haslayer( Raw ):
        #Informacion del paquete
        cabecera = ipLayer.getLayer( Raw ).load
        print(cabecera.decode(errors='ignore'))
   
    
if __name__ == "__main__":
   print("Presione ctrl+c para terminar")
   # llamar al hilo del sniffer
   sniff(iface= interface2, filter="ip", prn=imprimirInformacion)
   print("Termino el sniffer")
   


