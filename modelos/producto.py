from datetime import datetime

class Producto:
    def __init__(self, id=None, nombre="", descripcion="", precio=0.0, id_tipo_producto=None, proveedor="", fecha_ingreso=None):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.precio=precio
        self.id_tipo_producto=id_tipo_producto
        self.proveedor=proveedor
        self.fecha_ingreso=fecha_ingreso if fecha_ingreso else datetime.now ()
    def __str__(self):
        return f"Producto(id={self.id} nombre='{self.nombre}', descripcion ='{self.descripcion}', precio={self.precio}, id_tipo_producto={self.id_tipo_producto}, proveedor='{self.proveedor}', fecha_ingreso= {self.fecha_ingreso})"
        