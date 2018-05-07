''' Grafica los espectros de absorción de los datos obtenidos en
formato ASC'''

import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join
import Archivos
import pandas as pd

colores = ['black', 'blue', 'blueviolet', 'brown', 'chocolate', 'cornflowerblue',
           'cyan', 'darkblue', 'gold', 'goldenrod', 'gray', 'green',
           'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey',
           'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange',
           'darkorchid', 'darkred', 'darksalmon', 'darkseagreen',
           'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise',
           'darkviolet', 'deeppink', 'deepskyblue', 'dodgerblue', 'firebrick',
           'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo',
           'lime', 'limegreen', 'linen', 'magenta', 'maroon',
           'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple',
           'mediumseagreen', 'mediumslateblue', 'mediumspringgreen',
           'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod',
           'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip',
           'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple',
           'rebeccapurple', 'red', 'rosybrown', 'royalblue', 'saddlebrown',
           'tomato', 'turquoise', 'violet', 'yellow', 'yellowgreen']

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
    fig=plt.figure(figsize=(20, 12))
    plt.plot(datosx,datosy, color='k')
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
def graficaSobrepuestas(directorio,listaDeArchivos,bandasSobrepuestas, titulo):
    fig = plt.figure(figsize=(20,12))
    plt.title(titulo)
    plt.xlabel('Número de onda [cm⁻¹]')
    plt.ylabel('Transmitancia [%]')
    minimos=[]
    cont=0
    for dir in listaDeArchivos:
        todosLosMinimos=[]
        f=open(directorio+dir)
        archivo=f.read()
        datos=getDatos(archivo,limpia(archivo))
        datosx=[]
        datosy=[]
        for i in range(len(datos)):
            datosx.append(datos[i][0])
            datosy.append(datos[i][1])
            if(1<i<len(datos)-1 and datos[i-1][1]>datos[i][1] and
               datos[i][1]<datos[i+1][1]) and datos[i][1]<95 :
                    minimos.append([datos[i][0],datos[i][1]])
        plt.plot(datosx,datosy,label=dir[:len(dir)-4], color=colores[cont])
        cont+=1
        plt.legend(loc=2)
        ax = fig.add_subplot(111)
    for i in bandasSobrepuestas.keys():
        for j in minimos:
            if (j[0]-10<bandasSobrepuestas.get(i)<j[0]+10):
                ax.annotate(i, xy=(j[0],j[1]), xytext=(j[0],j[1]),
                arrowprops=dict(facecolor='black'))
                break
    ax = plt.gca()
    ax.set_xlim(ax.get_xlim()[::-1])
    plt.savefig(titulo+'.png',dpi=400)
    for i in bandasSobrepuestas.keys():
        for j in minimos:
            if (j[0]-15<bandasSobrepuestas.get(i)<j[0]+15):
                axzoom=fig.add_subplot(111)
                if (0<j[1]<60):
                    axzoom.set(xlim=(j[0]+200, j[0]-200),
                               ylim=(j[1]-30, j[1]+65), autoscale_on=False,
                               title=str(i))
                if (85<j[1]<100):
                    axzoom.set(xlim=(j[0]+200, j[0]-200),
                               ylim=(j[1]-25, j[1]+15), autoscale_on=False,
                               title=str(i))
                elif(60<=j[1]<=85):
                    axzoom.set(xlim=(j[0]+200, j[0]-200),
                               ylim=(j[1]-35, j[1]+35), autoscale_on=False,
                               title=str(i))
                plt.savefig(titulo+ ' ' + str(i)+'.png', dpi=400)

""" Ajunta los datos de todos los .asc y los convierte en un .csv"""
def aExcel(directorio,listaDeArchivos):
    nombres={}
    cont=0;
    for dir in listaDeArchivos:
        f=open(directorio+dir)
        archivo=f.read()
        datos=getDatos(archivo,limpia(archivo))
        datosx=[]
        datosy=[]
        for i in range(len(datos)):
            datosx.append(float(datos[i][0]))
            datosy.append(float(datos[i][1]))
        nombres.update({dir[:len(dir)-4] +'\n' + 'Transmitancia[%]' : datosy})
        cont+=1
    nombres.update({'Número de Onda [cm⁻¹]' : datosx})
    matrizDatos=pd.DataFrame(nombres).sort_index(axis=1,  ascending=False)
    matrizDatos.to_csv('Datos.csv')


'''Diccionario con las bandas de absorción de interés'''
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

bandasl={'ν NH3⁺, ν CH'.translate(SUB):3060, 'ν NH3⁺, ν CH'.translate(SUB):2990,
        'ν CH3, ν NH3⁺'.translate(SUB):2970, 'ν NH3⁺'.translate(SUB):2742,
        'ν CH3 simétrico'.translate(SUB):2603.25,'ν CH':3089.62,'ν C=O':1619.81,
        'ν NH2 asimétrico'.translate(SUB):2292.55, 'ν OH':3439.71,
        'δ NH3⁺ , ν CO2⁻'.translate(SUB):1566, 'δ CH3'.translate(SUB):1447,
        'ν CO2⁻ , δ CH3 , δ ΝCH'.translate(SUB): 1386,
        'δ CH3 , δ ΝCH, ν CCC'.translate(SUB): 1336, 'δ CCH': 1290,
        'ρ NH3⁺'.translate(SUB):1238, 'ρ NH3 , δ CCH'.translate(SUB):1157,
        'ρ CH3 , ν CN'.translate(SUB):1095,
        'δ CCH, ρ CH3 , ρ NH3 , ν C-CH3'.translate(SUB):1004,
        'ν CN, ν CCC': 897, 'ν CN, ν CCC': 832, 'ω CO2⁻'.translate(SUB):749,
        'ρ CH3 , ρ NH3 , δ CO2⁻'.translate(SUB):639,
        'ρ NH3'.translate(SUB):569, 'δ CCO, ν C-N':526, 'δ CCN':418,
        'τ CH3 , ω NH3⁺'.translate(SUB):321, 'δ CCC':275  }
bandasd={'δ NH3, ν asimétrico COO'.translate(SUB):1623,
         'ν asimétrico COO, δ NH3'.translate(SUB):1587,
         'δ asimétrica CH3':1456, 'ν simétrico COO'.translate(SUB):1414,
         'δ asimétrica CH3':1360, 'δ asimétrica CH3'.translate(SUB):1307,
         'β NH3':1239, 'ρ NH3'.translate(SUB): 1115,
         'ν simétrico CCNC'.translate(SUB):1015,
         'ν asimétrico CCNC, ρ CH3'.translate(SUB):919,
         '2ν CCNC, ρ CH3'.translate(SUB):850,}

bandas=bandasl
bandas.update(bandasd)
