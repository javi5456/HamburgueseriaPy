import os
from Encargados.loginEncargados import login
def limpiar():
     os.system('cls' if os.name=='nt'else 'clear')

def menuPrincipal():
    print("Bienvenidos a Hamburguesas IT")
    user = input("Ingrese su usuario de encargado: ")
    password = input("Ingrese contraseña: ")
    encargado = login(user, password)
    if encargado:
        return user
    else: 
         print("Usuario o contraseña incorrecto")
         limpiar()
         menuPrincipal()
    return