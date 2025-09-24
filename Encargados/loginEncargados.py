from connectDb import connect

def login(name, contraseña):
    con= connect()
    cur= con.cursor()
    cur.execute("""SELECT name FROM usuarios WHERE name = ? AND pass = ?""", (name, contraseña))
    tabla = cur.fetchall()
    if len(tabla) > 0:
        con.close()
        return True
    else:
        print("Usuario o contraseña incorrectos")
        con.close()
        return False