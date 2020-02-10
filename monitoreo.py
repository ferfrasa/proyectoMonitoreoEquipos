# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 20:26:49 2020

@author: user
"""

#Monitoreo con protocolo SNMP


#Importar la libreria SNMP
from pysnmp.hlapi import *


ipEquipo='192.168.0.3'
puerto=161


if __name__ == "__main__":
    #funcion para leer las caracteristicas del equipo a monitorear
    caracteristicas= getCmd( SnmpEngine(),
                             CommunityData('public'),
                             UdpTransportTarget((ipEquipo,puerto)),
                             ContextData(),
                             ObjectType(ObjectIdentity('SNMPv2-MIB','sysDescr',0)))
    #Extraer objetos de la lista
    informacion= next(caracteristicas)
    print(informacion)
    
def informacionSistemaOperativo(OID):
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
            
            
def     