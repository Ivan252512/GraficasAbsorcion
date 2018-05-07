''' Grafica los espectros de absorción de los datos obtenidos en
formato ASC'''
import sys
sys.path.append("/home/ivan/Documents/Taller/Graficas")
import espectros as e

#e.graficaSobrepuestas('Archivos/', e.getNombresArchivos('Archivos',
#                      'L-Alanina  NM 1M P.asc'), e.bandasl, 'L-Alanina')

e.graficaSobrepuestas('Archivos/', e.getNombresArchivos('Archivos',
                      'L-Alanina  NM 1M P.asc'), e.bandasl, 'L-Alanina')
