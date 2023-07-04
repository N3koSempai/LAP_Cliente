#!/bin/bash

# Verificar si la carpeta repo existe, y crearla si no existe
if [ ! -d "repo" ]
then
    mkdir repo
fi

# Verificar si el archivo main.json ya existe en la carpeta repo
if [ -f "repo/main.json" ]
then
    echo "el repositorio ya existe. no es necesario actualizarlo."
else
    # Verificar si el archivo main.zip ya existe en el directorio actual
    if [ -f "main.zip" ]
    then
        echo "archivo main.zip encontrado. descomprimiendo"
    else
        # Descargar el archivo usando wget o curl
        URL="https://github.com/N3koSempai/LAP_Directory/archive/refs/heads/main.zip"
        if command -v wget &> /dev/null
        then
            wget $URL
        else
            curl -O $URL
        fi
    fi

    # Descomprimir el archivo en el directorio actual y mover los archivos a la carpeta repo
    unzip -o main.zip -d . && mv -f main/* repo/ && rm -rf main

    echo "El repositorio se ha actualizado correctamente en la carpeta repo."
fi
