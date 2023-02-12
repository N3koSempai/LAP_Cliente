import urllib.request
import os
from zipfile import ZipFile
import shutil
from os import remove, chdir, mkdir
import errno
import json
class repoAdm():
    
    
    def __init__(self):
        # definiendo el origen de los repositorios
        self.url = 'https://github.com/N3koSempai/LAP_Directory/archive/refs/heads/main.zip'
        
    def getrepo(self):
        # estableciendo directorio actual que es dentro de modulos
        chdir(os.path.dirname(os.path.realpath(__file__)))
        
        
        try:
            # descargando lista de librerias en formato zip
            response = urllib.request.urlopen(self.url)
            data = response.read()
            # creando directorio para repo
            mkdir('../repo')
            
        except OSError as e:
            #capturando excepcion en caso de que exista el directorio
            if e.errno != errno.EEXIST:
                print(e)
            else:
                pass
        except:
            print("error")
        finally:
            # verificando respuesta correcta del servidor
            if response.status == 200:    
                with open('../repo/main.zip', 'wb') as compress:
                    #creando comprimido
                    compress.write(data)
                zipx = ZipFile('../repo/main.zip', 'r')
                # extrayendo
                zipx.extractall('../repo/')
                #ajustando carpetas y borrando temporales
                shutil.move('../repo/LAP_Directory-main/main.json', '../repo/main.json')
                shutil.rmtree('../repo/LAP_Directory-main')
                os.remove('../repo/main.zip')
            else:
             raise("sin respuesta del servidor de repositorios")
             
    def jsonSearch(self, library):
        #abriendo archivo repo tipo json previamente descargado
        with open("./repo/main.json", 'r') as repolist:
            repolib = json.loads(repolist.read())
        try:
            # buscando nombre de la libreria
            for i in repolib.keys():
                if i == library:
                    print(repolib[i])
                else:
                    print("no encontrada")
        except:
            print("error en busqueda de la libreria")    
