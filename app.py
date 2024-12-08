import tkinter as tk
import random

# Función para verificar el número
def verificar_numero():
    global numero_aleatorio, intentos
    try:
        intento = int(entrada.get())
        if intento < 1 or intento > 100:
            etiqueta_resultado.config(text="Por favor, ingresa un número entre 1 y 100.")
            return
        
        intentos -= 1
        etiqueta_intentos.config(text=f"Intentos restantes: {intentos}")
        
        if intento == numero_aleatorio:
            etiqueta_resultado.config(text="¡Correcto! Has adivinado el número.", fg="green")
            deshabilitar_campos()
        elif intento < numero_aleatorio:
            etiqueta_resultado.config(text="Demasiado bajo. Intenta con un número más alto.", fg="red")
        else:
            etiqueta_resultado.config(text="Demasiado alto. Intenta con un número más bajo.", fg="red")
        
        if intentos <= 0 and intento != numero_aleatorio:
            etiqueta_resultado.config(text=f"Has perdido. El número era {numero_aleatorio}.", fg="red")
            deshabilitar_campos()
    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingresa un número válido.")

# Función para deshabilitar los campos
def deshabilitar_campos():
    entrada.config(state="disabled")
    boton_adivinar.config(state="disabled")

# Función para reiniciar el juego
def reiniciar_juego():
    global numero_aleatorio, intentos
    numero_aleatorio = random.randint(1, 100)
    intentos = 10
    etiqueta_resultado.config(text="", fg="black")
    etiqueta_intentos.config(text=f"Intentos restantes: {intentos}")
    entrada.config(state="normal")
    entrada.delete(0, tk.END)
    boton_adivinar.config(state="normal")

# Inicializar ventana principal
root = tk.Tk()
root.title("Adivina el Número")

# Variables globales
numero_aleatorio = random.randint(1, 100)
intentos = 10

# Interfaz de usuario
etiqueta_titulo = tk.Label(root, text="¡Adivina el número entre 1 y 100!", font=("Arial", 14))
etiqueta_titulo.pack(pady=10)

entrada = tk.Entry(root, font=("Arial", 12))
entrada.pack(pady=5)

boton_adivinar = tk.Button(root, text="Adivinar", command=verificar_numero, font=("Arial", 12))
boton_adivinar.pack(pady=5)

etiqueta_resultado = tk.Label(root, text="", font=("Arial", 12))
etiqueta_resultado.pack(pady=10)

etiqueta_intentos = tk.Label(root, text=f"Intentos restantes: {intentos}", font=("Arial", 12))
etiqueta_intentos.pack(pady=5)

boton_reiniciar = tk.Button(root, text="Reiniciar", command=reiniciar_juego, font=("Arial", 12))
boton_reiniciar.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()

