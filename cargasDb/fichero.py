from connectDb import connect
import time
import sqlite3
def inOperario(nombre):
    con = connect()
    cur = con.cursor()
    try:
        nombre = str(nombre)
    except ValueError as e:
        raise TypeError("Nombre debe ser un String")
    f = open("rUsuarios.txt", "a")
    fecha = time.ctime()
    f.write("IN " + fecha + " Encargad@ " + nombre + "\n")
    f.close()
    cur.execute("""
        INSERT INTO fichero (encargado, fecha, evento, caja)
        VALUES (?, ?, ?, ?)
    """, (nombre, fecha, "IN",0))
    res = cur.execute("SELECT * FROM fichero")
    print(res.fetchall())
    con.commit()
    con.close()

def outOperario(nombre, monto):
    con = connect() 
    cur = con.cursor()
    try:
        nombre = str(nombre)
        monto = float(monto)
    except ValueError as e:
        raise TypeError("Uno de los parámetros no tiene el tipo correcto")
    
    f = open("archivo.txt", "a")
    fecha = time.ctime()
    f.write("OUT " + fecha + " Encargad@ " + nombre + " $" + str(monto) + "\n")
    f.write("##################################################\n")
    f.close()
    cur.execute("""
        INSERT INTO fichero (encargado, fecha, evento, caja)
        VALUES (?, ?, ?, ?)
    """, (nombre, fecha, "OUT",monto))
    res = cur.execute("SELECT * FROM fichero")
    print(res.fetchall())
    con.commit()
    con.close()