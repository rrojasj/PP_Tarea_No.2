# -------------------- #
# Alert styles:
# buttons
MB_OK = 0x0
MB_OKCXL = 0x01
MB_YESNOCXL = 0x03
MB_YESNO = 0x04
MB_HELP = 0x4000

# icons
ICON_EXCLAIM = 0x30
ICON_INFO = 0x40
ICON_STOP = 0x10
# -------------------- #

import tkinter as tk
import tkinter.messagebox as tkmb
from tkinter import Button
import ctypes

def menu():
    """
    function: menu()
    description: Muestra en pantalla las opciones de menu
    """
    print("\nMenu")
    print("[1] Ingresar una nueva pesca")
    print("[0] Salir del programa\n")

def init_win32(add_fishing):
    """
    function: init_win32()
    description: Ejecuta el programa para usuarios de Windows
    params: add_fishing
    """
    if add_fishing == 1:
        while add_fishing == 1:
            cant_shrimp = int(input("\nIngrese la cantidad de camarones por Libra:\n"))
            msg = validate_fishing(cant_shrimp)
            print(msg)

            menu()
            add_fishing = int(input("Seleccione una opción: "))

    elif add_fishing == 0:
        message = "Gracias por utilizar el sistema de selección de pesca."
        ctypes.windll.user32.MessageBoxW(0, message, "Info",  ICON_INFO)

    else:
        message = "Valor incorrecto. Trate nuevamente."
        ctypes.windll.user32.MessageBoxW(0, message, "Error",  ICON_STOP)

def init_MacOs(add_fishing):
    """
    function: init_MacOs()
    description: Ejecuta el programa para usuarios de MacOS
    params: add_fishing
    """
    if add_fishing == 1:
        while add_fishing == 1:
            cant_shrimp = int(input("\nIngrese la cantidad de camarones por Libra:\n"))
            msg = validate_fishing(cant_shrimp)
            print(msg)
            
            timeout=5000
            root = tk.Tk()
            root.withdraw()
            root.after(timeout, root.destroy)
            
            tkmb.showinfo(title='Info Box', message=msg, icon='info')
            

            menu()
            add_fishing = int(input("Seleccione una opción: "))

    elif add_fishing == 0:
        farewell = "Gracias por utilizar el sistema de selección de pesca."
        tkmb.showinfo(title='Info Box', message=farewell, icon='info')

    else:
        message = "Valor incorrecto. Trate nuevamente."
        tkmb.showinfo(title='Información', message=message, icon='warning')

def validate_fishing(cant_shrimp:int) -> str:
    """
    function: validate_fishing()
    description: Valida la información y determina el resultado
    params: validate_fishing
    """
    jumbo = range(1, 19)
    medium = range (19, 39)
    small = range (39, 56)
    shrimp_in = False
    valid_value = True
    shrimp = ""

    if cant_shrimp in jumbo:
        shrimp = "Jumbo"
        shrimp_in = True
    else:
        if cant_shrimp in medium:
            shrimp = "Mediano"
            shrimp_in = True
        else:
            if cant_shrimp in small:
                shrimp = "Chico"
            else:
                if cant_shrimp < 1:
                    valid_value = False
                else:
                    shrimp = "Extra Chico"
    if shrimp_in == True:
        msg = f"\n- Cantidad de camarones: {cant_shrimp}\n- Camarón tipo: {shrimp}\n- Pesca permitida: Si\n"
    else:
        if valid_value != False:
            msg =f"\n- Cantidad de camarones: {cant_shrimp}\n- Camarón tipo: {shrimp}\n- Pesca permitida: No\n"
        else:
            msg = "\nCantidad incorrecta. Por favor trate nuevamente."

    return msg