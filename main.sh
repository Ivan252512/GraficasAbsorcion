#!/bin/bash

#Corre todos los scripts escritos en python.
cd Datos

for p in *
    do
      cd "$p"
      python *py
      cd ..
    done
