from setuptools import setup, find_packages
import os
VERSION = '0.0.2' 
DESCRIPTION = 'Administrador de paquetes de latino (LAP)'
LONG_DESCRIPTION = 'Este es el administrador de paquetes o modulos del lenguage de programacion latino'

# Configurando
setup(
       # el nombre debe coincidir con el nombre de la carpeta 	  
       #'modulomuysimple'
        name="LAP-latino-client", 
        version=VERSION,
        author="Alvaro Martinez",
        author_email="<alvarom12098@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['python', 'LAP', 'latino lenguaje de programacion'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Topic :: Software Development",
            "Operating System :: Unix",
            "Operating System :: Microsoft :: Windows"
        ]
)

print(os.getcwd())
