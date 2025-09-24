from menu.menuPrincipal import limpiar
from validaciones.validaciones import pedirNum
def menuEncargado():
    print("Recuerda, siempre hay que recibir al cliente con una sonrisa :D")
    print("1 - Ingreso nuevo pedido")
    print("2 - Cambio de turno")
    print("3 - Apagar sistema")
    opcion = pedirNum()
    limpiar()
    return opcion