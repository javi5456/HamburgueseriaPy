from cargasDb.cargaVentas import cargarVenta
from menu.menuEncargado import menuEncargado
from menu.helper import ConfirmarPed, limpiar
from validaciones.validaciones import pedirNum
def opcion1(caja):
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
    while vuelto < 0:
        print("El monto ingresado es insuficiente, por favor ingrese un monto mayor o igual al total")
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
        opcion=menuEncargado()
        return opcion, caja
    elif confPedido == "N":
        limpiar()
        print("Pedido cancelado")
        opcion=menuEncargado()
        return opcion, caja