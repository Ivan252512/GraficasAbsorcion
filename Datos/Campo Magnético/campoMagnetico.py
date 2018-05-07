''' Grafica los espectros de absorción de los datos obtenidos en
formato ASC'''
import sys
sys.path.append("/home/ivan/Documents/Taller/Graficas")
import espectros as e

e.graficaSobrepuestas('Archivos/', e.getNombresArchivos('Archivos',
                      'D-Alanina  Magnetizada Petri.asc'), e.bandas, 'Campo Magnético')

e.aExcel('Archivos/', e.getNombresArchivos('Archivos',
                    'D-Alanina  Magnetizada Petri.asc'),'Campo Magnético')

e.CSVToASCII('Campo Magnético.csv')
