import tkinter as tk
from tkinter import messagebox
# Pacientes
def nuevoPaciente():
    ventanaRegistro = tk.Toplevel(ventanaPrincipal)
    ventanaRegistro.title("Registro de Pacientes")
    ventanaRegistro.geometry("600x450")
    ventanaRegistro.configure(bg="#8D8C8C")
    #Nombre
    nombreLabel = tk.Label(ventanaRegistro, text="Nombre: ",bg="#8D8C8C")
    nombreLabel.grid(row=0, column=0, padx=10, pady=5,sticky="w") # n=norte, s=sur, e=este, w=oeste
    entradaNombre = tk.Entry(ventanaRegistro)
    entradaNombre.grid(row=0, column=1, padx=10, pady=5, sticky="we")
    #Dirección
    direccionLabel = tk.Label(ventanaRegistro, text="Dirección: ",bg="#8D8C8C")
    direccionLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entradaDireccion = tk.Entry(ventanaRegistro)
    entradaDireccion.grid(row=1, column=1, padx=10, pady=5, sticky="we")
    #Teléfono
    telefonoLabel = tk.Label(ventanaRegistro, text="Teléfono: ",bg="#8D8C8C")
    telefonoLabel.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entradaTelefono = tk.Entry(ventanaRegistro)
    entradaTelefono.grid(row=2, column=1, padx=10, pady=5, sticky="we")
    #sexo
    sexoLabel = tk.Label(ventanaRegistro, text="Sexo: ",bg="#8D8C8C")
    sexoLabel.grid(row=3, column=0, padx=10, pady=5,sticky="w")
    Sexo = tk.StringVar(value="Masculino")# Es una variable especial de Tkinter que se utiliza para enlazar widgets como RadioButtons
    rbMasculino = tk.Radiobutton(ventanaRegistro, text="Masculino", variable=Sexo, value="Masculino")
    rbMasculino.grid(row=3, column=1, padx=10, pady=5, sticky="w")
    rbFemenino = tk.Radiobutton(ventanaRegistro, text="Femenino", variable=Sexo, value="Femenino")
    rbFemenino.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    #Enfermedades
    enfLabel = tk.Label(ventanaRegistro, text="Enfermedades base: ",bg="#8D8C8C")
    enfLabel.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    diabetes = tk.BooleanVar()
    hipertension = tk.BooleanVar()
    asma = tk.BooleanVar()
    cbDiabetes = tk.Checkbutton(ventanaRegistro, text="Diabetes", variable=diabetes, bg="#8D8C8C")      
    cbDiabetes.grid(row=5, column=1, padx=10, pady=5, sticky="w")
    cbHipertension = tk.Checkbutton(ventanaRegistro, text="Hipertensión", variable=hipertension, bg="#8D8C8C")
    cbHipertension.grid(row=6, column=1, padx=10, pady=5, sticky="w") 
    cbAsma = tk.Checkbutton(ventanaRegistro, text="Asma", variable=asma, bg="#8D8C8C")
    cbAsma.grid(row=7, column=1, padx=10, pady=5, sticky="w")
    # Cadena para mostrar todos los datos del formulario
    def registrarDatos():
        enfermedades = []
        if diabetes.get():
            enfermedades.append("Diabetes")
        if hipertension.get():
            enfermedades.append("Hipertensión")
        if asma.get():
            enfermedades.append("Asma")
        if len(enfermedades) > 0:
            enfermedadesTexto = ", ".join(enfermedades)
        else:
            enfermedadesTexto = "Ninguna"
        info = (
            f"Nombre: {entradaNombre.get()}\n"
            f"Dirección: {entradaDireccion.get()}\n"
            f"Teléfono: {entradaTelefono.get()}\n"
            f"Sexo: {Sexo.get()}\n"
            f"Enfermedades: {enfermedadesTexto}\n"
        )
        messagebox.showinfo("Datos Registrados", info,)
        ventanaRegistro.destroy() #Cierra la ventana tras el mensaje
    btnRegistrar = tk.Button(ventanaRegistro, text="Registrar", command=registrarDatos)
    btnRegistrar.grid(row=9, columnspan=2, pady=15,)
def BuscarPaciente():
    messagebox.showinfo("BuscarPaciente","Busqueda de Paciente")
def EliminarPaciente():
    messagebox.showinfo("EliminarPaciente","Eliminación de Paciente")
# Doctores
def nuevoDoctor():
    messagebox.showinfo("nuevoDoctor","Registrar Doctor")
def BuscarDoctor():
    messagebox.showinfo("BuscarDoctor","Busqueda de Doctor")
def EliminarDoctor():
    messagebox.showinfo("EliminarDoctor","Eliminación de Doctor")
    
#Ventana
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Sistema de Registro de Pacientes")
ventanaPrincipal.geometry("600x450")
ventanaPrincipal.configure(bg="#BBBBBB")

#Barra de menu
barraMenu = tk.Menu(ventanaPrincipal)
ventanaPrincipal.configure(menu=barraMenu)

#Barra de pacientes
menuPacientes = tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Pacientes",menu=menuPacientes)
menuPacientes.add_command(label="Nuevo Paciente",command=nuevoPaciente)
menuPacientes.add_command(label="Buscar Paciente",command=BuscarPaciente)
menuPacientes.add_command(label="Eliminar Paciente",command=EliminarPaciente)
menuPacientes.add_separator()
menuPacientes.add_command(label="Salir",command=ventanaPrincipal.quit)

#Barra de doctores
menuDoctores = tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Doctores",menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor",command=nuevoDoctor)
menuDoctores.add_command(label="Buscar Doctor",command=BuscarDoctor)
menuDoctores.add_command(label="Eliminar Doctor",command=EliminarDoctor)
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir",command=ventanaPrincipal.quit)
#Barra de Ayuda
menuAyuda = tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Ayuda",menu=menuAyuda)
menuAyuda.add_command(label="Acerca de...",command=lambda:messagebox.showinfo("Acerca de...","V: Prueba 1.0\nby: Bcrra_"))
menuAyuda.add_separator()
menuAyuda.add_command(label="Salir",command=ventanaPrincipal.quit)
ventanaPrincipal.mainloop()