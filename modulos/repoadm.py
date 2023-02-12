import urllib.request
import os
from zipfile import ZipFile
import shutil
from os import remove, chdir, mkdir
import errno

class repoAdm():
    
    
    def __init__(self):
        self.url = 'https://github.com/N3koSempai/LAP_Directory/archive/refs/heads/main.zip'
        # definiendo el origen de los repositorios
    def getrepo(self):
        chdir(os.path.dirname(os.path.realpath(__file__)))
        try:
            response = urllib.request.urlopen(self.url)
            data = response.read()
            mkdir('../repo')
        except OSError as e:
            if e.errno != errno.EEXIST:
                print(e)
            else:
                pass
        except:
            print("error")
        finally:
            if response.status == 200:    
                with open('../repo/main.zip', 'wb') as compress:
                    compress.write(data)
                zipx = ZipFile('../repo/main.zip', 'r')
                zipx.extractall('../repo/')
                shutil.move('../repo/LAP_Directory-main/main.json', '../repo/main.json')
                shutil.rmtree('../repo/LAP_Directory-main')
                os.remove('../repo/main.zip')
            else:
             raise("sin respuesta del servidor de repositorios")
