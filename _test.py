import unittest
import os
print(os.getcwd())
from LAP.modulos.repoadm import repoAdm
from LAP.modulos.paqadm import paqAdm

class RepoDownload(unittest.TestCase):
        
        
        def test_file_exist(self):
            """test para la funcion que descarga el repositorio"""
            direct = os.path.dirname(os.path.realpath(__file__))
            repo = repoAdm()
            res = repo.getrepo()
            
            """comprobando que el archivo de repositorio se descarga correctamente"""
            self.assertTrue(os.path.exists('./repo/main.json'))
        
        def test_lib_install(self):
            """comprueba si la descarga de libreria funciona correctamente"""
            # si el anterior test falla este tambien al no encontrar el repositorio
            direct = os.path.dirname(os.path.realpath(__file__))
            paq = paqAdm()
            paq.getlibrary(direct,"lat_libreria_prueba","https://github.com/N3koSempai/lat_libreria_prueba")
            self.assertTrue(os.path.exists('./modulos/lat_libreria_prueba'))

if __name__ == '__main__':
    unittest.main()
