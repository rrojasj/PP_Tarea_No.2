
# jumbo = range(1, 18)

# print(jumbo)

# num = True

# if num in jumbo:
#     print("Es Jumbo")
# else:
#     print("No es Jumbo")

# -------------------- #
# CODE FOR WINDOWS USERS
# from cc_functions import *
# import ctypes

# menu()
# add_fishing = int(input("Seleccione una opción: \n"))

# try:
#     if add_fishing != 1:
#         if add_fishing == 0:
#             msg = "test"
#             print(msg)
# except:
#     ctypes.windll.user32.MessageBoxW(0, "No se permiten otros valores diferentes al menu.\nTrate nuevamente.", "Error",  ICON_STOP)
#     menu()
#     add_fishing = int(input("Seleccione una opción: "))
# -------------------- #

# -------------------- #
# CODE FOR MAC OS USERS
from cc_functions import *
import ctypes

menu()
add_fishing = int(input("Seleccione una opción: \n"))

if add_fishing != 1:
    if add_fishing == 0:
        msg = "test"
        print(msg)
        
    else:
        import tkinter as tk
        import tkinter.messagebox as tkmb
        from tkinter import Button
        message = "Valor incorrecto. Trate nuevamente."
        tkmb.showinfo(title='Información', message=message, icon='warning')


# ------ NOTIFICATION EXAMPLES ------ #

# ------ NOTIFICATION #1 ------ #

# import os

# def notify(title, text):
#     os.system("""
#               osascript -e 'display notification "{}" with title "{}"'
#               """.format(text, title))

# notify("Title", "Heres an alert")

# ------ NOTIFICATION #2 ------ #
# num1 =1
# num2 =2

# # An error box
# if(num1<num2):
#     tkmb.showinfo(title='Info Box', message='Info with warning icon', icon='warning')

# # A warning box 
# if(num1==num2):
#     tkmb.showwarning(title='Warning Box', message='Warning box with default icon', icon='warning')

# # An information box
# if(condition)
#     tkMessageBox.showinfo("Information","Created in Python.")


# ------ NOTIFICATION #3 ------ #
# import tkinter as tk
# import tkinter.messagebox as tkmb
# from tkinter import Button

# def show_message_boxes():
#     tkmb.showinfo(title='Info Box', message='Info with info icon', icon='info')
#     tkmb.showinfo(title='Info Box', message='Info with error icon', icon='error')
#     tkmb.showinfo(title='Info Box', message='Info with question icon', icon='question')
#     tkmb.showinfo(title='Info Box', message='Info with warning icon', icon='warning')

#     tkmb.showinfo(title='Info Box', message='Info box with info icon', icon='info')
#     tkmb.showerror(title='Error Box', message='Error box with default icon', icon='error')
#     tkmb.showwarning(title='Warning Box', message='Warning box with default icon', icon='warning')

#     tkmb.showinfo(title='Info Box', message='Info box with default icon')
#     tkmb.showerror(title='Error Box', message='Error box with default icon')
#     tkmb.showwarning(title='Warning Box', message='Warning box with default icon')

# window = tk.Tk()

# but = Button(window, text ='Click', command = show_message_boxes, width=20, height=10)
# but.grid(row=0, column=0)

# window.mainloop()
# -------------------- #
