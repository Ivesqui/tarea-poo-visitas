import tkinter as tk
from tkinter import ttk, messagebox
#Importamos ttk y el módulo messagebox

class AppVisitas:
    """
    Capa de Interfaz de Usuario (UI): Gestiona la visualización y la interacción.
    Aplica el principio de Inyección de Dependencias al recibir el servicio
    en su constructor, manteniéndose desacoplada de la lógica de negocio.
    """

    def __init__(self, root, servicio):
        """
        Configura la ventana principal y vincula el servicio de datos.

        Args:
            root (tk.Tk): La instancia de la ventana principal de Tkinter.
            servicio (VisitaServicio): El motor lógico que gestiona los datos.
        """
        self.root = root
        self.servicio = servicio  # Dependencia inyectada
        self.root.title("Sistema de Registro de Visitantes - Smart Stock")
        self.root.geometry("600x400")

        # Construcción de la interfaz y carga inicial de datos
        self._crear_widgets()
        self.actualizar_tabla()

    # Evitamos que el usuario coloque más de 10 caracteres en el entry
    def _validar_cedula(self, texto):
        return (texto.isdigit() and len(texto) <= 10) or texto == ""

    def _crear_widgets(self):
        """
        Define la disposición de los componentes visuales en la ventana.
        Utiliza métodos privados (con _) para organizar la creación de la UI.
        """
        # --- Panel de Entrada: Agrupa los campos de texto con un LabelFrame ---
        frame_entrada = tk.LabelFrame(self.root, text="Datos del Visitante", padx=10, pady=10)
        frame_entrada.pack(fill="x", padx=10, pady=5)

        vcmd = (self.root.register(self._validar_cedula), '%P')

        # Campos de texto (Entry) con sus respectivas etiquetas (Labels)
        tk.Label(frame_entrada, text="Cédula:").grid(row=0, column=0, sticky="w")
        self.entry_cedula = tk.Entry(
            frame_entrada,
            validate='key',
            validatecommand=vcmd
        )
        self.entry_cedula.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_entrada, text="Nombre:").grid(row=1, column=0, sticky="w")
        self.entry_nombre = tk.Entry(frame_entrada)
        self.entry_nombre.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(frame_entrada, text="Motivo:").grid(row=2, column=0, sticky="w")
        self.entry_motivo = tk.Entry(frame_entrada)
        self.entry_motivo.grid(row=2, column=1, padx=5, pady=2)

        # --- Panel de Acciones: Botones para ejecutar las operaciones CRUD ---
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        # Vinculación de botones con sus métodos de acción mediante 'command'
        tk.Button(btn_frame, text="Registrar", command=self._registrar).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Eliminar", command=self._eliminar, fg="red").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Limpiar", command=self._limpiar_campos).pack(side="left", padx=5)

        # --- Visualización de Datos: Tabla dinámica (Treeview) ---
        self.tabla = ttk.Treeview(self.root, columns=("Cedula", "Nombre", "Motivo"), show="headings")
        self.tabla.heading("Cedula", text="Cédula")
        self.tabla.heading("Nombre", text="Nombre Completo")
        self.tabla.heading("Motivo", text="Motivo de Visita")
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)

    def _registrar(self):
        """
        Captura los datos del formulario y solicita al servicio el registro.
        Incluye validación visual de campos y manejo de errores lógicos.
        """
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        # Validamos mediante un if que el usuario no coloque menos de 10 dígitos en la cédula
        if len(cedula) != 10:
            messagebox.showerror("Error", "La cédula debe tener exactamente 10 dígitos")
            return

        # Validación simple de presencia de datos
        if not (cedula and nombre and motivo):
            messagebox.showwarning("Atención", "Todos los campos son obligatorios")
            return

        try:
            # Delegamos la creación al servicio (Capa Lógica)
            self.servicio.registrar_visitante(cedula, nombre, motivo)
            messagebox.showinfo("Éxito", "Visitante registrado correctamente")
            self._limpiar_campos()
            self.actualizar_tabla()
        except ValueError as e:
            # Captura errores de negocio (ej. cédula duplicada) enviados por el servicio
            messagebox.showerror("Error", str(e))

    def actualizar_tabla(self):
        """
        Refresca el Treeview obteniendo la versión más reciente de los datos
        desde la capa de servicio.
        """
        # Limpieza técnica: eliminamos las filas actuales antes de repoblar
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Iteración sobre los objetos recibidos desde el servicio
        for v in self.servicio.obtener_todos():
            self.tabla.insert("", "end", values=(v.cedula, v.nombres_completos, v.motivo_visita))

    def _limpiar_campos(self):
        """Vacia el contenido de todos los cuadros de texto en el formulario."""
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)

    def _eliminar(self):
        """
        Gestiona la eliminación de un registro seleccionado directamente
        desde la tabla Treeview.
        """
        # Identificamos la fila seleccionada por el usuario
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un visitante de la tabla para eliminar.")
            return

        # Extraemos los datos de la fila (específicamente la cédula en el índice 0)
        valores_fila = self.tabla.item(seleccion[0], "values")
        cedula_a_borrar = str(valores_fila[0])

        # Protocolo de seguridad: confirmación antes de destruir datos
        confirmar = messagebox.askyesno("Confirmar",
                                        f"¿Está seguro de eliminar al visitante con cédula {cedula_a_borrar}?")

        if confirmar:
            # Solicitamos la eliminación al servicio
            if self.servicio.eliminar_visitante(cedula_a_borrar):
                messagebox.showinfo("Éxito", "Visitante eliminado correctamente.")
                self.actualizar_tabla()
                self._limpiar_campos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el registro.")