import os
from cargasDb.cargaVentas import cargarVenta
from cargasDb.fichero import inOperario, outOperario
import menuPrincipal
from validaciones.validaciones import pedirNum
def limpiar():
     os.system('cls' if os.name=='nt'else 'clear')
def menuEncargado():
    print("Recuerda, siempre hay que recibir al cliente con una sonrisa :D")
    print("1 - Ingreso nuevo pedido")
    print("2 - Cambio de turno")
    print("3 - Apagar sistema")
    opcion = pedirNum()
    limpiar()
    return opcion
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
                caja+=total
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
            else:
                print("Opcion incorrecta")
                opcion = menuEncargado()
menu()
