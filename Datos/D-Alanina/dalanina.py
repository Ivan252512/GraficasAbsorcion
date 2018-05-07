''' Grafica los espectros de absorción de los datos obtenidos en
formato ASC'''
import sys
sys.path.append("/home/ivan/Documents/Taller/Graficas")
import espectros as e

e.graficaSobrepuestas('Archivos/', e.getNombresArchivos('Archivos',
                      'D-Alanina  Magnetizada Petri.asc'), e.bandasd, 'D-Alanina')

e.aExcel('Archivos/', e.getNombresArchivos('Archivos',
                    'D-Alanina  Magnetizada Petri.asc'), 'D-Alanina')

e.CSVToASCII('D-Alanina.csv')
