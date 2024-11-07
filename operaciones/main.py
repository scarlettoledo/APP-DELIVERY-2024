#Clase a utilizar
from modelos.tipo_producto import TipoProducto
#archivo de operaciones de tipo_producto
from operaciones.tipo_producto_operaciones import TipoProductoOperaciones

def main():
    #creamos una instancia de operaciones
    operaciones = TipoProductoOperaciones()

    #Menu de opciones
    while True:
        print("*** Menú principal ***")
        print("1. Agregar tipo de producto")
        print("2. Listar tipo de producto")
        print("3. Salir")

        #capturamos la opcion seleccionada
        opcion= input("Seleccione una opción")

        #En caso de que la opción sea 1
        if opcion =="1":
            #Solicitamos los datos del nuevo tipo de producto
            nombre= input("Nomre del tipo de producto: ")
            descripcion= input("Descripción: ")

            #Creamos un objeto de la clase tipo producto
            nuevoTipoProducto = TipoProducto(nombre= nombre, descripcion=descripcion)
            
            # Agregamos registro a la base de datos mediante el objeto de la clase TipoProductoOperaciones
            resultado = operaciones.agregar(nuevoTipoProducto)
            
            #en caso de que la operación se ejecute correctamente
            if resultado:
                print(f"Tipo de Produto ingresado correctamente con ID: {resultado.id}")

