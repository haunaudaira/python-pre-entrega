# trae el modulo de sqlite
import sqlite3

# abrimos la conexión on la bd
connection = sqlite3.connect("products_db.db")

# creamos el cursor para interactuar con la bd
cursor = connection.cursor()

# tabla en la base de datos
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
    color TEXT NOT NULL,
	stock INTEGER NOT NULL
)
""")

# insertamos 10 productos y una vez cargados en la bd, los comentamos.
cursor.execute("""
INSERT INTO products (name, color, stock) VALUES
    ('Camiseta básica', 'Blanco', 50),
    ('Camiseta básica', 'Negro', 40),
    ('Jeans rectos', 'Azul', 30),
    ('Chaqueta de cuero', 'Negro', 15),
    ('Vestido de verano', 'Rojo', 20),
    ('Sudadera con capucha', 'Gris', 25),
    ('Falda plisada', 'Rosa', 10),
    ('Camisa de cuadros', 'Azul y blanco', 35),
    ('Pantalones cargo', 'Verde oliva', 18),
    ('Abrigo largo', 'Beige', 12);
""")
# guardamos los cambios realizados
connection.commit()
# cerramos la conexión del cursor
cursor.close()



# se puede dejar al final del código para cerrar la conexión de la bd
connection.close()
