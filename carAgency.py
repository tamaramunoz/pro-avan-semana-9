import tkinter as tk
import styles as st
from tkinter import ttk, messagebox
from mysql.connector import Error
from database import DatabaseManager

class AgenciaVehiculosApp:
    def __init__(self, root):
        self.root = root
        self.root.title(st.WINDOW_TITLE)
        self.root.geometry(st.WINDOW_GEOMETRY)
        self.root.resizable(*st.WINDOW_RESIZABLE)

        # Instancia del Database Manager
        self.db = DatabaseManager()
        exito, mensaje = self.db.inicializar_conexion()
        if not exito:
            messagebox.showerror("Error de Conexión", f"No se pudo conectar a MySQL:\n{mensaje}")

        # Variables de Control
        self.id_var = tk.StringVar()
        self.marca_var = tk.StringVar()
        self.modelo_var = tk.StringVar()
        self.anio_var = tk.StringVar()
        self.combustible_var = tk.StringVar(value="Gasolina")
        self.disponible_var = tk.BooleanVar(value=True)

        # Construcción de la Interfaz
        self.crear_interfaz()

        if exito:
            self.mostrar_vehiculos()

    def crear_interfaz(self):
        # 1. CONTENEDOR: Formulario
        frame_form = tk.LabelFrame(self.root, **st.FRAME_FORM_CONFIG)
        frame_form.pack(fill="x", padx=15, pady=10)

        tk.Label(frame_form, text="Marca:").grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(frame_form, textvariable=self.marca_var, width=28).grid(row=0, column=1, pady=5, padx=5)

        tk.Label(frame_form, text="Modelo:").grid(row=0, column=2, sticky="w", pady=5, padx=(15, 0))
        tk.Entry(frame_form, textvariable=self.modelo_var, width=28).grid(row=0, column=3, pady=5, padx=5)

        tk.Label(frame_form, text="Año:").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(frame_form, textvariable=self.anio_var, width=28).grid(row=1, column=1, pady=5, padx=5)

        tk.Label(frame_form, text="Combustible:").grid(row=1, column=2, sticky="w", pady=5, padx=(15, 0))
        combo_comb = ttk.Combobox(
            frame_form, 
            textvariable=self.combustible_var, 
            values=["Gasolina", "Diésel", "Híbrido", "Eléctrico"], 
            state="readonly", 
            width=26
        )
        combo_comb.grid(row=1, column=3, pady=5, padx=5)

        tk.Label(frame_form, text="Estado:").grid(row=2, column=0, sticky="w", pady=5)
        frame_radio = tk.Frame(frame_form)
        frame_radio.grid(row=2, column=1, columnspan=3, sticky="w", pady=5)
        tk.Radiobutton(frame_radio, text="Disponible", variable=self.disponible_var, value=True).pack(side="left", padx=5)
        tk.Radiobutton(frame_radio, text="En Mantenimiento / Reservado", variable=self.disponible_var, value=False).pack(side="left", padx=15)

        # 2. CONTENEDOR: Botones
        frame_botones = tk.Frame(self.root, pady=5)
        frame_botones.pack()

        tk.Button(frame_botones, text="Agregar", command=self.agregar_vehiculo, **st.BTN_ADD).grid(row=0, column=0, padx=4)
        tk.Button(frame_botones, text="Actualizar", command=self.actualizar_vehiculo, **st.BTN_UPDATE).grid(row=0, column=1, padx=4)
        tk.Button(frame_botones, text="Borrar", command=self.borrar_vehiculo, **st.BTN_DELETE).grid(row=0, column=2, padx=4)
        tk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos, **st.BTN_CLEAR).grid(row=0, column=3, padx=4)
        tk.Button(frame_botones, text="Informe", command=self.generar_informe, **st.BTN_REPORT).grid(row=0, column=4, padx=4)

        # 3. CONTENEDOR: Tabla
        frame_tabla = tk.LabelFrame(self.root, **st.FRAME_TABLE_CONFIG)
        frame_tabla.pack(fill="both", expand=True, padx=15, pady=10)

        self.tabla = ttk.Treeview(frame_tabla, columns=st.TABLE_COLUMNS, show="headings", height=10)

        for col in st.TABLE_COLUMNS:
            self.tabla.heading(col, text=col)
            config = st.TABLE_COLUMN_CONFIGS.get(col, {})
            self.tabla.column(col, **config)

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tabla.bind("<<TreeviewSelect>>", self.cargar_seleccion)

    def agregar_vehiculo(self):
        marca = self.marca_var.get().strip()
        modelo = self.modelo_var.get().strip()
        anio = self.anio_var.get().strip()
        combustible = self.combustible_var.get()
        disponible = self.disponible_var.get()

        if not marca or not modelo or not anio:
            messagebox.showwarning("Campos Incompletos", "Por favor ingrese Marca, Modelo y Año.")
            return

        try:
            self.db.agregar_vehiculo(marca, modelo, anio, combustible, disponible)
            messagebox.showinfo("Éxito", f"Vehículo '{marca} {modelo}' registrado correctamente.")
            self.mostrar_vehiculos()
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error de Formato", "El campo Año debe ser un número entero.")
        except Error as e:
            messagebox.showerror("Error SQL", f"Error al insertar en la base de datos:\n{str(e)}")

    def mostrar_vehiculos(self):
        try:
            for item in self.tabla.get_children():
                self.tabla.delete(item)

            registros = self.db.obtener_vehiculos()

            for reg in registros:
                estado_texto = "Disponible" if reg[5] else "En Mantenimiento"
                self.tabla.insert("", "end", values=(reg[0], reg[1], reg[2], reg[3], reg[4], estado_texto))
        except Error as e:
            messagebox.showerror("Error SQL", f"Error al consultar MySQL:\n{str(e)}")

    def cargar_seleccion(self, event):
        item_seleccionado = self.tabla.selection()
        if item_seleccionado:
            valores = self.tabla.item(item_seleccionado[0], "values")
            self.id_var.set(valores[0])
            self.marca_var.set(valores[1])
            self.modelo_var.set(valores[2])
            self.anio_var.set(valores[3])
            self.combustible_var.set(valores[4])
            self.disponible_var.set(True if valores[5] == "Disponible" else False)

    def actualizar_vehiculo(self):
        vehiculo_id = self.id_var.get()
        if not vehiculo_id:
            messagebox.showwarning("Advertencia", "Seleccione un vehículo de la tabla para actualizar.")
            return

        marca = self.marca_var.get().strip()
        modelo = self.modelo_var.get().strip()
        anio = self.anio_var.get().strip()
        combustible = self.combustible_var.get()
        disponible = self.disponible_var.get()

        try:
            self.db.actualizar_vehiculo(vehiculo_id, marca, modelo, anio, combustible, disponible)
            messagebox.showinfo("Éxito", f"Vehículo ID {vehiculo_id} actualizado correctamente.")
            self.mostrar_vehiculos()
            self.limpiar_campos()
        except Error as e:
            messagebox.showerror("Error SQL", f"Error al actualizar el registro:\n{str(e)}")

    def borrar_vehiculo(self):
        vehiculo_id = self.id_var.get()
        if not vehiculo_id:
            messagebox.showwarning("Advertencia", "Seleccione un vehículo de la tabla para eliminar.")
            return

        confirmacion = messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de eliminar el vehículo con ID {vehiculo_id}?")
        if confirmacion:
            try:
                self.db.borrar_vehiculo(vehiculo_id)
                messagebox.showinfo("Éxito", "Vehículo eliminado de la base de datos.")
                self.mostrar_vehiculos()
                self.limpiar_campos()
            except Error as e:
                messagebox.showerror("Error SQL", f"Error al eliminar registro:\n{str(e)}")

    def generar_informe(self):
        try:
            disponibles, mantenimiento = self.db.obtener_metricas_informe()
            total = disponibles + mantenimiento
            tasa = (disponibles / total * 100) if total > 0 else 0

            mensaje_informe = (
                f"=== INFORME DE ESTADO DE LA FLOTA ===\n\n"
                f"• Total de Vehículos Registrados : {total}\n"
                f"• Vehículos Disponibles           : {disponibles}\n"
                f"• En Mantenimiento / Reservados  : {mantenimiento}\n\n"
                f"Tasa de Disponibilidad Activa: {tasa:.1f}%"
            )
            messagebox.showinfo("Informe de Flota", mensaje_informe)
        except Error as e:
            messagebox.showerror("Error SQL", f"Error al generar el informe:\n{str(e)}")

    def limpiar_campos(self):
        self.id_var.set("")
        self.marca_var.set("")
        self.modelo_var.set("")
        self.anio_var.set("")
        self.combustible_var.set("Gasolina")
        self.disponible_var.set(True)

    def al_cerrar(self):
        self.db.cerrar()
        self.root.destroy()