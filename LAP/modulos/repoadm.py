import shutil, json
import urllib.request
from io import BytesIO
from os import remove, chdir, mkdir
from os.path import exists
from zipfile import ZipFile


class repoAdm:
    def __init__(self):
        # Definiendo el origen de los repositorios.
        self.url = urllib.request.Request(
            'https://github.com/N3koSempai/LAP_Directory/archive/refs/heads/main.zip')

    def getrepo(self):
        if not exists('repo'):
            # Creando directorio para repo.
            mkdir('repo')

        try:
            # Descargando lista de paquetes en formato zip.
            response = urllib.request.urlopen(self.url)
            data = response.read()

        except Exception as err:
            print(f"ERROR: {err}")

        finally:
            # Verificando respuesta correcta del servidor.
            if response.status == 200:
                with ZipFile(BytesIO(data), 'r') as zipx:
                    # Extrayendo.
                    zipx.extractall('repo/')

                # Ajustando carpetas y borrando temporales
                shutil.move('repo/LAP_Directory-main/main.json', 'repo/main.json')
                shutil.rmtree('repo/LAP_Directory-main')

                return 'INFO: Repositorios actualizados.'
            else:
                raise ("sin respuesta del servidor de repositorios")

    def jsonSearch(self, actual_dir, library):
        if not exists('repo/main.json'):
            self.getrepo()

        # Abriendo archivo repo tipo json previamente descargado.
        with open("repo/main.json", 'r') as repolist:
            repolib = json.loads(repolist.read())

        try:
            # Buscando nombre de la paquete.
            for paquete in repolib.keys():
                if paquete == library:
                    return repolib[paquete]
                else:
                    print("ERROR: Paquete no encontrado.")

        except Exception:
            print("ERROR: Error en busqueda de la paquete")
