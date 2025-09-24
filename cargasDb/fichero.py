from connectDb import connect
import time
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
    res.fetchall()
    con.commit()
    con.close()

def outOperario(encargado, caja):
    con = connect() 
    cur = con.cursor()
    try:
        nombre = str(encargado)
        monto = float(caja)
    except ValueError as e:
        raise TypeError("Uno de los parámetros no tiene el tipo correcto")
    
    f = open("rUsuarios.txt", "a")
    fecha = time.ctime()
    f.write("OUT " + fecha + " Encargad@ " + nombre + " $" + str(monto) + "\n")
    print("El encargado", nombre, "ha cerrado su caja con un total de $", monto)
    f.write("##################################################\n")
    f.close()
    cur.execute("""
        INSERT INTO fichero (encargado, fecha, evento, caja)
        VALUES (?, ?, ?, ?)
    """, (nombre, fecha, "OUT",monto))

    con.commit()
    con.close()