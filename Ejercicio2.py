import mysql.connector

def mostrar_datos(cursor):
    cursor.execute("SELECT * FROM test_table")
    print("\nDatos actuales de la tabla:")
    for row in cursor:
        print(row)

def insertar_registro(cursor, conexion):
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    nuevo_apellido = input("Ingrese el nuevo apellido: ")
    nuevo_registro = (nuevo_nombre, nuevo_apellido)
    cursor.execute("INSERT INTO test_table (firstName, lastName) VALUES (%s, %s)", nuevo_registro)
    conexion.commit()
    print("Nuevo registro insertado")
def actualizar_registro(cursor, conexion):
    user_id_a_actualizar = input("Ingrese el userId del registro a actualizar: ")
    mostrar_registro(cursor, user_id_a_actualizar)

    confirmacion = input("¿Está seguro de actualizar este registro? (s/n): ")
    if confirmacion.lower() == "s":
        nuevo_apellido = input("Ingrese el nuevo apellido: ")
        cursor.execute("UPDATE test_table SET lastName = %s WHERE userId = %s", (nuevo_apellido, user_id_a_actualizar))
        conexion.commit()
        print("Registro actualizado")
    else:
        print("Operación cancelada")

def eliminar_registro(cursor, conexion):
    user_id_a_eliminar = input("Ingrese el userId del registro a eliminar: ")
    mostrar_registro(cursor, user_id_a_eliminar)

    confirmacion = input("¿Está seguro de eliminar este registro? (s/n): ")
    if confirmacion.lower() == "s":
        cursor.execute("DELETE FROM test_table WHERE userId = %s", (user_id_a_eliminar,))
        conexion.commit()
        print("Registro eliminado")
    else:
        print("Operación cancelada")
def mostrar_registro(cursor, user_id):
    cursor.execute("SELECT * FROM test_table WHERE userId = %s", (user_id,))
    row = cursor.fetchone()
    
    if row:
        print("\nRegistro encontrado:")
        print(f"userId: {row[0]}, firstName: {row[1]}, lastName: {row[2]}")
    else:
        print(f"No se encontró un registro con userId {user_id}")

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="testdb"
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

while True:
    print("\n--- Menú ---")
    print("1. Mostrar datos")
    print("2. Insertar registro")
    print("3. Actualizar registro")
    print("4. Eliminar registro")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_datos(cursor)
    elif opcion == "2":
        insertar_registro(cursor, conexion)
    elif opcion == "3":
        actualizar_registro(cursor, conexion)
    elif opcion == "4":
        eliminar_registro(cursor, conexion)
    elif opcion == "0":
        break
    else:
        print("Opción no válida. Intente nuevamente.")

# Cerrar cursor y conexión
cursor.close()
conexion.close()