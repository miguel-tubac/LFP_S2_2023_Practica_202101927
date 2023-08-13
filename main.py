import tkinter as tk
from tkinter import filedialog
from CargaInventario import cargar_inventario

def mostrar_inventario(inventario):
    print("Inventario Inicial:")
    for producto, datos in inventario.items():
        print(f"Producto: {datos.nombre}")
        print(f"Cantidad: {datos.cantidad}")
        print(f"Precio unitario: {datos.precio_unitario}")
        print(f"Ubicación: {datos.ubicacion}")
        print()

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    
    archivo = filedialog.askopenfilename(initialdir='C:/Users/DELL/Downloads', title='Seleccionar archivo .inv', filetypes=[('Archivos de inventario', '*.inv')])
    return archivo

while True:
    print("""          ---------------------------------------------------------------
          Practica 1 - Lenguajes Formales y De Programacion
          ---------------------------------------------------------------
          # Sistema de Inventario:
          
          1. Cargar Inventario Inicial
          2. Cargar Instrucciones de Movimiento
          3. Crear Informe de inventario
          4. Salir

          Ingrese una Opcion: """, end=" ")
    try:
        opcionSeleccionada = int(input())
    except ValueError:
        print("Error: Ingrese un número válido.")
        continue
    
    if opcionSeleccionada == 1:
        print("Opcion 1")
        archivo_inventario = seleccionar_archivo()
        if archivo_inventario:
            inventario_inicial = cargar_inventario(archivo_inventario)
            mostrar_inventario(inventario_inicial)
    elif opcionSeleccionada == 2:
        print("Opcion 2")
    elif opcionSeleccionada == 3:
        print("Opcion 3")
    elif opcionSeleccionada == 4:
        print("Saliendo del programa.")
        break
    else:
        print("Opcion inválida.")
