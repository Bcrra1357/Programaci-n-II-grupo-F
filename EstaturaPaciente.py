# Importaciones necesarias
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from datetime import datetime

# Ventana
ventana = tk.Tk()
ventana.title("Registro de Pacientes")
ventana.geometry("1050x650")
ventana.configure(bg="#50CDFF",)

# Crear Treeview en la parte inferior de la ventana emergente después de definir la ventana principal
def configurar_treeview():
    global treeview, scrollbar
    treeview = ttk.Treeview(ventana, columns=("Nombre", "Fecha de Nacimiento", "Edad", "Género", "Grupo Sanguíneo", "Tipo de Seguro", "Centro Médico", "Estatura"), show="headings", height=8)  # Ajustar la altura del Treeview
    treeview.heading("Nombre", text="Nombre")
    treeview.heading("Fecha de Nacimiento", text="Fecha de Nacimiento")
    treeview.heading("Edad", text="Edad")
    treeview.heading("Género", text="Género")
    treeview.heading("Grupo Sanguíneo", text="Grupo Sanguíneo")
    treeview.heading("Tipo de Seguro", text="Tipo de Seguro")
    treeview.heading("Centro Médico", text="Centro Médico")
    treeview.heading("Estatura", text="Estatura (m)")

    # Ajustar el ancho de las columnas
    treeview.column("Nombre", width=150, anchor="center")
    treeview.column("Fecha de Nacimiento", width=120, anchor="center")
    treeview.column("Edad", width=50, anchor="center")
    treeview.column("Género", width=100, anchor="center")
    treeview.column("Grupo Sanguíneo", width=120, anchor="center")
    treeview.column("Tipo de Seguro", width=120, anchor="center")
    treeview.column("Centro Médico", width=150, anchor="center")
    treeview.column("Estatura", width=100, anchor="center")

    treeview.grid(row=13, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    # Agregar barra de desplazamiento vertical
    scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=treeview.yview)
    treeview.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=13, column=4, sticky="ns")

# Llamar a la configuración del Treeview después de definir la ventana
configurar_treeview()

# Función para cargar datos en el Treeview
def cargar_datos_treeview():
    # Limpiar el Treeview
    for item in treeview.get_children():
        treeview.delete(item)
    # Insertar datos registrados
    for paciente in pacienteDataP:
        treeview.insert("", "end", values=(
            paciente["Nombre"],
            paciente["Fecha de Nacimiento"],
            paciente["Edad"],
            paciente["Género"],
            paciente["Grupo Sanguíneo"],
            paciente["Tipo de Seguro"],
            paciente["Centro Médico"],
            paciente["Estatura"]
        ))

# Función para guardar los datos en un archivo de texto
def guardar_datos_en_archivo():
    with open("EstaturaPaciente.txt", "w", encoding="utf-8") as archivo:
        for paciente in pacienteDataP:
            archivo.write(
                f"{paciente['Nombre']}|{paciente['Fecha de Nacimiento']}|{paciente['Edad']}|{paciente['Género']}|{paciente['Grupo Sanguíneo']}|{paciente['Tipo de Seguro']}|{paciente['Centro Médico']}|{paciente['Estatura']}\n"
            )

# Función para cargar los datos desde un archivo de texto
def cargar_datos_desde_archivo():
    try:
        with open("EstaturaPaciente.txt", "r", encoding="utf-8") as archivo:
            pacienteDataP.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 8:  # Validar que haya 8 campos
                    paciente = {
                        "Nombre": datos[0],
                        "Fecha de Nacimiento": datos[1],
                        "Edad": datos[2],
                        "Género": datos[3],
                        "Grupo Sanguíneo": datos[4],
                        "Tipo de Seguro": datos[5],
                        "Centro Médico": datos[6],
                        "Estatura": datos[7]
                    }
                    pacienteDataP.append(paciente)
    except FileNotFoundError:
        open("EstaturaPaciente.txt", "w", encoding="utf-8").close()

def enmascarar_fecha(event):
    texto = entry_fecha_nacimiento.get()
    limpio = "".join(filter(str.isdigit, texto))
    formato_final = ""

    if len(limpio) > 8:
        limpio = limpio[:8]
    if len(limpio) > 4:
        formato_final = f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio) > 2:
        formato_final = f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final = limpio

    entry_fecha_nacimiento.delete(0, tk.END)
    entry_fecha_nacimiento.insert(0, formato_final)

    if len(formato_final) == 10:
        try:
            fecha_nac = datetime.strptime(formato_final, "%d-%m-%Y").date()
            fecha_actual = datetime.now().date()
            edad = fecha_actual.year - fecha_nac.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nac.month, fecha_nac.day))
            edad_var.set(edad)
        except ValueError:
            edad_var.set("")
    else:
        edad_var.set("")

def registrarPaciente():
    nombre = entry_nombre.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    edad = edad_var.get()
    genero = genero_var.get()
    grupo_sanguineo = entry_grupo_sanguineo.get()
    tipo_seguro = tipo_seguro_var.get()
    centro_medico = centro_medico_var.get()
    estatura = entry_estatura.get()

    # Crear un diccionario con los datos registrados
    paciente = {
        "Nombre": nombre,
        "Fecha de Nacimiento": fecha_nacimiento,
        "Edad": edad,
        "Género": genero,
        "Grupo Sanguíneo": grupo_sanguineo,
        "Tipo de Seguro": tipo_seguro,
        "Centro Médico": centro_medico,
        "Estatura": estatura
    }

    # Agregar el paciente a la lista de datos
    pacienteDataP.append(paciente)

    # Guardar los datos en el archivo
    guardar_datos_en_archivo()

    # Actualizar el Treeview
    cargar_datos_treeview()

def eliminarPaciente():
    seleccionado = treeview.selection()
    if not seleccionado:
        messagebox.showinfo("Eliminar Paciente", "No se ha seleccionado ningún paciente.")
        return

    id_item = seleccionado[0]
    valores = treeview.item(id_item, 'values')
    nombre_paciente = valores[0]  # Obtener el nombre del paciente seleccionado

    if messagebox.askyesno("Eliminar Paciente", f"¿Estás seguro de que deseas eliminar este paciente '{nombre_paciente}'?"):
        # Buscar el índice del paciente en la lista basado en el nombre
        for i, paciente in enumerate(pacienteDataP):
            if paciente["Nombre"] == nombre_paciente:
                del pacienteDataP[i]
                break

        guardar_datos_en_archivo()  # Guardar los cambios en el archivo
        cargar_datos_treeview()
        messagebox.showinfo("Paciente Eliminado", "El paciente ha sido eliminado exitosamente.")

# Lista para almacenar los datos de pacientes
pacienteDataP = []

# Nombre completo
tk.Label(ventana, text="Nombre completo:",bg="#50CDFF").grid(row=0, column=0, sticky="w", pady=5, padx=10)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, columnspan=3, sticky="w", padx=10, pady=5)

# Fecha de Nacimiento
tk.Label(ventana, text="Fecha de Nacimiento:", bg="#50CDFF").grid(row=1, column=0, sticky="w", pady=8, padx=10)
entry_fecha_nacimiento = tk.Entry(ventana)
entry_fecha_nacimiento.grid(row=1, column=1, columnspan=2, sticky="w", padx=10, pady=8)
entry_fecha_nacimiento.bind('<KeyRelease>', enmascarar_fecha)

# Grupo Sanguíneo
tk.Label(ventana, text="Grupo Sanguíneo:", bg="#50CDFF").grid(row=2, column=0, sticky="w", pady=8, padx=10)
entry_grupo_sanguineo = tk.Entry(ventana)
entry_grupo_sanguineo.grid(row=2, column=1, columnspan=2, sticky="w", padx=10, pady=8)

# Tipo de Seguro
tk.Label(ventana, text="Tipo de Seguro:", bg="#50CDFF").grid(row=3, column=0, sticky="w", pady=8, padx=10)
tipo_seguro_var = tk.StringVar(value="Público")
combobox_tipo_seguro = ttk.Combobox(ventana, textvariable=tipo_seguro_var, values=["Público", "Privado", "Ninguno"], state="readonly")
combobox_tipo_seguro.grid(row=3, column=1, columnspan=2, sticky="w", padx=10, pady=8)

# Centro Médico
tk.Label(ventana, text="Centro Médico:", bg="#50CDFF").grid(row=4, column=0, sticky="w", pady=8, padx=10)
centro_medico_var = tk.StringVar(value="Hospital Central")
combobox_centro_medico = ttk.Combobox(ventana, textvariable=centro_medico_var, values=["Hospital Central", "Clínica Norte", "Centro Salud Sur"], state="readonly")
combobox_centro_medico.grid(row=4, column=1, columnspan=2, sticky="w", padx=10, pady=8)

# Género
tk.Label(ventana, text="Género:", bg="#50CDFF").grid(row=5, column=0, sticky="w", pady=8, padx=10)
genero_var = tk.StringVar(value="Masculino")
tk.Radiobutton(ventana, text="Masculino", bg="#50CDFF", variable=genero_var, value="Masculino").grid(row=5, column=1, sticky="w", padx=10, pady=4)
tk.Radiobutton(ventana, text="Femenino", bg="#50CDFF", variable=genero_var, value="Femenino").grid(row=6, column=1, sticky="w", padx=10, pady=4)

# Edad (readonly)
tk.Label(ventana, text="Edad:", bg="#50CDFF").grid(row=7, column=0, sticky="w", pady=8, padx=10)
edad_var = tk.StringVar()
entry_edad = tk.Entry(ventana, textvariable=edad_var, state="readonly")
entry_edad.grid(row=7, column=1, columnspan=2, sticky="w", padx=10, pady=8)

# Estatura
tk.Label(ventana, text="Estatura (m):", bg="#50CDFF").grid(row=8, column=0, sticky="w", pady=8, padx=10)
entry_estatura = tk.Entry(ventana)
entry_estatura.grid(row=8, column=1, columnspan=2, sticky="w", padx=10, pady=8)

# Botón de registro
frame_botones = tk.Frame(ventana, bg="#50CDFF")
frame_botones.grid(row=9, column=0, columnspan=3, pady=20, sticky="n")  # Centrar el marco de botones

# Botón Registrar
btn_registrar = tk.Button(frame_botones, text="Registrar", command=registrarPaciente, width=15)
btn_registrar.pack(side="left", padx=10, pady=10)

# Botón Eliminar
btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminarPaciente, width=15)
btn_eliminar.pack(side="left", padx=10, pady=10)

# Cargar los datos desde el archivo al iniciar el programa
cargar_datos_desde_archivo()

# Cargar datos iniciales en el Treeview
cargar_datos_treeview()

ventana.mainloop()