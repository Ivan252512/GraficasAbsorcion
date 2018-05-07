import sys
sys.path.append("/home/ivan/Documents/Taller/Graficas")
import espectros as e

e.graficaSobrepuestas('Archivos/', e.getNombresArchivos('Archivos',
                      'D-Alanina Irradiada Magnetizada Eppendorf.asc'),
                       e.bandas, 'Alanina')

e.graficaTodos('Archivos/',e.getNombresArchivos('Archivos',
                      'D-Alanina Irradiada Magnetizada Eppendorf.asc'),e.bandas)

e.aExcel('Archivos/', e.getNombresArchivos('Archivos',
                    'D-Alanina Irradiada Magnetizada Eppendorf.asc'))
