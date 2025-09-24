from menu.helper import limpiar
from Encargados.loginEncargados import login
def menuPrincipal():
    print("Bienvenidos a Hamburguesas IT")
    user = input("Ingrese su usuario de encargado: ")
    password = input("Ingrese contraseña: ")
    encargado = login(user, password)
    if encargado:
        return user
    else: 
         limpiar()
         print("Usuario o contraseña incorrecto")
         menuPrincipal()
    return