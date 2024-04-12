import sqlite3

db= sqlite3.connect("bd.sqlite3", check_same_thread= False)
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS listaTareas(id integer primary key autoincrement, nombre varchar(30), descripcion varchar(100))")

def creartarea(nombre: str, descripcion:str):
    cursor.execute("INSERT INTO listaTareas( nombre, descripcion) VALUES (?,?)",(nombre, descripcion))
    db.commit()

def borrartarea(id):
    cursor.execute("DELETE FROM listaTareas WHERE id = ?", (id))
    db.commit()

def mostrarTareas():
    res = cursor.execute("SELECT * FROM listaTareas")
    data= res.fetchall()
    return data