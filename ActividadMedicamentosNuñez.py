# Proyeto Formulario de medicamentos

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Constantes
rutaArchivo = "medicamento.txt"

# Funciones de persistencia
def guardarRegistrosEnArchivo():
    """
    Guarda todos los registros del Treeview en el archivo de texto.
    Cada registro se guarda en formato camelCase separado por '|'.
    """
    with open(rutaArchivo, "w") as archivo:
        for item_id in treeview.get_children():
            valores = treeview.item(item_id, "values")
            # Formato: nombre|presentacion|dosis|fechaVencimiento
            linea = f"{valores[0]}|{valores[1]}|{valores[2]}|{valores[3]}\n"
            archivo.write(linea)

def cargarRegistrosDesdeArchivo():
    """
    Carga los registros desde el archivo de texto al Treeview
    al iniciar la aplicación.
    """
    try:
        with open(rutaArchivo, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    # Desempaquetamos los valores y los insertamos en el Treeview
                    nombre, presentacion, dosis, fechaVencimiento = linea.split("|")
                    treeview.insert("", tk.END, values=(nombre, presentacion, dosis, fechaVencimiento))
    except FileNotFoundError:
        # Si el archivo no existe, lo creamos vacío para evitar errores futuros.
        open(rutaArchivo, "w").close()


# Funciones de la interfaz
def registrarMedicamento():
    """
    Recoge los datos del formulario, los valida, los inserta en el Treeview
    y los guarda en el archivo de texto.
    """
    nombre = entryNombre.get()
    presentacion = comboPresentacion.get()
    dosis = entryDosis.get()
    fechaVencimiento = entryFechaVar.get()

    # Validación de campos
    if not all([nombre, presentacion, dosis, fechaVencimiento]):
        messagebox.showwarning("Campos incompletos", "Por favor, rellene todos los campos.")
        return

    # Insertar en el Treeview
    treeview.insert("", tk.END, values=(nombre, presentacion, dosis, fechaVencimiento))

    # Guardar todos los registros en el archivo
    guardarRegistrosEnArchivo()

    # Limpiar campos del formulario
    limpiarCampos()

def eliminarMedicamento():
    """
    Elimina el registro seleccionado del Treeview y actualiza el archivo de texto.
    """
    selectedItem = treeview.selection()
    if not selectedItem:
        messagebox.showwarning("Sin selección", "Por favor, seleccione un medicamento para eliminar.")
        return

    # Confirmación de eliminación
    confirmar = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de que desea eliminar el medicamento seleccionado?")
    if not confirmar:
        return

    # Eliminar del Treeview
    treeview.delete(selectedItem)

    # Actualizar el archivo de texto
    guardarRegistrosEnArchivo()
    messagebox.showinfo("Eliminado", "El medicamento ha sido eliminado correctamente.")

def limpiarCampos():
    """Limpia los campos de entrada del formulario."""
    entryNombre.delete(0, tk.END)
    comboPresentacion.set('')
    entryDosis.delete(0, tk.END)
    entryFechaVar.set('')

def formatoFechaKeyrelease(event):
    """
    Aplica un formato DD-MM-YYYY al campo de fecha mientras el usuario escribe.
    """
    s = entryFechaVar.get()
    # Conservar solo dígitos y limitar a 8 (DDMMYYYY)
    digits = ''.join(ch for ch in s if ch.isdigit())[:8]

    if len(digits) > 4:
        formatted = f"{digits[:2]}-{digits[2:4]}-{digits[4:]}"
    elif len(digits) > 2:
        formatted = f"{digits[:2]}-{digits[2:]}"
    else:
        formatted = digits

    if formatted != s:
        entryFechaVar.set(formatted)

    entryFecha.icursor(tk.END)

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Gestión de Medicamentos")
ventana.geometry("800x520")
ventana.minsize(700, 450)
ventana.configure(bg="#3ADBFB")

# Frame del formulario
formFrame = tk.Frame(ventana, bg="#3ADBFB")
formFrame.grid(row=0, column=0, sticky="ew", padx=12, pady=10)
formFrame.columnconfigure(0, weight=0)
formFrame.columnconfigure(1, weight=1)

# Nombre
lblNombre = tk.Label(formFrame, text="Nombre:", bg="#3ADBFB")
lblNombre.grid(row=0, column=0, sticky="w", padx=5, pady=5)
entryNombre = tk.Entry(formFrame)
entryNombre.grid(row=0, column=1, sticky="w", padx=5, pady=5)
5
# Presentación
lblPresentacion = tk.Label(formFrame, text="Presentación:", bg="#3ADBFB")
lblPresentacion.grid(row=1, column=0, sticky="w", padx=5, pady=5)
comboPresentacion = ttk.Combobox(formFrame, values=["Tabletas", "Jarabe", "Inyectable", "Cápsulas", "Otro"])
comboPresentacion.grid(row=1, column=1, sticky="w", padx=5, pady=5)

# Dosis
lblDosis = tk.Label(formFrame, text="Dosis:", bg="#3ADBFB")
lblDosis.grid(row=2, column=0, sticky="w", padx=5, pady=5)
entryDosis = tk.Entry(formFrame)
entryDosis.grid(row=2, column=1, sticky="w", padx=5, pady=5)

# Fecha Vencimiento con enmascarado
lblFecha = tk.Label(formFrame, text="Fecha Vencimiento (dd-mm-yyyy):", bg="#3ADBFB")
lblFecha.grid(row=3, column=0, sticky="w", padx=5, pady=5)
entryFechaVar = tk.StringVar()
entryFecha = tk.Entry(formFrame, textvariable=entryFechaVar)
entryFecha.grid(row=3, column=1, sticky="w", padx=5, pady=5)
entryFecha.bind("<KeyRelease>", formatoFechaKeyrelease)

# Botones
btnFrame = tk.Frame(formFrame, bg="#3ADBFB")
btnFrame.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=(10, 2))
btnFrame.columnconfigure((0, 1), weight=1)

btnRegistrar = tk.Button(btnFrame, text="Registrar", command=registrarMedicamento, bg="#45D042", fg="white")
btnRegistrar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

btnEliminar = tk.Button(btnFrame, text="Eliminar", command=eliminarMedicamento, bg="#E83333", fg="White")
btnEliminar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Frame lista
listFrame = tk.Frame(ventana, bg="#3ADBFB")
listFrame.grid(row=1, column=0, sticky="nsew", padx=12, pady=6)
ventana.rowconfigure(1, weight=1)
ventana.columnconfigure(0, weight=1)
listFrame.rowconfigure(0, weight=1)
listFrame.columnconfigure(0, weight=1)

treeview = ttk.Treeview(listFrame,
                        columns=("nombre", "presentacion", "dosis", "fechaVencimiento"),
                        show="headings")
treeview.grid(row=0, column=0, sticky="nsew")
treeview.heading("nombre", text="Nombre")
treeview.heading("presentacion", text="Presentación")
treeview.heading("dosis", text="Dosis")
treeview.heading("fechaVencimiento", text="Fecha Vencimiento")
treeview.column("nombre", width=220)
treeview.column("presentacion", width=120, anchor="center")
treeview.column("dosis", width=100, anchor="center")
treeview.column("fechaVencimiento", width=120, anchor="center")

scrollY = ttk.Scrollbar(listFrame, orient="vertical", command=treeview.yview)
scrollY.grid(row=0, column=1, sticky="ns")
treeview.configure(yscrollcommand=scrollY.set)


# Carga inicial de datos
cargarRegistrosDesdeArchivo()

# Ejecutar
ventana.mainloop()
