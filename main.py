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

#carga del inventario
def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    
    archivo = filedialog.askopenfilename(initialdir='C:/Users/DELL/Downloads', title='Seleccionar archivo .inv', filetypes=[('Archivos de inventario', '*.inv')])
    return archivo
#Modificacion del inventario .mov
def seleccionar_archivo_movimiento():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    
    archivo = filedialog.askopenfilename(initialdir='C:/Users/DELL/Downloads', title='Seleccionar archivo .mov', filetypes=[('Archivos de inventario', '*.mov')])
    return archivo
inventario_inicial = None
while True:
    print("\n---------------------------------------------------------------")
    print("      Practica 1 - Lenguajes Formales y De Programacion")
    print("---------------------------------------------------------------")
    print("Sistema de Inventario:\n")  
    print("1. Cargar Inventario Inicial")
    print("2. Cargar Instrucciones de Movimiento")
    print("3. Crear Informe de inventario")
    print("4. Salir\n")
    print("Ingrese una Opcion: """, end=" ")
    try:
        opcionSeleccionada = int(input())
    except ValueError:
        print("Error: Ingrese un número válido.")
        continue
    
    if opcionSeleccionada == 1:
        if inventario_inicial is None:
            archivo_inventario = seleccionar_archivo()
            inventario_inicial = cargar_inventario(archivo_inventario)
            print("\nInventario ingresado correctamente. Presione: 'Enter'", end=" ")
            input()
        elif inventario_inicial is not None:
            archivo_inventario2 = seleccionar_archivo()
            inventario_inicial.update(cargar_inventario(archivo_inventario2))
            print("\nSe agrego al Inventario correctamente. Presione: 'Enter'", end=" ")
            input()
            #mostrar_inventario(inventario_inicial)
    elif opcionSeleccionada == 2:
        archivo_movimiento = seleccionar_archivo_movimiento()
        if archivo_movimiento:
            with open(archivo_movimiento, 'r') as f:
                for linea in f:
                    instruccion, datos = linea.strip().split(' ', 1)
                    if instruccion == "agregar_stock":
                        nombre, cantidad, ubicacion = datos.split(';')
                        if nombre in inventario_inicial and ubicacion in inventario_inicial[nombre].ubicacion:
                            inventario_inicial[nombre].cantidad += int(cantidad)
                        else:
                            print(f"Error: Producto '{nombre}' no existe en la ubicación '{ubicacion}'.")
                    elif instruccion == "vender_producto":
                        nombre, cantidad, ubicacion = datos.split(';')
                        if nombre in inventario_inicial and ubicacion in inventario_inicial[nombre].ubicacion and int(cantidad)<=inventario_inicial[nombre].cantidad:
                            inventario_inicial[nombre].cantidad -= int(cantidad)
                        elif int(cantidad)>inventario_inicial[nombre].cantidad:
                            print(f"\nError: La cantidad a vender '{cantidad}' es mayor a la actual: '{inventario_inicial[nombre].cantidad}'.\n")
                        else:
                            print(f"\nError: Producto '{nombre}' no existe en la ubicación '{ubicacion}'.\n")
            print("\nInventario actualizado correctamente. Presione: 'Enter'", end=" ")
            input()
            #mostrar_inventario(inventario_inicial)
    elif opcionSeleccionada == 3:
        archivo_informe = "InformeInventario.txt"
    
        with open(archivo_informe, 'w') as f:
            f.write("---------------------------------------------------------------------------------------------------\n")
            f.write("Producto \t Cantidad\t Precio Unitario(Q.)\t Valor Total(Q.)\t Ubicación\n")
            f.write("---------------------------------------------------------------------------------------------------\n")
            for nombre, producto in inventario_inicial.items():
                valor_total = producto.cantidad * producto.precio_unitario
                f.write("{:15}\t{:8}\t{:18.2f}\t{:15.2f}\t\t{}\n".format(producto.nombre, producto.cantidad, producto.precio_unitario, valor_total, producto.ubicacion))
        
        print(f"\nInforme de inventario creado en '{archivo_informe}'. Presione 'Enter'", end=" ")
        input()
    elif opcionSeleccionada == 4:
        print("\nSaliendo del programa.\n")
        break
    else:
        print("Error: Ingrese un número válido.")
