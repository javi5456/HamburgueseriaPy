import sqlite3
def crearDB():
    encargados=[
        ("javier", "123"),
        ("lucas","123"),
        ("alex","qwe"),
        ("juanm","asd")
    ]
    con = sqlite3.connect("hamburgueseria.db")
    cur= con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass TEXT)")
    for encargado in encargados:
        cur.execute("""
        INSERT INTO usuarios (name, pass)
        VALUES (?, ?)
    """, encargado)
    cur.execute("CREATE TABLE IF NOT EXISTS fichero (id INTEGER PRIMARY KEY AUTOINCREMENT, encargado TEXT,fecha TEXT, evento TEXTO, caja FLOAT )")
    cur.execute("CREATE TABLE IF NOT EXISTS ventas(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, fecha TEXT, ComboS INTEGER, ComboD INTEGER, ComboT INTEGER, Flurby INTEGER, Total FLOAT)")
    con.commit()
    con.close()
crearDB()