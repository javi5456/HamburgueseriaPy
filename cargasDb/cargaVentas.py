import time
import sqlite3
from connectDb import connect

def cargarVenta(nombre:str, ComboS:int, ComboD:int, ComboT:int, Flurby:int, Total:int):
    con = connect()
    cur = con.cursor()
    try:
        nombre = str(nombre)
        ComboS = int(ComboS)
        ComboD = int(ComboD)
        ComboT = int(ComboT)
        Flurby = int(Flurby)
        Total = float(Total)
    except ValueError:
        raise TypeError("Uno de los parámetros no tiene el tipo correcto")

    fecha = time.ctime()

    f = open("rVentas.txt", "a")
    f.write(f"{nombre}; {fecha}; {ComboS}; {ComboD}; {ComboT}; {Flurby}; {Total}\n")
    f.close()
    cur.execute("""
        INSERT INTO ventas (nombre, fecha, ComboS, ComboD, ComboT, Flurby, Total)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (nombre, fecha, ComboS, ComboD, ComboT, Flurby, Total))
    res = cur.execute("SELECT * FROM ventas")
    print(res.fetchall())
    con.commit()
    con.close()