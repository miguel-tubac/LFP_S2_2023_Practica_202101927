
class Producto:
    def __init__(self, nombre, cantidad, precio_unitario, ubicacion):
        self.nombre = nombre
        self.cantidad = int(cantidad)
        self.precio_unitario = float(precio_unitario)
        self.ubicacion = ubicacion

def cargar_inventario(archivo):
    inventario = {}
    
    with open(archivo, 'r') as f:
        for linea in f:
            instruccion, datos = linea.strip().split(' ', 1)
            if instruccion == "crear_producto":
                nombre, cantidad, precio_unitario, ubicacion = datos.split(';')
                producto = Producto(nombre, cantidad, precio_unitario, ubicacion)
                inventario[nombre] = producto
    
    return inventario
