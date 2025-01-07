# Sistema de Gestión de Productos, Tipos de Productos y Repartidores para Delivery

Este es un proyecto de simulación de un sistema de gestión para una empresa de delivery. El sistema permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre tres entidades principales: productos, tipos de productos y repartidores.

El sistema está implementado utilizando **programación orientada a objetos (POO)** y se conecta a una base de datos **MySQL** que reside en una máquina virtual **CentOS 8** gestionada mediante **VirtualBox**.

## Tecnologías Utilizadas

- **Lenguaje de Programación**: Python
- **Base de Datos**: MySQL (a través de MySQL Workbench)
- **Máquina Virtual**: VirtualBox (con CentOS 8)
- 
## Funcionalidades

El sistema permite las siguientes operaciones CRUD:

### Productos
- **Crear Producto**: Registrar un nuevo producto con información relevante como nombre, descripción, precio, etc.
- **Leer Producto**: Consultar productos existentes en la base de datos.
- **Actualizar Producto**: Modificar la información de un producto.
- **Eliminar Producto**: Eliminar un producto del sistema.

### Tipos de Productos
- **Crear Tipo de Producto**: Definir y registrar diferentes tipos de productos.
- **Leer Tipo de Producto**: Consultar los tipos de productos disponibles.
- **Actualizar Tipo de Producto**: Modificar un tipo de producto existente.
- **Eliminar Tipo de Producto**: Eliminar un tipo de producto.

### Repartidores
- **Crear Repartidor**: Registrar un repartidor con su información de contacto y detalles relevantes.
- **Leer Repartidor**: Consultar información de los repartidores.
- **Actualizar Repartidor**: Modificar la información de un repartidor.
- **Eliminar Repartidor**: Eliminar un repartidor.

## Estructura de la Base de Datos

El sistema utiliza una base de datos en MySQL con las siguientes tablas principales:
- **Productos**: Almacena información sobre los productos que la empresa gestiona.
- **Tipos de Productos**: Guarda los diferentes tipos de productos disponibles.
- **Repartidores**: Contiene la información de los repartidores que entregan los productos.

El esquema de la base de datos fue diseñado en **MySQL Workbench** y se encuentra conectado a la máquina virtual a través de **CentOS 8**.
