# trae el modulo de sqlite
import sqlite3

# funciones 
def agregar_producto():
    # establecemos la conexión con la base de datos para almacenar y actualizar la información
    connection = sqlite3.connect("products_db.db")
    # solicitamos el nombre, color y cantidad del producto
    name = input("Ingrese el nombre del producto: ")
    color = input("Color del producto: ")
    stock = int(input("Ingrese la cantidad del producto: "))
    # lo guardamos en la base de datos
    cursor = connection.cursor()
    # ejecutamos la consulta para guardar un nuevo producto
    cursor.execute("""
    INSERT INTO products (name, color, stock) values (?, ?, ?)
""", (name, color, stock))
    # confirmamos en la base de datos la acción realizada y cerramos el cursor
    connection.commit( )
    cursor.close()
    print("producto agregado correctamente")

# la siguiente función nos muestra todos los productos del inventario
def mostrar_productos():
    connection = sqlite3.connect("products_db.db")
    cursor = connection.cursor()
    # ejecutamos la consulta para obtener todos los productos
    cursor.execute("SELECT * FROM products")
    # obtenemos todos los resultados
    productos = cursor.fetchall()
    cursor.close()
    # si no hay productos se informa a traves del mensaje
    if not productos:
        print("No hay productos en el inventario.")
    # si hay productos, se muestran
    else:
        for producto in productos:
            print(f"ID: {producto[0]}, Producto: {producto[1]}, Color: {producto[2]}, Cantidad: {producto[3]}") #utilizando f-string


# actualizamos las cantidades de stock disponibles de un producto. Ya sea que aumente o decremente.
def actualizar_productos():
    connection = sqlite3.connect("products_db.db")
    cursor = connection.cursor()
    # solicitamos al usuario que ingrese el ID del producto que desea actualizar y la cantidad a modificar
    producto_id = int(input("Ingrese el ID del producto a actualizar:"))
    nueva_cantidad = int(input("Ingrese la nueva cantidad:"))
    #ejecutamos la consulta para poder actualizar la cantidad del producto y se notifica en la terminal.
    cursor.execute("UPDATE products SET stock = ? WHERE id = ?", (nueva_cantidad, producto_id))
    connection.commit()
    connection.close()
    print("Cantidad actualizada")

# función para eliminar un producto del inventario ingresando su ID
def eliminar_producto():
    connection = sqlite3.connect("products_db.db")
    cursor = connection.cursor()
    producto_id = int(input("Ingrese el ID del producto a eliminar: "))
    cursor.execute("DELETE FROM products WHERE id = ?", (producto_id,))
    connection.commit()
    connection.close()
    print("Producto eliminado exitosamente.")

# función para buscar un producto por su nombre
def buscar_producto():
    connection = sqlite3.connect("products_db.db")
    cursor = connection.cursor()
    name = input("Ingrese el nombre del producto a buscar:")
    # utilizamos la herramienta de sql % que nos permite buscar un producto por el nombre ingresado
    cursor.execute("SElECT * FROM products WHERE name LIKE ?", ('%' + name + '%',))
    productos = cursor.fetchall()
    connection.close()
    if not productos:
        print ("No se encontraron productos con ese nombre")
    else: 
        print ("\n--- Resultado de búsqueda ---")
        for producto in productos:
            print(f"ID: {producto[0]}, Producto: {producto[1]}, Color: {producto[2]}, Cantidad: {producto[3]}")

# reporte informa bajo stock considerando los productos que tengan 4 o menos unidades.
def reporte_bajo_stock():
    connection = sqlite3.connect("products_db.db")
    cursor = connection.cursor()
    # en la linea comentada abajo, nos permitiría ingresar manualmente lo que considera el usuario bajo stock
    # limite = int(input("Ingrese el límite considerable como bajo stock: "))
    cursor.execute("SELECT * FROM products WHERE stock <= 4 ") # de utilizar la línea "limite", esta linea se modifica desde la palabra stock de la siguiente manera: stock < ?", (limite,))
    productos_bajostock = cursor.fetchall()
    cursor.close()
    if not productos_bajostock:
        print("No hay productos con bajo stock")
    else: 
        print("\n--- Reporte de Bajo Stock ---")
        for producto in productos_bajostock:
            print(f"ID: {producto[0]}, Producto: {producto[1]}, Color: {producto[2]}, Cantidad: {producto[3]}")


# abrimos la conexión on la bd
connection = sqlite3.connect("products_db.db")
inventario = []
# menú principal iría acá debajo
opcion = "in"

while True:
    print("""
    Menú del inventario
    1. Agregar producto
    2. Mostrar productos
    3. Actualizar cantidad de producto
    4. Eliminar producto
    5. Buscar producto
    6. Reporte de bajo stock
    7. Salir
    """)

# función principal
    opcion = input("Seleccione una opción (1-7): ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        actualizar_productos()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        buscar_producto()
    elif opcion == "6":
        reporte_bajo_stock()
    elif opcion == "7":
        print("¡Hasta luego!")
        connection.close()  # cerramos la conexión al final
        break # cerramos el bucle
    else:
        print("Opción inválida. Intente de nuevo.")