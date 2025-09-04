import os
from cargaRegistros import cargarVenta, outOperario, inOperario
def limpiar():
     os.system('cls' if os.name=='nt'else 'clear')

def menuPrincipal():
    encargados={
         "javi" : "123",
         "alex" : "qwe",
         "juan" : "asd"
    }    
    print("Bienvenidos a Hamburguesas IT")
    user = input("Ingrese su usuario de encargado: ")
    password = input("Ingrese contraseña: ")
    if user in encargados and encargados[user] == password:
        return user
    else: 
         print("Usuario o contraseña incorrecto")
         limpiar()
         menuPrincipal()
    return
def menuEncargado():
    print("Recuerda, siempre hay que recibir al cliente con una sonrisa :D")
    print("1 - Ingreso nuevo pedido")
    print("2 - Cambio de turno")
    print("3 - Apagar sistema")
    opcion = pedirNum()
    limpiar()
    return opcion

def pedirNum():
    while True:
            try:
               return int(input())
            except ValueError:
                    print("Tiene que ingresar un numero valido")

def ConfirmarPed():
            op=input().upper()
            try:
                if op == "Y" or op == "N":
                    return op
            except ValueError:
                print("Tiene que ingresar una opcion")

def menu():
        while True:
            caja = 0
            encargado = menuPrincipal()
            inOperario(encargado)
            opcion=menuEncargado()
            

            while opcion == 1 or opcion == 2 or opcion == 3:
                if opcion == 1: 
                    nombre = input ("Ingrese nombre del cliente:")
                   
                    print("Ingrese cantidad Combo S: ")
                    comboS = pedirNum()
                    
                    print("Ingrese cantidad Combo D: ")
                    comboD = pedirNum()

                    print("Ingrese cantidad Combo T:")
                    comboT = pedirNum()
                    
                    print("Ingrese cantidad Flurby: ")
                    comboF = pedirNum()
                    
                    total = (comboS * 5) + (comboD * 6) + (comboT * 7) + (comboF * 2)
                    print("Total:", total)

                    print("Abona con: ")
                    abona=pedirNum()
                
                    vuelto= abona-total
                    print("Vuelto: ", vuelto)
                    print("¿Confirma Pedido? Y/N: ")
                    confPedido=ConfirmarPed()
                    if confPedido == "Y":
                        limpiar()
                    cargarVenta(nombre,comboS,comboD,comboT,comboF,total)
                    caja=+total
                    opcion = menuEncargado()

                elif opcion == 2:
                    outOperario(encargado,caja)
                    caja = 0
                    encargado = menuPrincipal()
                    inOperario(encargado)
                    opcion = menuEncargado()
                elif opcion == 3:
                     print("en opcion 3 while")
                     outOperario(encargado,caja)
                     print("Se ejecuto el outOperario")
                     return False
            break
menu()
