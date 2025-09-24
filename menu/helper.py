import os

def ConfirmarPed():
            op=input().upper()
            while op != "Y" and op != "N":
                print("Tiene que ingresar una opcion")
                print("¿Confirma Pedido? Y/N: ")
                op = input().upper()
                limpiar()
            return op

def limpiar():
    os.system('cls' if os.name=='nt'else 'clear')