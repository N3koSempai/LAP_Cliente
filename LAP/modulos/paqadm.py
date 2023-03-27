import urllib.request
import urllib.error
import errno
import shutil, sys
from io import BytesIO
from os import remove, chdir, mkdir
from os.path import exists
from zipfile import ZipFile


class paqAdm():
    def getlibrary(self, actual_dir, name, liburl, version='latest'):
        """Metodo para manejar la descarga del paquete comprimido, su
        descompresion y ubicación"""

        # Necesario para acceder al espacio release de github
        if version == 'latest':
            aux = '/releases/latest/download'
            url = urllib.request.Request(f"{liburl}{aux}/{name}.zip")
        else:
            aux = '/releases/download/'

            # Conformando la petición con todas las variantes.
            url = urllib.request.Request(f"{liburl}{aux}{version}/{name}.zip")

        if not exists('modulos'):
            # Creando directorio para almacenar los paquetes en local.
            mkdir('modulos')

        try:
            # Descargando release comprimida.
            response = urllib.request.urlopen(url)

            if response.getcode() != 200:
                print(
                    'ERROR: Verifique que haya escrito la versión '
                    'correctamente.')
                return False

        except urllib.error.HTTPError as e:
            print('ERROR: Versión del paquete incorrecta.')
            return False

        with ZipFile(BytesIO(response.read()), 'r') as zipx:
            # Extrayendo el comprimido
            if exists(f'modulos/{name}'):
                shutil.rmtree(f'modulos/{name}')
                mkdir(f'modulos/{name}')

            zipx.extractall(f'modulos/{name}')
            print('INFO: Paquete instalado.')


if __name__ == '__main__':
    p = paqAdm()
    p.getlibrary(sys.argv[1], sys.argv[2])
