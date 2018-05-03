''' Grafica los espectros de absorción de los datos obtenidos en
formato ASC'''

import matplotlib.pyplot as plt
import numpy as np
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
def grafica(datos,nombre,bandas):
    datosx=[]
    datosy=[]
    minimos=[]
    for i in range(len(datos)):
        datosx.append(datos[i][0])
        datosy.append(datos[i][1])
        if(1<i<len(datos)-1 and datos[i-1][1]>datos[i][1] and
           datos[i][1]<datos[i+1][1]) and datos[i][1]<95 :
                minimos.append([datos[i][0],datos[i][1]])
    fig=plt.figure(figsize=(20,10))
    plt.plot(datosx,datosy)
    ax = fig.add_subplot(111)
    for i in bandas.keys():
        for j in minimos:
            if (j[0]-15<bandas.get(i)<j[0]+15):
                ax.annotate(i, xy=(j[0],j[1]), xytext=(j[0],j[1]),
                arrowprops=dict(facecolor='black'))
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
def graficaTodos(directorio,listaDeArchivos,bandas):
    for i in listaDeArchivos:
        f=open(directorio+i)
        archivo=f.read()
        datos=getDatos(archivo,limpia(archivo))
        grafica(datos,i[:len(i)-4],bandas)

'''Grafica sobreponiendo los datos de todos los archivos dentro de un
directorio'''
def graficaSobrepuestas(directorio,listaDeArchivos):
    fig = plt.figure(figsize=(20,10))
    plt.title('Sobrepuestas')
    plt.xlabel('Número de onda [cm⁻¹]')
    plt.ylabel('Transmitancia [%]')
    minimos=[]
    for dir in listaDeArchivos:
        f=open(directorio+dir)
        archivo=f.read()
        datos=getDatos(archivo,limpia(archivo))
        datosx=[]
        datosy=[]
        minimos=[]
        for i in range(len(datos)):
            datosx.append(datos[i][0])
            datosy.append(datos[i][1])
            if(1<i<len(datos)-1 and datos[i-1][1]>datos[i][1] and
               datos[i][1]<datos[i+1][1]) and datos[i][1]<95 :
                    minimos.append([datos[i][0],datos[i][1]])
        plt.plot(datosx,datosy,label=dir[:len(dir)-4])
        plt.legend(loc=2)
        ax = fig.add_subplot(111)
    for i in bandas.keys():
        for j in minimos:
            if (j[0]-15<bandas.get(i)<j[0]+15):
                ax.annotate(i, xy=(j[0],j[1]), xytext=(j[0],j[1]),
                arrowprops=dict(facecolor='black'))
    ax = plt.gca()
    ax.set_xlim(ax.get_xlim()[::-1])
    plt.savefig('Sobrepuestas.png',dpi=400)
    for i in bandas.keys():
        for j in minimos:
            if (j[0]-15<bandas.get(i)<j[0]+15):
                axzoom=fig.add_subplot(111)
                axzoom.set(xlim=(j[0]+400, j[0]-400),
                           ylim=(j[1]-20, j[1]+20), autoscale_on=False,
                           title='Zoom'+str(i))
                plt.savefig( 'Zoom'+str(i)+'.png', dpi=400)

'''Diccionario con las bandas de absorción de interés'''
bandas={'Estiramiento simétrico CH3':2608,'Estiramiento CH3':3089.6,
        'Estiramiento C=O':1619.81,'Estiramiento asimétrico NH2':2295.55,
        'Estiramiento OH':3439.71}

'''Uso de las funciones para obtener las gráficas'''
graficaTodos('Archivos/',getNombresArchivos('Archivos','allende1.asc'),bandas)
graficaSobrepuestas('Archivos/',getNombresArchivos('Archivos','allende1.asc'))
