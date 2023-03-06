import urllib.request
import urllib.error
import errno
import os
from os import remove, chdir, mkdir
from zipfile import ZipFile


class paqAdm():
    
    
    def __init__(self):
        pass
        
    def getlibrary(self, actual_dir ,name, liburl, version='latest'):
        """funcion para manejar la descarga de la libreria comprimida y su descompresion y ubicacion"""
        # necesario para acceder al espacio release de github
        if version == 'latest':
            aux = '/releases/latest/download'
            url = f"{liburl}{aux}/{name}.zip"
        else:
            aux = '/releases/download/'
        # conformando la peticion con todas las variantes
        
            url = f"{liburl}{aux}{version}/{name}.zip"
        # conformando la peticion con todas las variantes
        chdir(os.path.realpath(f'{actual_dir}'))
        #print("path actual es" + os.getcwd())
        try:
            # creando directorio para almacenar los paquetes en local
            mkdir('modulos')

        except OSError as e:
            # continuando en caso de que el directorio modulos ya exista
            if e.errno != errno.EEXIST:
                print(e)

        try:
            # descargando release comprimido
            print(url)
            response = urllib.request.urlopen(url)
            print(response.getcode())
            if response.getcode() != 200:
                return "error. verifique que a escrito la version correctamente"
        except urllib.error.HTTPError as e:
             print("version de la libreria incorrecta")
             return False

        with open(f'./modulos/{name}.zip', 'wb') as lib:
            # creando archivo comprimido temporal
            lib.write(response.read())
            print('libreria instalada')
        # extrayendo el comprimido
        zipx = ZipFile(f'./modulos/{name}.zip', 'r')
        try:
            # crenado carpeta con el nombre de la libreria descargada
            mkdir(f'./modulos/{name}')
            # extrayendo todos los archivos dentro de la carpeta anterior
            zipx.extractall(f'./modulos/{name}')
        except OSError as e:
            if e.errno != errno.EEXIST:
                print(e)
            else:
                pass
        finally:
            # eliminando el comprimido temporal
            remove(f'./modulos/{name}.zip')
            
    
    
    
    
    
if __name__ == '__main__':
    p = paqAdm()
    p.getlibrary('lat_Libreria_prueba','https://github.com/N3koSempai/lat_libreria_prueba')
    
    
