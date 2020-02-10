# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 19:32:41 2020

@author: user
"""

#Protocolo SNMP
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