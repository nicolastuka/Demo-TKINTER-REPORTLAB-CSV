# importo tKInter completo... luego puedo ir recortando
import tkinter as tk


def SaludarUsuario(nombre):
    label["text"] = f"Hola {inputText.get()}"


# Creación de la ventana
window = tk.Tk()
# Configuración de las dimensiones de la pantalla
window.geometry("500x500")

# Creación de la etiqueta, requiere indicar donde agregarla, el texto y otras opciones.
label = tk.Label(window, text="Hola Campeón", bg="blue")
# El método pack coloca la etiqueta en la pantalla y se le pueden agregar opciones
label.pack(side=tk.BOTTOM, fill=tk.X)

# Creación de un botón, es importante indicar el comando que le da funcionalidad
button = tk.Button(window, text="Salir", command=exit, padx=50, pady=50)
button.pack()

# Creación de una caja de introducción de texto
inputText = tk.Entry(window)
inputText.pack()

# Creción de un botón con función con parámtros (se usa lambda)
buttonParam = tk.Button(
    window, text="Botón con parámetro", command=lambda: SaludarUsuario("Nicolás")
)
buttonParam.pack()

# Bucle que mantiene abierta la ventana hasta que se finaliza el programa
window.mainloop()
