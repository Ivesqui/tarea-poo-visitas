from visitas_app.modelos.visitante import Visitante


class VisitaServicio:
    """
    Capa de Servicio: Gestiona la lógica de negocio para el registro de visitas.
    Esta clase actúa como el controlador de datos en memoria, asegurando
    la integridad de la información antes de cualquier operación CRUD.
    """

    def __init__(self):
        """
        Inicializa el servicio con una lista privada de visitantes.
        Se usa el guion bajo (_) por convención para indicar que la lista
        no debe ser manipulada directamente desde fuera de esta clase.
        """
        self._visitantes = []

    def registrar_visitante(self, cedula, nombre, motivo):
        """
        Crea y almacena un nuevo objeto Visitante.

        Args:
            cedula (str): Identificador único del visitante.
            nombre (str): Nombre completo.
            motivo (str): Razón de la visita.

        Raises:
            ValueError: Si la cédula ya se encuentra registrada en el sistema.
        """
        # Regla de negocio: No permitir duplicados por cédula (ID único)
        if self.buscar_por_cedula(cedula):
            raise ValueError(f"Ya existe un visitante con la cédula {cedula}")

        # Instanciamos el modelo y lo agregamos a nuestra "base de datos" temporal
        nuevo = Visitante(cedula, nombre, motivo)
        self._visitantes.append(nuevo)
        return nuevo

    def obtener_todos(self):
        """
        Proporciona la lista completa de visitantes registrados.

        Returns:
            list: Una copia de la lista de visitantes para proteger la original
                  de modificaciones accidentales externas.
        """
        return list(self._visitantes)

    def buscar_por_cedula(self, cedula):
        """
        Busca un visitante específico dentro de la lista interna.

        Args:
            cedula (str): La cédula a buscar.

        Returns:
            Visitante: El objeto encontrado o None si no existe coincidencia.
        """
        for v in self._visitantes:
            # Normalizamos a string para evitar errores de comparación entre tipos
            if str(v.cedula) == str(cedula):
                return v
        return None

    def eliminar_visitante(self, cedula):
        """
        Elimina un registro de la lista basado en su identificador único.

        Args:
            cedula (str): Cédula del visitante a eliminar.

        Returns:
            bool: True si la eliminación fue exitosa, False si no se encontró el registro.
        """
        # Primero intentamos localizar el objeto en la lista
        visitante = self.buscar_por_cedula(cedula)

        if visitante:
            # remove() busca el objeto exacto y lo extrae de la lista
            self._visitantes.remove(visitante)
            return True

        return False