import urllib.request
import urllib.error
import errno
from os import remove, chdir, mkdir
from zipfile import ZipFile


class paqAdm():
    
    
    def __init__(self):
        pass
        
    def getlibrary(self,name, liburl, version='latest'):
        """funcion para manejar la descarga de la libreria comprimida y su descompresion y ubicacion"""
        # necesario para acceder al espacio release de github
        aux = '/releases/download/'
        # conformando la peticion con todas las variantes
        url = f"{liburl}{aux}{version}/{name}.zip"
        print(url)
        try:
            # creando directorio para almacenar los paquetes en local
            mkdir('modulos')
            # descargando release comprimido
            response = urllib.request.urlopen(url)
            
        except OSError as e:
            # continuando en caso de que el directorio modulos ya exista
            if e.errno != errno.EEXIST:
                print(e)
        except urllib.error.HTTPError:
                # manejando error de conexion (ejemplo respuesta 404)
                return 'error en la version a la que llamas'
        finally:
            try:
                response = urllib.request.urlopen(url)
            except urllib.error.HTTPError:
                return 'error en la version a la que llamas'
        
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
    
    
