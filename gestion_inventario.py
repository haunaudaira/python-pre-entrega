#   INVENTARIO DE ROPA

# lista vacía que almacena los productos del inventario
inventario = []

#
def mostrar_menu():
    print ("""
    Menú del inventario
        1. Agregar producto
        2. Mostrar inventario 
        3. Salir
           """)

# función que es llamada más abajo, sirve para agregar los productos al inventario
def agregar_producto():
    # solicitamos el nombre, color y cantidad del producto
    nombre = input("Ingrese el nombre del producto: ")
    color = input("Color del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    # implementacion de un diccionario que va a almacenar los datos de los productos que sean cargados
    producto = {"nombre": nombre, "color": color,"cantidad": cantidad}
    
    # agregamos el producto a la lista del inventario
    inventario.append(producto)

# función para mostrar el inventario
def mostrar_inventario():
    # verifica si el inventario está vacío
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        print("\n--- Inventario ---")
        # recorre la lista y muestra cada producto, si es que hay
        for producto in inventario:
            print(f"Producto: {producto['nombre']}, Cantidad: {producto['cantidad']}")

# función principal de ejecución
def main():
    while True: # el bucle while true permite que el programa entre en un "bucle infinito" hasta que reciba la orden "break" y se detenga
        mostrar_menu()  # mostramos el menú
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == "1":
            agregar_producto()  # si se selecciona, inicia la función correspondiente
        elif opcion == "2":
            mostrar_inventario()  # si se selecciona, inicia la función correspondiente
        elif opcion == "3":
            print("¡Chau!")  # salir del programa
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")  # si se intenta acceder a un índice que no existe

# ejecutar el programa
if __name__ == "__main__":
    main()
