from connectDb import connect

def login(name, contraseña):
    con= connect()
    cur= con.cursor()
    cur.execute("""SELECT name FROM usuarios WHERE (name) VALUES (?) AND (contraseña) VALUES (?)""", (name, contraseña))
    tabla = cur.fetchall()
    print(tabla)
    if len(tabla) > 0:
        print("Login exitoso")
        con.close()
        return True
    else:
        print("Usuario o contraseña incorrectos")
        con.close()
        con.close()
        return False