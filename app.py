import funciones

# Bucle Principal
while True:

    # Menú de Opciones 

    print("\n***** --- Aplicación de Seguimiento de Gastos --- *****\n")
    print("1. Registrar Ingreso")
    print("2. Registrar Gasto")
    print("3. Listar Transacciones")
    print("4. Mostrar Balance")
    print("5. Salir")

    print("\n")

    # Entrada de Datos
    opcion = int(input("Introduzca una ocpión: "))

    print("\n")

    # Menú de Opciones

    match opcion:
        case 1:
            funciones.registrar_transaccion()
        case 2:
            funciones.registrar_transaccion()
        case 3:
            funciones.listar_transacciones()
        case 4:
            funciones.mostrar_balance()
        case 5:
            print("Gracias por utilizar el seguimiento de gastos.")
            break
        case _:
            print("Opción inválida.")