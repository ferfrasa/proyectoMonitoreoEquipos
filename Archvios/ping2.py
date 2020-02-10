# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 16:13:38 2020

@author: user
"""

#Importar la libreria scapy
#scr1 e suna función que envia paquetes a la direccion inidcada
#ICMP el protocolo seleccionado
#IP es la dirección

#Scapy libreria para la manipulación de redes de computadoras
from scapy.all import sr1, IP, ICMP

#Definir la dirección de prueba del dispositivo

direccionIP= "192.168.0.1"

#llamar a la función sr1, timeout es un tiempo de espera

informacionRecibida= sr1(IP(dst=direccionIP)/ICMP(),timeout=2)
print (informacionRecibida)



# Show permite visualizar los datos recibidos
if informacionRecibida:
   informacionRecibida.show()
else:
    print('no se recibo')
