import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

# Ventana
ventana = tk.Tk()
ventana.title("Registro de Doctores")
ventana.geometry("1050x650")
ventana.configure(bg="#50CDFF",)

# Crear Treeview en la parte inferior de la ventana emergente después de definir la ventana principal
def configurar_treeview():
    global treeview, scrollbar
    treeview = ttk.Treeview(ventana, columns=("Nombre", "Especialidad", "Años de Experiencia", "Género", "Hospital"), show="headings")
    treeview.heading("Nombre", text="Nombre")
    treeview.heading("Especialidad", text="Especialidad")
    treeview.heading("Años de Experiencia", text="Años de Experiencia")
    treeview.heading("Género", text="Género")
    treeview.heading("Hospital", text="Hospital")
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
    for doctor in doctorDataD:
        treeview.insert("", "end", values=(
            doctor["Nombre"],
            doctor["Especialidad"],
            doctor["Años de Experiencia"],
            doctor["Género"],
            doctor["Hospital"]
        ))

# Función para guardar los datos en un archivo de texto
def guardar_datos_en_archivo():
    with open("codeRegistroDoctor.txt", "w", encoding="utf-8") as archivo:
        for doctor in doctorDataD:
            archivo.write(
                f"{doctor['Nombre']}|{doctor['Especialidad']}|{doctor['Años de Experiencia']}|{doctor['Género']}|{doctor['Hospital']}\n"
            )

# Función para cargar los datos desde un archivo de texto
def cargar_datos_desde_archivo():
    try:
        with open("codeRegistroDoctor.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 5:  # Validar que haya 5 campos
                    doctor = {
                        "Nombre": datos[0],
                        "Especialidad": datos[1],
                        "Años de Experiencia": datos[2],
                        "Género": datos[3],
                        "Hospital": datos[4]
                    }
                    doctorDataD.append(doctor)
    except FileNotFoundError:
        # Si el archivo no existe, se crea uno vacío
        open("codeRegistroDoctor.txt", "w", encoding="utf-8").close()

def registrarDoctor():
    nombre = entry_nombre.get()
    especialidad = especialidad_var.get()
    experiencia = spin_experiencia.get()
    genero = genero_var.get()
    hospital = hospital_var.get()

    # Crear un diccionario con los datos registrados
    doctor = {
        "Nombre": nombre,
        "Especialidad": especialidad,
        "Años de Experiencia": experiencia,
        "Género": genero,
        "Hospital": hospital
    }

    # Agregar el doctor a la lista de datos
    doctorDataD.append(doctor)

    # Guardar los datos en el archivo
    guardar_datos_en_archivo()

    # Actualizar el Treeview
    cargar_datos_treeview()

# Lista para almacenar los datos de doctores
doctorDataD = []

# Nombre completo
tk.Label(ventana, text="Nombre completo:",bg="#50CDFF").grid(row=0, column=0, sticky="w", pady=5, padx=10)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, columnspan=3, sticky="w", padx=10, pady=5)

# Especialidad 
especialidades = ["Cardiología", "Neurología", "Pediatría", "Traumatología"]
tk.Label(ventana, text="Especialidad:", bg="#50CDFF").grid(row=1, column=0, sticky="w", pady=8, padx=10)
especialidad_var = tk.StringVar(value="Pediatría")
combobox_especialidad = ttk.Combobox(ventana, textvariable=especialidad_var, values=especialidades, state="readonly")
combobox_especialidad.grid(row=1, column=1, columnspan=2, sticky="w", padx=10, pady=8)

# Hospital
tk.Label(ventana, text="Hospital:", bg="#50CDFF").grid(row=2, column=0, sticky="w", pady=8, padx=10)
hospital_var = tk.StringVar(value="Hospital Central")
hospitales = ["Hospital Central", "Hospital Norte", "Clínica Santa María", "Clínica Vida"]
combobox_hospital = ttk.Combobox(ventana, textvariable=hospital_var, values=hospitales, state="readonly")
combobox_hospital.grid(row=2, column=1, columnspan=2, sticky="w", padx=10, pady=8)

# Años de Experiencia
tk.Label(ventana, text="Años de Experiencia:", bg="#50CDFF").grid(row=3, column=0, sticky="w", pady=8, padx=10)
spin_experiencia = tk.Spinbox(ventana, from_=0, to=50, width=5)
spin_experiencia.grid(row=3, column=1, sticky="w", padx=10, pady=8)

# Género
tk.Label(ventana, text="Género:", bg="#50CDFF").grid(row=4, column=0, sticky="w", pady=8, padx=10)
genero_var = tk.StringVar(value="Masculino")
tk.Radiobutton(ventana, text="Masculino", bg="#50CDFF", variable=genero_var, value="Masculino").grid(row=4, column=1, sticky="w", padx=10, pady=4)
tk.Radiobutton(ventana, text="Femenino", bg="#50CDFF", variable=genero_var, value="Femenino").grid(row=5, column=1, sticky="w", padx=10, pady=4)

# Botón de registro
frame_botones = tk.Frame(ventana, bg="#50CDFF")
frame_botones.grid(row=6, column=0, columnspan=4, pady=20)
btn_registrar = tk.Button(frame_botones, text="Registrar", command=registrarDoctor, width=15)
btn_registrar.pack(pady=10)  # Centrar el botón dentro del marco

# Cargar los datos desde el archivo al iniciar el programa
cargar_datos_desde_archivo()

# Cargar datos iniciales en el Treeview
cargar_datos_treeview()

ventana.mainloop()
