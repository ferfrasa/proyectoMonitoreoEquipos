# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 19:32:41 2020

@author: user
"""

#Protocolo SNMP
#Importar la libreria SNMP
from pysnmp.hlapi import *

#identificador del equipo
OID= "1.3.6.1.2.1.1.1.0"

ipEquipo='192.168.0.3'
puerto=161


if __name__ == "__main__":
    #funcion para leer las caracteristicas del equipo a monitorear
    e1, e2, e3, vb =next( getCmd( SnmpEngine(),
                             CommunityData('public', mpModel=0),
                             UdpTransportTarget((ipEquipo,puerto)),
                             ContextData(),
                             ObjectType(ObjectIdentity(OID)))
    )
   #Imprimir errores de indicacion
    if(e1):
        print("1. "+e1+"\n")
  #Imprimir errores de estado
    if(e2):
        print("2. "+e2+"\n")      
  #Imprimir errores de estado
    if(e3):
        print("3. "+e3+"\n")  
   #Imprimir errores de dispositivo
    if(vb):
        for i in vb:
            print(str(i)+"\n")        