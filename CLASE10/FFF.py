import SS
import flet as ft

def main (page:ft.Page):

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

ft.app(target = main) 