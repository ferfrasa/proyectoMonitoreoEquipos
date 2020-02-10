# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:21:14 2020

@author: user
"""

#Importar la ñibreria os (Operating System)

import os
#Asigne a una variable la dirección IP
#del equipo con el que desee establecer una conexion

#IP="192.168.0.3"
IP="192.168.0.3"
#use el comando ping 

estado = os.system("ping "+IP)
print(estado)

#Publicar estado del equipo

if(estado==0):
    print ("Conexion establecida")
else:
    print("No se pudó establecer una conexión")
    
""" El comando solo determina si el equipo esta conectado a la red."""


    


    
