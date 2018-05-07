''' Grafica los espectros de absorción de los datos obtenidos en
formato ASC'''
import sys
sys.path.append("/home/ivan/Documents/Taller/Graficas")
import espectros as e

e.graficaSobrepuestas('Archivos/', e.getNombresArchivos('Archivos',
                      'L-Alanina Irradiada  Magnetizada Eppendorf.asc'),
                       e.bandas, 'Irradiados')

e.aExcel('Archivos/', e.getNombresArchivos('Archivos',
                    'L-Alanina Irradiada  Magnetizada Eppendorf.asc'), 'Irradiados')

e.CSVToASCII('Irradiados.csv')
