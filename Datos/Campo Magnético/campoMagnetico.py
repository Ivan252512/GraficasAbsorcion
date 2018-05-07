''' Grafica los espectros de absorción de los datos obtenidos en
formato ASC'''
import sys
sys.path.append("/home/ivan/Documents/Taller/Graficas")
import espectros as e

e.graficaSobrepuestas('Archivos/', e.getNombresArchivos('Archivos',
                      'D-Alanina  M 1M P.asc'), e.bandas, 'Campo Magnético')
