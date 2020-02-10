# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:41:42 2020

@author: user
"""

#Tiempo de retardo

#Importar la libreria os y time
import os
from time import time

#Asignar a una variable la direccion IP con que se
#deseea establecer la conexion

ip='192.168.0.5'

tiempoInicio= time()
estado= os.system("ping "+ip)
tiempoTranscurrido= time() - tiempoInicio
print(tiempoTranscurrido)