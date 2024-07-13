import pickle
from datetime import datetime
from typing import List

# Clase que representa una transacción
class Transaccion:
    def __init__(self, monto: float, fecha: str, descripcion: str, tipo: str):
        """
        Inicializa una nueva transacción.
        
        :param monto: Monto de la transacción.
        :param fecha: Fecha de la transacción en formato 'YYYY-MM-DD'.
        :param descripcion: Descripción de la transacción.
        :param tipo: Tipo de transacción ('Ingreso' o 'Gasto').
        """
        self.monto = monto
        self.fecha = datetime.strptime(fecha, '%Y-%m-%d')
        self.descripcion = descripcion
        self.tipo = tipo

    def __repr__(self):
        """
        Representación de la transacción en formato legible.
        """
        return f"{self.fecha.date()} - {self.tipo} - {self.descripcion}: ${self.monto:.2f}"

# Clase que gestiona las transacciones financieras
class GestorFinanciero:
    def __init__(self):
        """
        Inicializa el gestor financiero con una lista vacía de transacciones.
        """
        self.transacciones: List[Transaccion] = []

    def agregar_transaccion(self, monto: float, fecha: str, descripcion: str, tipo: str):
        """
        Agrega una nueva transacción a la lista.
        
        :param monto: Monto de la transacción.
        :param fecha: Fecha de la transacción en formato 'YYYY-MM-DD'.
        :param descripcion: Descripción de la transacción.
        :param tipo: Tipo de transacción ('Ingreso' o 'Gasto').
        """
        transaccion = Transaccion(monto, fecha, descripcion, tipo)
        self.transacciones.append(transaccion)

    def listar_transacciones(self):
        """
        Muestra todas las transacciones ordenadas por fecha.
        """
        for transaccion in sorted(self.transacciones, key=lambda x: x.fecha):
            print(transaccion)

    def calcular_balance(self):
        """
        Calcula y retorna el balance financiero actual.
        
        :return: Una tupla con el total de ingresos, el total de gastos y la capacidad de ahorro.
        """
        ingresos = sum(t.monto for t in self.transacciones if t.tipo == 'Ingreso')
        gastos = sum(t.monto for t in self.transacciones if t.tipo == 'Gasto')
        capacidad_ahorro = ingresos - gastos
        return ingresos, gastos, capacidad_ahorro

    def guardar_datos(self):
        """
        Guarda la lista de transacciones en un archivo utilizando pickle.
        """
        with open('datos_financieros.pkl', 'wb') as f:
            pickle.dump(self.transacciones, f)

    def cargar_datos(self):
        """
        Carga la lista de transacciones desde un archivo utilizando pickle.
        Si el archivo no existe, inicializa la lista de transacciones como vacía.
        """
        try:
            with open('datos_financieros.pkl', 'rb') as f:
                self.transacciones = pickle.load(f)
        except FileNotFoundError:
            self.transacciones = []