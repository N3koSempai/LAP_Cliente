import sys, os
# Elimina el prefijo LAP si quieres probarlo sin instalarlo mediante pip de lo contrario la importacion  # no funcionara correctamente
from LAP.modulos.repoadm import repoAdm
from LAP.modulos.paqadm import paqAdm

repo = repoAdm()
paq = paqAdm()
actual_dir = os.getcwd()
print(actual_dir)
if sys.argv[1] == 'actualizar':
    res = repo.getrepo()
    print(res)
elif sys.argv[1] == 'instalar':
    if sys.argv[2] != None:
        lib_url = repo.jsonSearch(actual_dir,sys.argv[2])
        paq.getlibrary(actual_dir, sys.argv[2], lib_url)
    else:
        print('escribe algun paquete')


