from connectDb import connect

def login(name, contraseña):
    cur= connect()
    res = cur.execute(""SELECT name FROM usuarios WHERE (name)"")
    tabla = res.fetchall()
    print(tabla)



login()