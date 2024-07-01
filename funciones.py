import pickle

# Registro de Transacciones

transacciones = []

# Variable para llevar el registro del balance total

balance = float(0)

def registrar_transaccion():
    """
        Esta función permite ingresar una transacción.

        returns: (str: tipo)
    """
    from app import opcion

    global balance
    # Verificar si es Ingreso o Gasto
    if opcion == 1:
        tipo = "Ingreso"
    elif opcion == 2:
        tipo = "Gasto"
    else:
        print("La opción no es válida.")
    
    # Pedir al usuario que ingrese la información de la transacción
    monto = float(input("Monto: $"))
    fecha = str(input("Fecha (YYYY-MM-DD): "))
    descripcion = input("Ingrese la descripción: ")
    
    # Crear un diccionario para la transacción
    transaccion = {"monto": monto, "fecha": fecha, "descripcion": descripcion, "tipo": tipo}
    # Agregar la transacción a la lista
    transacciones.append(transaccion)

    # Se suma o se resta al balance
    if tipo == "Ingreso":
        balance += monto
    elif tipo == "Gasto":
        balance -= monto
    else:
        print("La opción no es válida.")
    
    print("¡Transacción agregada con éxito!")

def listar_transacciones():
    # Mostrar todas las transacciones
    for i, transaccion in enumerate(transacciones):
        print(f"Transacción {i+1}:")
        print(transaccion['tipo'])
        print(f"Monto: ${transaccion['monto']}")
        print(f"Fecha: {transaccion['fecha']}")
        print(f"Descripción: {transaccion['descripcion']}")
        print()

def guardar_transacciones():
    # Serializar la lista de transacciones y guardarla en un archivo.pkl
    with open("transacciones.pkl", "wb") as f:
        pickle.dump(transacciones, f)

    print("¡Transacciones guardadas con éxito!")

def cargar_transacciones():
    # Cargar la lista de transacciones desde el archivo.pkl
    global transacciones
    try:
        with open("transacciones.pkl", "rb") as f:
            transacciones = pickle.load(f)
    except FileNotFoundError:
        print("No hay transacciones guardadas.")

def mostrar_balance():
    print(f"El balance actual es de ${balance}.")