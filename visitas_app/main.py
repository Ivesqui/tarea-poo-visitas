import tkinter as tk
# Importamos las dos piezas clave
from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppVisitas


def main():
    """
    Punto de entrada de la aplicación.
    Aquí orquestamos la unión de las capas.
    """
    # 1. Creamos el root de Tkinter
    root = tk.Tk()

    # 2. Instanciamos el Servicio (La lógica)
    # Senior Tip: Al crearlo aquí, vive mientras la app esté abierta
    servicio_logica = VisitaServicio()

    # 3. Instanciamos la UI e INYECTAMOS el servicio
    # Nota como pasamos 'servicio_logica' como argumento
    app = AppVisitas(root, servicio_logica)

    # 4. Iniciamos el loop principal
    root.mainloop()


if __name__ == "__main__":
    main()

