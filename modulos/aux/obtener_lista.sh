#!/bin/bash

# Leer el archivo main.json de la carpeta repo
JSON=$(cat ../repo/main.json)

# Convertir el JSON a un diccionario de Bash
declare -A DICCIONARIO=$(echo "$JSON" | jq -r 'to_entries | map("\(.key)=\(.value|tostring)") | .[]' | sed 's/""/"/g' | sed 's/\\"/"/g' | sed 's/\\n/ /g' | awk -F= '{print "[\""$1"\"]=\""$2"\""}' | paste -sd " " - | sed 's/^/declare -A DICCIONARIO=(/g' | sed 's/$/)/g')

# Devolver el diccionario como valor
eval "$DICCIONARIO"