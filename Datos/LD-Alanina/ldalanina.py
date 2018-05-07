''' Grafica los espectros de absorción de los datos obtenidos en
formato ASC'''
import sys
sys.path.append("/home/ivan/Documents/Taller/Graficas")
import espectros as e

e.graficaSobrepuestas('Archivos/', e.getNombresArchivos('Archivos',
                      'LD-Alanina No Magnetizada  Eppendorf.asc'), e.bandas, 'LD-Alanina')

e.aExcel('Archivos/', e.getNombresArchivos('Archivos',
                    'LD-Alanina No Magnetizada  Eppendorf.asc'), 'LD-Alanina')

e.CSVToASCII('LD-Alanina.csv')
