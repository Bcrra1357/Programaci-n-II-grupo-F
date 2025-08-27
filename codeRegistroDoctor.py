import tkinter as tk
from tkinter import messagebox

def registrarDoctor():
    nombre = entry_nombre.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    especialidad = especialidad_var.get()
    if especialidad == "Otro":
        especialidad = entry_otro.get()
    disponibilidad = []
    if var_manana.get():
        disponibilidad.append("Mañana")
    if var_tarde.get():
        disponibilidad.append("Tarde")
    if var_noche.get():
        disponibilidad.append("Noche")
    datos = (
        f"Nombre completo: {nombre}\n"
        f"Dirección: {direccion}\n"
        f"Teléfono: {telefono}\n"
        f"Especialidad: {especialidad}\n"
        f"Disponibilidad: {', '.join(disponibilidad)}"
    )
    messagebox.showinfo("Datos Registrados", datos)

#Ventana
ventana = tk.Tk()
ventana.title("Registro de Doctores")
ventana.geometry("550x500")
ventana.configure(bg="#50CDFF",)
# Nombre completo
tk.Label(ventana, text="Nombre completo:",bg="#50CDFF").grid(row=0, column=0, sticky="w", pady=5, padx=10)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, columnspan=3, sticky="w", padx=10, pady=5)

# Dirección
tk.Label(ventana, text="Dirección:",bg="#50CDFF").grid(row=1, column=0, sticky="w", pady=5, padx=10)
entry_direccion = tk.Entry(ventana)
entry_direccion.grid(row=1, column=1, columnspan=3, sticky="w", padx=10, pady=8)

# Teléfono 
def solo_numeros(char):
    return char.isdigit() or char == ""
vcmd = ventana.register(solo_numeros)
tk.Label(ventana, text="Teléfono:",bg="#50CDFF").grid(row=2, column=0, sticky="w", pady=8, padx=10)
entry_telefono = tk.Entry(ventana, validate="key", validatecommand=(vcmd, '%P'))
entry_telefono.grid(row=2, column=1, columnspan=3, sticky="w", padx=10, pady=8)

# Especialidad 
tk.Label(ventana, text="Especialidad:",bg="#50CDFF").grid(row=3, column=0, sticky="w", pady=8, padx=10)
especialidad_var = tk.StringVar(value="Pediatría")
tk.Radiobutton(ventana, text="Pediatría",bg="#50CDFF", variable=especialidad_var, value="Pediatría").grid(row=4, column=1, sticky="w", padx=10, pady=4)
tk.Radiobutton(ventana, text="Cardiología",bg="#50CDFF", variable=especialidad_var, value="Cardiología").grid(row=5, column=1, sticky="w", padx=10, pady=4)
tk.Radiobutton(ventana, text="Neurología",bg="#50CDFF", variable=especialidad_var, value="Neurología").grid(row=6, column=1, sticky="w", padx=10, pady=4)
# Opción Otro
tk.Radiobutton(ventana, text="Otro:",bg="#50CDFF", variable=especialidad_var, value="Otro").grid(row=7, column=1, sticky="w", padx=10, pady=4)
entry_otro = tk.Entry(ventana, state="disabled")
entry_otro.grid(row=7, column=2, sticky="w", padx=10, pady=4)
def actualizar_otro(*args):
    if especialidad_var.get() == "Otro":
        entry_otro.config(state="normal")
    else:
        entry_otro.delete(0, tk.END)
        entry_otro.config(state="disabled")
especialidad_var.trace_add("write", actualizar_otro)

# Disponibilidad 
tk.Label(ventana, text="Disponibilidad:",bg="#50CDFF").grid(row=8, column=0, sticky="w", pady=8, padx=10)
var_manana = tk.BooleanVar()
var_tarde = tk.BooleanVar()
var_noche = tk.BooleanVar()
tk.Checkbutton(ventana, text="Mañana",bg="#50CDFF", variable=var_manana).grid(row=9, column=1, sticky="w", padx=10, pady=5)
tk.Checkbutton(ventana, text="Tarde",bg="#50CDFF", variable=var_tarde).grid(row=10, column=1, sticky="w", padx=10, pady=5)
tk.Checkbutton(ventana, text="Noche",bg="#50CDFF", variable=var_noche).grid(row=11, column=1, sticky="w", padx=10, pady=5)

# Botón de registro y salir
frame_botones = tk.Frame(ventana, bg="#50CDFF")
frame_botones.grid(row=12, column=0, columnspan=4, pady=20)
tk.Button(frame_botones, text="Registrar", command=registrarDoctor, width=15).pack(side="left", padx=10)
tk.Button(frame_botones, text="Salir", command=ventana.destroy, width=15).pack(side="left", padx=10)

ventana.mainloop()
