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
        # buscar libreria que corresponda en los repos internos
        lib_url = repo.jsonSearch(actual_dir,sys.argv[2])
        # obtener libreria comprimida
        if sys.argv[3] != None:
            print("aqui")
            paq.getlibrary(actual_dir, sys.argv[2], lib_url, sys.argv[3])
        else:
            paq.getlibrary(actual_dir, sys.argv[2], lib_url)
    else:
        print('escribe algun paquete')
# captura ordenes que no corresponden a ninguna valida
else:
    print(f"orden no valida, el error puede estar en el argumento '{sys.argv[1]}'")
