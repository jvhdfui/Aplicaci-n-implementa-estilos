import flet as ft

def main(page:ft.Page):
    page.title = "Flet - estructuras"
    page.window.min_width = 900
    page.window.min_height = 600
    page.window.maximized = True

    #Manejo de estilos
    estilo_texto = ft.TextStyle(
        bgcolor = "#ebf34e", #color de fondo
        color = "#4407b4", #color de texto
        weight = ft.FontWeight.BOLD,
        font_family = "Arial",
        size = 28
    ) 

    estilo_texto2 = ft.TextStyle(
        bgcolor = "#4cd516", #color de fondo
        color = "#f70606", #color de texto
        weight = ft.FontWeight.BOLD,
        font_family = "Times New Roman",
        size = 24
    )

    estilo_texto3 = ft.TextStyle(
        bgcolor = "#46eaec", #color de fondo
        color = "#cc0ea3", #color de texto
        weight = ft.FontWeight.BOLD,
        font_family = "Calibri",
        size = 12
    )

    #Se crean los componentes
    texto1 = ft.Text("Arriba", style = estilo_texto)
    texto2 = ft.Text("Medio", style = estilo_texto2)
    texto3 = ft.Text("Bajo", style = estilo_texto3)
    
    page.add(texto1, texto2, texto3)

if __name__ == "__main__":
    ft.run(main)
