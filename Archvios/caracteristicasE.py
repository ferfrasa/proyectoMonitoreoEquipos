# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:21:28 2020

@author: user
"""

#Importar libreria psutil
import psutil

#indicar unidades a monitorear

diskUsage= psutil.disk_usage("C:\\")


def convertirBytesGigas(bytes):
    #convertir a gigabytes
    return bytes / 1024**3

if __name__ == "__main__":
    print("Espacio total: {:.2f} GB."
          .format(convertirBytesGigas(diskUsage.total)))
    print("Espacio disponible: {:.2f} GB."
          .format(convertirBytesGigas(diskUsage.free)))
    print("Espacio Usado: {:.2f} GB."
          .format(convertirBytesGigas(diskUsage.used)))
    print("Porcentaje de espacio usado: {}%."
          .format(diskUsage.percent))
          