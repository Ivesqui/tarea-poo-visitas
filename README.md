# Universidad Estatal Amazónica

## Sistema de Registro de Visitantes - Arquitectura Modular

Este proyecto es una aplicación de escritorio desarrollada en **Python** utilizando la librería gráfica **Tkinter**. 
El sistema permite gestionar el flujo de visitantes a una oficina mediante un CRUD (Crear, Leer, Actualizar, Eliminar) básico, aplicando rigurosamente los principios de la **Programación Orientada a Objetos (POO)** y una arquitectura de capas.

El sistema permite:

- Registrar visitantes
- Visualizar visitantes registrados en una tabla
- Eliminar visitantes
- Limpiar campos del formulario

## 👤 Información del Estudiante
* **Nombre:** Christian Iván Estupiñán Quintero
* **Asignatura:** Programación Orientada a Objetos
* **Curso:** 2do A

---
## 🏗️ Arquitectura del Proyecto
El sistema sigue una estructura modular para separar la lógica de negocio de la interfaz de usuario:

* **`modelos/`**: Contiene la definición del objeto `Visitante` (Data Class).
* **`servicios/`**: El "cerebro" del sistema. Gestiona la lógica CRUD y la persistencia en memoria.
* **`ui/`**: Capa de presentación desarrollada en Tkinter.
* **`main.py`**: Punto de entrada que orquesta la inyección de dependencias.

```
visitas_app/
│
├── modelos/
│   ├── __init__.py
│   └── visitante.py
├── servicios/
│   ├── __init__.py
│   └── visita_servicio.py
├── ui/
│   ├── __init__.py
│   └── app_tkinter.py
├────── main.py
└────── README.me
```

## 🚀 Características Técnicas
* **Inyección de Dependencias:** La UI no crea el servicio, lo recibe, facilitando el desacoplamiento.
* **Encapsulamiento:** Atributos protegidos para mantener la integridad de los datos.
* **Validaciones:** Control de duplicados por cédula y manejo de campos vacíos mediante `messagebox`.
* **Uso de Dataclasses:** Implementación moderna para modelos de datos limpios.

## 🛠️ Requisitos
* Python 3.7 o superior.
* No requiere librerías externas (solo la librería estándar).

## 📥 Instalación y Ejecución

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu_usuario/tarea_poo_visitas.git](https://github.com/tu_usuario/tarea_poo_visitas.git)
    cd tarea_poo_visitas
    ```

2.  **Ejecutar la aplicación:**
    Desde la raíz del proyecto, ejecuta:
    ```bash
    python main.py
    ```

## 📝 Guía de Uso
1.  **Registrar:** Ingrese la cédula, nombre y motivo, luego presione "Registrar".
2.  **Visualizar:** Los datos aparecerán automáticamente en la tabla inferior.
3.  **Eliminar:** Seleccione una fila de la tabla y presione el botón "Eliminar".
4.  **Limpiar:** Presione "Limpiar" para vaciar los campos de entrada manualmente.



