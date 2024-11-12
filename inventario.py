#   INVENTARIO DE ROPA

# lista vacía que almacena los productos del inventario
inventario = []

while True:
    print ("""
    Menú del inventario
        1. Agregar producto
        2. Mostrar inventario 
        3. Salir
           """)
    
# capta la opción ingresada por el usuario
    option = input("Ingrese el número para su elección: ")

# código para agregar productos al inventario
    if option == "1":
        name = input ("Ingrese el nombre del producto: ")
        color = input ("Color del producto: ")
        stock = int(input("Ingrese la cantidad de producto a cargar: "))

    # diccionario que almacena los datos del producto
        product = { "name": name, "color": color, "stock": stock }

    # agrega a la lista del inventario el producto ingresado por el usuario
        inventario.append(product)

    elif option == "2":
        # muestra el inventario
        if len(inventario) == 0:
            print("El inventario está vacío")
        else:
            print("\n--- Inventario ---")
            for product in inventario:
                print("Producto:", product['name'])
                print("Color:", product['color'])
                print("Cantidad:", product['stock'])

    elif option == "3":
        # salir del programa
        print("Chau!")
        break

    else: 
        print ("Opción inválida")