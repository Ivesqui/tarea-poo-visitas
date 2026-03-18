from dataclasses import dataclass
"""importamos dataclass para almacenar datos de visitante"""

@dataclass
class Visitante:
    """Clase con atributos dataclass para representar visitantes"""

    cedula: str
    nombres_completos: str
    motivo_visita: str

    """Por qué elegí esta forma de inicializar las variables
    1. Código limpio: Me ahorré el __init__, getters repetitivos y el __str__
    2. dataclass ya genera un __repr__(similar al __str__)
    3. Es más legible cualquiera que lea el código sabrá que es un
    contenedor de datos puro."""




