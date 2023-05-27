from .ControlFertilizantes import ControlFertilizantes
from .ControlPlagas import ControlPlagas
from .Antibiotico import Antibioticos
from datetime import datetime

class Facturas:
    def __init__(self):
        self.__productos_comprados = []
        self.__datos_cliente = None
        self.__fecha = datetime.now()
        self.__total = 0.00

    def recibir_datos_cliente(self, cliente):
        self.__datos_cliente = cliente

    @property
    def obtener_fecha(self):
        return self.__fecha

    @property
    def obtener_total(self):
        return self.__total

    def agregar_productos(self, producto, cantidad):
        producto.obtener_cantidad = cantidad
        self.__total += (float(cantidad) * float(producto.obtener_valor))
        for _ in range(cantidad):
            self.__productos_comprados.append(producto)

    def numero_productos_comprados(self):
        return len(self.__productos_comprados)


    def lista_productos_comprados(self):
        return self.__productos_comprados

