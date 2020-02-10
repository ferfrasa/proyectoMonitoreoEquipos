# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:45:35 2020

@author: user
"""

#Caractersiticas del procesador 

import psutil

#Frecuencia del procesador
print (psutil.cpu_freq())

#POrcentaje de uso del procesador 

print(psutil.cpu_percent())
"""Devuelve varias estadisticas de CPU como una tupla con nombre:
    ctx_switches: numero de cambios de contexto (voluntario + involuntario)
    desde el arranque.
    Interrupciones: número de interrupciones desde el arranque.
    soft_interrupts: número de interrupciones de software desde el arranque.
    syscalls: numero de llamadas al sistema desde el inicio.
    """
print(psutil.cpu_stats())
#Segundos que ha pasado la cpu en ejecucion
print(psutil.cpu_times())
#Promedio de carga de la CPU en los ultimos 15 minutos
print(psutil.getloadavg())

"""Memoria RAM y particiones"""

#uso de memoria RAM
print(psutil.virtual_memory())
#uso de la memoria de intercambio
print(psutil.swap_memory())
#particiones del disco duro
print(psutil.disk_partitions())




"""Recursos de red"""
#Medidor de cantidad de paquetes de llegada y envio
print(psutil.net_io_counters())
#Cantidad de conexiones disponibles
print(psutil.net_connections(kind='tcp'))

#kind es un filtro que puede configurarse como :'all',tcp,tcp4
#upd , udp4, inet, inet4, inet6, tcp6 , udp6

#Leer direcciones asociadas a la red
print(psutil.net_if_addrs())
#leer caracteristicas de la tarjeta de red
print(psutil.net_if_stats())



"""Senores del computador"""
#medir la bateria del computador (si la hay)
print(psutil.sensors_battery())
#uso de los ventiladores (si los hay)
#print(psutil.sensors_fans())

#Medir la temperatura (si hay sensor)
#print(psutil.sensors_temperatures())

#Usuarios del cpu
print(psutil.users())