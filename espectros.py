''' Grafica los espectros de absorción de los datos obtenidos en
formato ASCII'''

import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import Archivos

'''Retira todo el texto anterior a los datos numéricos'''
def limpia(archivo):
    i=0;
    cadena=""
    while(cadena!='#DATA'):
        cadena=archivo[i]+archivo[i+1]+archivo[i+2]+archivo[i+3]+archivo[i+4]
        i+=1
    return i+5

'''Convierte la cadena de datos a sus respectivos valores numéricos'''
def getDatos(archivo,indice):
    datos=[]
    cadena1=""
    cadena2=""
    while(indice<len(archivo)):
        while(indice<len(archivo) and archivo[indice]!='\t'):
            cadena1+=archivo[indice]
            indice+=1
        indice+=1
        while(indice<len(archivo) and archivo[indice]!='\n'):
            cadena2+=archivo[indice]
            indice+=1
        indice+=1
        if(cadena1!='' and cadena2!='' and cadena1!='\n' and cadena2!='\n'
           and cadena1!='\t' and cadena2!='\t'):
            datos.append([float(cadena1),float(cadena2)])
        cadena1=""
        cadena2=""
    return datos

'''Grafica los datos y asigna el nombre a la grafica de acuardo al nombre del
archivo'''
def grafica(datos,nombre):
    datosx=[]
    datosy=[]
    for i in range(len(datos)):
        datosx.append(datos[i][0])
        datosy.append(datos[i][1])
    plt.figure(figsize=(30,10))
    plt.plot(datosx,datosy)
    plt.title(nombre)
    plt.xlabel('Número de onda [cm⁻¹]')
    ax = plt.gca()
    ax.set_xlim(ax.get_xlim()[::-1])
    plt.ylabel('Transmitancia [%]')
    plt.savefig(nombre+'.png',dpi=400)

'''Obtiene los nombres de los archivos del directorio que recibe'''
def getNombresArchivos(directorio,primerArchivo):
    archivos = [
        i for i in listdir(directorio)
        if isfile(join(directorio,primerArchivo))]
    return archivos

'''Grafica individualmente los datos de todos los archivos dentro de un
directorio'''
def graficaTodos(directorio,listaDeArchivos):
    for i in listaDeArchivos:
        f=open(directorio+i)
        archivo=f.read()
        datos=getDatos(archivo,limpia(archivo))
        grafica(datos,i[:len(i)-4])

'''Grafica sobreponiendo los datos de todos los archivos dentro de un
directorio'''
def graficaSobrepuestas(directorio,listaDeArchivos):
    plt.figure(figsize=(30,10))
    plt.title('Sobrepuestas')
    plt.xlabel('Número de onda [cm⁻¹]')
    plt.ylabel('Transmitancia [%]')
    for i in listaDeArchivos:
        f=open(directorio+i)
        archivo=f.read()
        datos=getDatos(archivo,limpia(archivo))
        datosx=[]
        datosy=[]
        for j in range(len(datos)):
            datosx.append(datos[j][0])
            datosy.append(datos[j][1])
        plt.plot(datosx,datosy,label=i[:len(i)-4])
        plt.legend(loc=2)
    ax = plt.gca()
    ax.set_xlim(ax.get_xlim()[::-1])
    plt.savefig('Sobrepuestas.png',dpi=400)

'''Uso de las funciones para obtener las gráficas'''
graficaTodos('Archivos/',getNombresArchivos('Archivos','allende1.asc'))
graficaSobrepuestas('Archivos/',getNombresArchivos('Archivos','allende1.asc'))
