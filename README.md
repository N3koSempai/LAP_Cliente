## Este es LAP (latino administrador de paquetes)

Un administrador de paquetes centrado en la facilidad y sencilles de uso para el usuario. Se intenta automatizar la mayor cantidad de cosas posibles, ser descriptivo con las dependencias y evitar soluciones raras como los espacios virtuales de python optando por la declaracion de dependencias y ubicacion de archivos en base a un arbol de directorios (como npm).

#### LAP esta en version alpha y abierto a colaboradores y donaciones

### principales comandos de LAP

- este comando descarga un archivo tipo repositorio donde se indica la ubicacion de las librerias disponibles actualmente.

```shell
python3 -m LAP actualizar
```

- este comando instala una libreria solicitada si esta se encuentra disponible en los repositorios (no uses <>)

```shell
python3 -m LAP instalar <nombre-de-la-libreria>
```
