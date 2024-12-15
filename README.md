# Proyecto Final Integrador - Iniciación a la Programación con Python

Este proyecto fue realizado como parte del curso **"Iniciación a la programación con Python"** y consiste en una aplicación que gestiona un inventario de productos utilizando una base de datos SQLite. La aplicación permite registrar, actualizar, eliminar y buscar productos, así como generar un reporte de productos con bajo stock.

## Requisitos
La aplicación cumple con los siguientes requisitos:

### 1. Base de Datos

Se utilizó **SQLite** para implementar una base de datos que almacena la información de los productos en el inventario.

### 2. Funcionalidades de la Aplicación

#### Registro de Productos
La aplicación permite al usuario agregar un nuevo producto al inventario. Para ello, se solicita al usuario ingresar:
  - Nombre del producto
  - Color del producto
  - Cantidad disponible del producto

#### Visualización de Productos
La aplicación muestra todos los productos registrados en el inventario. Se muestra la siguiente información de cada producto:
  - ID del producto
  - Nombre del producto
  - Color del producto
  - Cantidad disponible del producto

#### Actualización de Productos
El usuario puede actualizar la cantidad disponible de un producto específico. Para ello, se solicita el **ID** del producto y la nueva cantidad a actualizar.

#### Eliminación de Productos
La aplicación permite al usuario eliminar un producto del inventario. Para ello, se solicita el **ID** del producto a eliminar.

#### Búsqueda de Productos
La aplicación ofrece una funcionalidad para buscar productos por su nombre. Los resultados de la búsqueda muestran los productos que coinciden con el nombre ingresado.

#### Reporte de Bajo Stock
La aplicación genera un reporte de productos cuyo stock sea igual o inferior a un límite especificado por el usuario. Este reporte permite al usuario conocer qué productos tienen bajo stock y necesitan ser reabastecidos.
