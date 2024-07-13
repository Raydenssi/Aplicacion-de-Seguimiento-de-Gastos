import funciones

def mostrar_menu():
    """
    Muestra el menú de opciones en la terminal y retorna la opción seleccionada por el usuario.
    
    :return: Opción seleccionada por el usuario.
    """
    print("\n--- Menú de Seguimiento de Gastos ---")
    print("1. Agregar Transacción")
    print("2. Listar Transacciones")
    print("3. Mostrar Balance")
    print("4. Guardar Datos")
    print("5. Cargar Datos")
    print("6. Salir")
    return input("Elige una opción: ")

print("\n")

# Menú de Opciones

def main():
    """
    Función principal que ejecuta el bucle principal del programa.
    """

    gestor = funciones.GestorFinanciero()
    gestor.cargar_datos()  # Cargar datos al inicio

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            # Agregar una nueva transacción
            monto = float(input("Monto: "))
            fecha = input("Fecha (YYYY-MM-DD): ")
            descripcion = input("Descripción: ")
            tipo = input("Tipo (Ingreso/Gasto): ")
            gestor.agregar_transaccion(monto, fecha, descripcion, tipo)
        elif opcion == '2':
            # Listar todas las transacciones
            gestor.listar_transacciones()
        elif opcion == '3':
            # Mostrar el balance actual
            ingresos, gastos, capacidad_ahorro = gestor.calcular_balance()
            print(f"Ingresos: ${ingresos:.2f}")
            print(f"Gastos: ${gastos:.2f}")
            print(f"Capacidad de Ahorro: ${capacidad_ahorro:.2f}")
        elif opcion == '4':
            # Guardar datos en el archivo
            gestor.guardar_datos()
            print("Datos guardados exitosamente.")
        elif opcion == '5':
            # Cargar datos desde el archivo
            gestor.cargar_datos()
            print("Datos cargados exitosamente.")
        elif opcion == '6':
            # Salir del programa
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()