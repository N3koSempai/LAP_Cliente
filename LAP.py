from modulos.repoadm import repoAdm
import modulos.paqadm
import sys


repo = repoAdm()

if sys.argv[1] == 'actualizar':
    repo.getrepo()
elif sys.argv[1] == 'instalar':
    if sys.argv[2] != None:
        repo.jsonSearch(sys.argv[2])
    else:
        print('escribe algun paquete')


