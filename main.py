#Clases a utilizar
from modelos.tipo_producto import TipoProducto
from modelos.producto import Producto
from modelos.repartidor import Repartidor
#archivos de operaciones a utilizar
from operaciones.tipo_producto_operaciones import TipoProductoOperaciones
from operaciones.producto_operaciones import ProductoOperaciones
from operaciones.repartidor_operaciones import RepartidorOperaciones

#Creamos una función para seleccionar la opción a la cual queremos realizar una modificación
def seleccionar_opcion ():
    while True:
        print("** Seleccionar una opción **")
        print("1. Acceder a Tipo Producto")
        print("2. Acceder a Producto")
        print("3. Acceder a Repartidor")
        print("4. Salir") 

        seleccionar_opcion= input("Seleccione una opción: ")
        if seleccionar_opcion == "1":
            main_tipo_producto ()
        
        if seleccionar_opcion =="2":
            main_producto ()

        if seleccionar_opcion =="3":
            main_repartidor ()

        if seleccionar_opcion =="4":
            print("Saliendo del programa.")
            break

def main_tipo_producto():
    #creamos una instancia de operaciones para tipoProducto
    operaciones = TipoProductoOperaciones()

    #Menu de opciones
    while True:
        print("*** Menú principal ***")
        print("1. Agregar tipo de producto")
        print("2. Listar tipo de producto")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Salir")
        #capturamos la opcion seleccionada
        opcion= input("Seleccione una opción: ")

        #En caso de que la opción sea 1
        if opcion =="1":
            #Solicitamos los datos del nuevo tipo de producto
            nombre= input("Nombre del tipo de producto: ")
            descripcion= input("Descripción: ")

            #Creamos un objeto de la clase tipo producto
            nuevoTipoProducto = TipoProducto(nombre= nombre, descripcion=descripcion)
            
            # Agregamos registro a la base de datos mediante el objeto de la clase TipoProductoOperaciones
            resultado = operaciones.agregar(nuevoTipoProducto)
            
            #en caso de que la operación se ejecute correctamente
            if resultado:
                print(f"Tipo de Produto ingresado correctamente con ID: {resultado.id_tipo_producto}")

        if opcion == "2":
            tipos_productos = operaciones.obtener_datos() #función obtener_datos está definida con el objeto operaciones
            #Si existen tipos de productos los mostramos sino enviamos un mensaje al usuario
            if tipos_productos:
                print("*** Tipos de producto registrados ***")
                #Efectuamos un recorrido con los datos para mostrar los tipos de productos registrados
                for tipo in tipos_productos:
                    print(f"ID: {tipo.id_tipo_producto}") 
                    print(f"NOMBRE TIPO: {tipo.nombre}") 
                    print(f"DESCRIPCION: {tipo.descripcion}")
            else:
                print("No hay registro de tipo de producto")
       
       
         #En caso de actualizar  
        if opcion == "3":
            id = input("Ingrese id de tipo producto a actualizar: ")
            nombre =input("Ingrese nuevo nombre: ")
            descripcion = input("Nueva descripción: ")
            #Creamos un objeto de la clase TipoProducto
            tipo_producto = TipoProducto (id_tipo_producto=int(id), nombre=nombre, descripcion=descripcion) 
            #Verificamos si la operacion devuelve True lo cual indica que actualizó registros
            if operaciones.actualizar(tipo_producto):
                print("Registro actualizado correctamente")
            else: 
                print("No se actualizó ningún registro")
        #En caso de requerir eliminación
        if opcion == "4":
            id_tipo_producto=input("Ingrese id de tipo de producto a eliminar: ")
            if operaciones.eliminar(int(id_tipo_producto)): 
                print("Registro eliminado correctamente")
            else:
                print("No fue posible eliminar")


        if opcion == "5":
            print("Hasta Luego! ")
            break


def main_producto():
    #creamos una instancia de operaciones para ProductoOperaciones
    operaciones = ProductoOperaciones()

    #Nuevamente se muestra el Menu de opciones
    while True:
        print("*** Productos ***")
        print("1. Agregar un producto")
        print("2. Listar producto")
        print("3. Actualizar un producto")
        print("4. Eliminar un producto")
        print("5. Salir")
        #capturamos la opcion seleccionada
        opcion= input("Seleccione una opción: ")

        #En caso de que la opción sea 1
        if opcion =="1":
            #Solicitamos los datos del nuevo tipo de producto
            nombre= input("Nombre del producto: ")
            descripcion = input("Descripción: ")
            precio = input("Precio: ")
            id_tipo_producto=input("Tipo Producto: ")
            proveedor = input("Proveedor: ")

            #Creamos un objeto de la clase tipo producto
            nuevoProducto = Producto(nombre= nombre, descripcion = descripcion, precio=precio, id_tipo_producto=id_tipo_producto, proveedor=proveedor)
            
            # Agregamos registro a la base de datos mediante el objeto de la clase ProductoOperaciones
            resultado = operaciones.agregar(nuevoProducto)
            
            #en caso de que la operación se ejecute correctamente
            if resultado:
                print(f"Produto ingresado correctamente con ID: {resultado.id}")

        if opcion == "2":
            productos = operaciones.listar_datos() #función obtener_datos está definida con el objeto operaciones
            #Si existen productos los mostramos sino enviamos un mensaje al usuario
            if productos:
                print("*** Producto registrado ***")
                #Efectuamos un recorrido con los datos para mostrar los productos registrados
                for producto in productos:
                    print(f"ID: {producto.id}") 
                    print(f"NOMBRE PRODUCTO: {producto.nombre}") 
                    print(f"DESCRIPCION: {producto.descripcion}")
                    print(f"PRECIO:{producto.precio} ")
                    print(f"ID TIPO PRODUCTO: {producto.id_tipo_producto}")
                    print(f"PROVEEDOR: {producto.proveedor}")
            else:
                print("No hay registro del producto")
       
       
         #En caso de actualizar  
        if opcion == "3":
            id = input("Ingrese id de tipo producto a actualizar: ")
            nombre =input("Ingrese nuevo nombre: ")
            descripcion= input("Nueva descripción: ")
            precio = input ("Ingrese precio actualizado: ")
            id_tipo_producto= input("Ingrese nuevo id tipo producto: ")
            proveedor= input ("Ingrese nuevo Proveedor: ")
            #Creamos un objeto de la clase Producto
            producto = Producto (id=int(id), nombre= nombre, descripcion = descripcion, precio=precio, id_tipo_producto=id_tipo_producto, proveedor=proveedor) 
            #Verificamos si la operacion devuelve True, lo que indica que actualizó registros
            if operaciones.actualizar(producto):
                print("Registros actualizados ")
            else: 
                print("No se pudo registrar la actualización")
        #En caso de requerir eliminación
        if opcion == "4":
            id=input("Ingrese id del producto a eliminar: ")
            if operaciones.eliminar(int(id)): 
                print("Registro eliminado correctamente")
            else:
                print("No fue posible eliminar")


        if opcion == "5":
            print(" El programa ha sido cerrado.")
            break


def main_repartidor():
    operaciones = RepartidorOperaciones()

    while True:
        print(" *** Menú principal *** ")
        print("1. Agregar nuevo Repartidor")
        print("2. Listar repartidores")
        print("3. Actualizar Repartidor")
        print("4. Eliminar Repartidor")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            rut = input("Rut del repartidor: ")
            nombre = input("Nombre del repartidor: ")
            apellidos = input("apellido del repartidor: ")
            telefono = input("Telefono del repartidor: ")
            estado = input("Estado: ")

            nuevoRepartidor = Repartidor(rut = rut, nombre = nombre, apellidos = apellidos, telefono = telefono, estado = estado)

            resultado = operaciones.agregar(nuevoRepartidor)

            if resultado:
                print(f" Repartidor ingresado correctamente con ID : {resultado.id} ")


        if opcion == "2":
            
            repartidores = operaciones.listar_datos()
            if repartidores:
                print("Repartidores")
                for repartidor in repartidores:
                    print(f"ID: {repartidor.id}")
                    print(f"Rut: {repartidor.rut}")
                    print(f"Nombre: {repartidor.nombre}")
                    print(f"Apellidos: {repartidor.apellidos}")
                    print(f"estado: {repartidor.estado}'")
                                    
            else:
                print("No hay Repartidores registrados.")

        if opcion == "3":
            id = input("ingrese id del repartidor a actualizar: ")
            nuevo_rut = input("Nuevo rut: ")
            nuevo_nombre = input("Nuevo nombre : ")
            nuevo_apellidos  = input("Nuevos apellidos: ")
            nuevo_telefono = input("Nuevo telefono: ")
            nuevo_estado = input("Nuevo estado: ")
            repartidor = Repartidor(id = int(id),rut = nuevo_rut, nombre = nuevo_nombre, apellidos = nuevo_apellidos, telefono = nuevo_telefono, estado = nuevo_estado)
            
            #Verificamos si la operacion devuelve true, lo que indica que actualizó registros
            if operaciones.actualizar(repartidor):
                print("Registros actualizados ")
            else: 
                print("No se pudo registrar la actualización")

        if opcion == "4":
            id = input("Ingrese el id del repartidor a eliminar: ")
            if operaciones.eliminar(int(id)):

                print("Repartidor eliminado correctamente.")
            else:
                print("El repartidor no se ha podido eliminar.")

        if opcion == "5":
            print("programa finalizado")
            break


if __name__== "__main__": 
    seleccionar_opcion ()


