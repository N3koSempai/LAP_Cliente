## Este es LAP (latino administrador de paquetes)

[![CodeFactor](https://www.codefactor.io/repository/github/n3kosempai/lap_cliente/badge)](https://www.codefactor.io/repository/github/n3kosempai/lap_cliente)

Un administrador de paquetes centrado en la facilidad y sencilles de uso para el usuario. Se intenta automatizar la mayor cantidad de cosas posibles, ser descriptivo con las dependencias y evitar soluciones raras como los espacios virtuales de python optando por la declaracion de dependencias y ubicacion de archivos en base a un arbol de directorios (como npm).

#### LAP esta en version alpha y abierto a colaboradores y donaciones

### principales comandos de LAP

- este comando descarga un archivo tipo repositorio donde se indica la ubicacion de las librerias disponibles actualmente.

```shell
python3 -m LAP actualizar
```

- este comando instala la ultima version de una libreria solicitada si esta se encuentra disponible en los repositorios (no uses <>)

```shell
python3 -m LAP instalar <nombre-de-la-libreria>
```

- Si deseas descargar una version en especifico deja un espacio despues del nombre de la libreria y especifica el numero de la version. (como estandar se a establecido temporalmente v#.#.# como forma de definir las versiones )

```shell
python3 -m LAP instalar <nombre-libreria> v3.0.0
```

### Ejemplo de uso
1- Nos situamos en un directorio y creamos la carpeta **prueba**.
```shell
mkdir prueba
```

2- En la carpeta previamente creada guardamos un archivo llamado **prueba.lat** y dentro de él ponemos lo siguiente:
```Latino
prueba = incluir("modulos\lat_libreria_prueba\main")
imprimir("5 + 5: " .. prueba.suma(5, 5))
```

3- Usamos **LAP** para instalar **lat_libreria_prueba**.
```shell
python3 -m LAP instalar lat_libreria_prueba
```

4- Luego desde la terminal llamamos a **prueba.lat**.
```shell
latino prueba.lat
```

5- Y si todo está correcto podremos ver en la terminal lo siguiente:
```
5 + 5: 10
```

### Como contribuir:

Usted puede contribuir al desarrollo de esta herramienta como sponsor a traves de donaciones o como desarrollador.

donaciones:

puedes enviar tus donaciones a las siguientes direcciones de criptomonedas. (algunas redes permiten escribir una nota en la trasaccion para que dejes un mensaje)

| criptomoneda  | direccion                                                         |
| ------------- | ----------------------------------------------------------------- |
| bitcoin:      | 13bTVYTvUgPBX12cowvrVBzwf4LaqR6rFp                                |
| litecoin:     | LgeBgdRwvmnj1y7heL5xueZg8DxuhmLhZj                                |
| TON (native): | EQBCIudz4Utv_0wdUGtkpEjW9_-R0DfPq35rl2aizaFA6iwx                  |
| NANO          | nano_1gnfjonzfsgdf5kbixfamnaeq784o5gbj6tsdpof7cioriyxodx5co8818kt |



como desarrollador:

para comenzar a desarrollar por su parte en esta herramienta siga estos pasos.

1. cree una carpeta vacia y cree un espacio virtual de python (necesita python) en ella. ejemplo:   
   
   ```shell
   python3 -m virtualenv venv
   ```

2. acceda a ese espacio virtual para descargar su version de LAP a continuacion
   
   ```shell
   # en linux
   # acceder al espacio virtual
   source venv/bin/activate
   # luego instalar LAP
   pip3 install LAP-latino-client
   ```

3. ahora en la carpeta: 
   
   ```uri
   venv/lib/<su-version-python/site-packages/LAP
   ```
   
   se encuentra la libreria donde usted puede hacer cambios en los archivos para probarlos en ese espacio virtual.

4. Como subo las nuevas actualizaciones?
   
   clone este repositorio en otra carpeta.
   
   sobrescriba los archivos en el repositorio clonado con los que usted modifico en su entorno virtual.

5. si tiene alguna duda hagamelas saber a traves de los Issues y seran respondidas
