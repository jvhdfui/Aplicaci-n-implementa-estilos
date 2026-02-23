import flet as ft

def main (page:ft.Page):
    page.title = "Prueba_1"
    page.window.min_width = 600
    page.window.min_height = 400

    texto_1 = ft.Text("Hola mundo desde Flet")

    page.add(texto_1)

if __name__ == "__main__":
    ft.run(main)
