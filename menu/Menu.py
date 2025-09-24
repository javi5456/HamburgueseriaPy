from cargasDb.fichero import inOperario, outOperario
from menu.menuEncargado import menuEncargado
from menu.menuPrincipal import menuPrincipal
from menu.opcion1 import opcion1


def menu():
        while True:
            caja = 0
            encargado = menuPrincipal()
            inOperario(encargado)
            opcion=menuEncargado()
            while True:
                if opcion == 1: 
                    opcion, caja = opcion1(caja)

                elif opcion == 2:
                    outOperario(encargado,caja)
                    caja = 0
                    encargado = menuPrincipal()
                    inOperario(encargado)
                    opcion = menuEncargado()
                elif opcion == 3:
                        outOperario(encargado,caja)
                        break
                else:
                    print("Opcion incorrecta")
                    opcion = menuEncargado()
                    print("Gracias por usar el sistema")
            break
