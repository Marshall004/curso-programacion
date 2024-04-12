import SS
import flet as ft
from flet import *
from datetime import datetime
import sqlite3

def main (page:Page):
    page.horizontal_alignment= 'center'
    page.vertical_alignment= 'center'
    page.add(
        Container(
            width= 400,
            height = 900,
            margin = -10,
            bgcolor = "blue300"
        )
     )
   
def main (page:ft.page) :
    def agregartarea(e):
        nombre = camponombre.value
        descripcion = campodescripcion.value
        SS.creartarea(nombre, descripcion)
    camponombre = ft.TextField(label="nombre tarea")
    campodescripcion = ft.TextField(label= "descripcion tarea")
    botonagregar = ft.ElevatedButton("agregar", on_click=agregartarea)
    page.add(camponombre,campodescripcion,botonagregar)
    def mostrar():
        tareas = SS.mostrarTareas()
        for tarea in tareas:
            page.add(ft.Text(tarea[1]+'- '+ tarea[2]))
    mostrar()

ft.app(target=main)