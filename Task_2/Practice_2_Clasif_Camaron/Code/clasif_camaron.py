from cc_functions import *
from sys import platform

menu()
add_fishing = int(input("Seleccione una opción: \n"))

print(platform)

# Code for Windows users 
if platform == "win32":
    init_win32(add_fishing)

# Code for MacOS users 
else:
    init_MacOs(add_fishing)
