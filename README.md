# Programación Avanzada - Evaluación Final - Semana 9

Solución práctica para la **Evaluación Final** de la asignatura **Programación Avanzada**. El objetivo de esta entrega fue diseñar e implementar una aplicación de escritorio modularizada en Python conectada a una base de datos MySQL para el sistema de **Gestión de Flota - Agencia de Alquiler de Vehículos**, permitiendo realizar el flujo completo de operaciones CRUD (Agregar, Mostrar, Actualizar, Borrar) e informes de disponibilidad de manera segura e intuitiva.

## Conceptos Técnicos Aplicados

1. **Persistencia de Datos y Operaciones CRUD en MySQL:** Configuración de credenciales de acceso e integración mediante el conector de Python (`mysql.connector`) para realizar la creación (`INSERT`), lectura (`SELECT`), actualización (`UPDATE`) y eliminación (`DELETE`) de registros en la base de datos relacional.
2. **Arquitectura Modular y Separación de Responsabilidades:** Organización estructurada del proyecto mediante la segregación del código en módulos independientes (`db_connection.py`, `db_manager.py`, `gui.py` y `main.py`), desacoplando por completo la gestión de la conexión, la lógica de consultas a la base de datos y la capa visual de la interfaz gráfica.
3. **Diseño de Interfaz Gráfica e Interacción por Eventos:** Construcción de un panel interactivo en Tkinter con maquetación limpia mediante contenedores (`LabelFrame`, `Frame`), controles de interacción (`ttk.Treeview`, `ttk.Combobox`, `Scrollbar`, `Entry`, `Button`, `Radiobutton`) y enlace de eventos (*event binding*) para autocompletar formularios tras la selección de registros.

## Tecnologías utilizadas

- Python
- Tkinter
- MySQL Workbench

## Desarrollado por:

- Tamara Muñoz