import unittest
import os
print(os.getcwd())
from LAP.modulos.repoadm import repoAdm
from LAP.modulos.paqadm import paqAdm

class RepoDownload(unittest.TestCase):
    
        def test_file_exist(self):
            repo = repoAdm()
            direct = os.path.dirname(os.path.realpath(__file__))
            print(direct)
            res = repo.getrepo(direct)
            print(res)
            
            """comprobando que el archivo de repositorio se descarga correctamente"""
            self.assertTrue(os.path.exists('./repo/main.json'))

if __name__ == '__main__':
    unittest.main()
