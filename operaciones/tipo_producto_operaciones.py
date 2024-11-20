from mysql.connector import Error
from modelos import TipoProducto
from db_conexion import DatabaseConnection

class TipoProductoOperaciones:
    #Función para inicializar una conexión  base de datos...
    def __init__(self):
        self.db_conexion = DatabaseConnection()
    #Función para agregar un tipo de producto
    def agregar(self,tipo_producto):
        conexion = self.db_conexion.get_connection()
        try: 
            cursor = conexion.cursor() #cursor tiene los objetos de conexión que permite recorrer las tablas
            #Consulta SQL


            query ="insert into TipoProducto (nombre, descripcion) values (%s,%s)"

            #Extraemos valores de un objeto tipo producto
            valores = (tipo_producto.nombre, tipo_producto.descripcion) 
            #Ejecutamos la operación contra la base de datos (insertar)
            cursor.execute(query, valores)
            #Ejecutamos commit o una confirmación (es para confirmar el cambio y que quede actualizado en la base de datos.)
            conexion.commit()
            #Obtenemos el id del registro insertado
            tipo_producto.id_tipo_producto=cursor.lastrowid
            #Envíamos una confirmación
            print("Tipo de producto se ha ingresado correctamente.")
            return tipo_producto
        except Error as e:
            print(f"Error al insertar registro: {e}")
        finally:
            if cursor:
                cursor.close()

    #Función para obtener datos
    def obtener_datos(self):
        conexion=self.db_conexion.get_connection()
        try:
            cursor=conexion.cursor(dictionary=True)
            query="select *from TipoProducto"
            cursor.execute(query)
            resultados=cursor.fetchall() 
            return[TipoProducto(**resultado) for resultado in resultados]
        
        except Error as e:
            print(f"Error al consultar datos: {e}")
        finally:
            if cursor:
                cursor.close()
    #Función para actualizar datos
    def actualizar (self, tipo_producto):
        conexion = self.db_conexion.get_connection()
        try:
            cursor = conexion.cursor()
            query = "update TipoProducto set nombre = %s, descripcion=%s where id_tipo_producto= %s"
            valores = (tipo_producto.nombre, tipo_producto.descripcion, tipo_producto.id_tipo_producto)
            cursor.execute(query, valores)
            conexion.commit()
            return cursor.rowcount > 0 
        except Error as e:
            print(f"Error al actualizar el registro: {e}")
        finally:
            if cursor:
                cursor.close()
    #Función para eliminar datos
    def eliminar (self,id_tipo_producto):
        conexion= self.db_conexion.get_connection ()
        try:
            cursor = conexion.cursor()
            query = "delete from TipoProducto where id_tipo_producto = %s"
            cursor.execute(query,(id_tipo_producto,))
            conexion.commit ()
            return cursor.rowcount
        except Error as e:
            print(f"Error al eliminar el tipo de producto: {e}")
        finally:
            if cursor:
                cursor.close()

