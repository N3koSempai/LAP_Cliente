import sys, os

"""Elimina el prefijo LAP si quieres probarlo sin instalarlo mediante pip, de
lo contrario la importacion no funcionará correctamente."""
from LAP.modulos.repoadm import repoAdm
from LAP.modulos.paqadm import paqAdm
from . import __version__


def mostrar_ayuda():
    print("Uso:")
    print("  LAP <comando> <opciones>\n")
    print("Commandos:")
    print("  LAP actualizar")
    print("    Actualiza la lista de los paquetes instalables.\n")
    print("  LAP instalar <paquete> <version>")
    print(
        "    Instala el paquete solitado, siempre y cuando se encuentre "
        "registrado.\n"
    )
    print("  LAP version")
    print("    Muestra la versión del administrador de paquetes.\n")
    print("  LAP ayuda")
    print("    Muestra ayuda para los comandos.\n")


repo = repoAdm()
paq = paqAdm()
actual_dir = os.getcwd()

if (len(sys.argv) == 1) or (sys.argv[1] == 'ayuda'):
    mostrar_ayuda()

elif sys.argv[1] == 'actualizar':
    res = repo.getrepo()
    print(res)

elif sys.argv[1] == 'instalar':
    if len(sys.argv) > 2:
        # Buscar paquete que corresponda en los repos internos.
        lib_url = repo.jsonSearch(actual_dir, sys.argv[2])

        # Obtener libreria comprimida.
        if lib_url is None:
            exit(1)
        elif len(sys.argv) > 3:
            paq.getlibrary(actual_dir, sys.argv[2], lib_url, sys.argv[3])
        else:
            paq.getlibrary(actual_dir, sys.argv[2], lib_url)

    else:
        print('ERROR: Debe especificar el paquete a instalar.')

elif sys.argv[1] == 'version':
    print(f"LAP {__version__}")

else:
    # Captura ordenes que no corresponden a ninguna válida.
    print(
        "ERROR: Orden no válida, el error puede estar en el argumento "
        f"'{sys.argv[1]}'"
    )
