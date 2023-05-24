from .Facturas import Facturas

class Clientes():
    def __init__(self, nombre_cliente, numero_cedula):
        self.__nombre_cliente = nombre_cliente
        self.__numero_cedula = numero_cedula
        self.__facturas = []


    def lista_facturas_asociadas(self):
        return self.__facturas

    def facturas_asociadas(self):
        return len(self.__facturas)

    def mostrar_cliente(self):
        print("Nombre del cliente: ", self.nombre_cliente)
        print("Número de cedula: ", self.obtener_cedula)

    def agregar_factura(self, factura):
        factura.recibir_datos_cliente(self)
        self.__facturas.append(factura)

    def mostrar_facturas(self):
        print("------------------------------")
        print("Las facturas asociadas al cliente:")
        print("------------------------------")
        for factura_registrada in self.__facturas:
            factura_registrada.mostrar_factura()
            print("------------------------------")

    @property
    def nombre_cliente(self):
        return self.__nombre_cliente

    @property
    def obtener_cedula(self):
        return self.__numero_cedula

    @nombre_cliente.setter
    def nombre_cliente(self, nombre_nuevo):
        self.__nombre_cliente = nombre_nuevo

    def eliminar(self):
        self.__nombre_cliente = None
        self.__numero_cedula = None
        self.__facturas = None
        del self

    def eliminar_factura(self, factura):
        for i, factura_asociada in enumerate(self.__facturas):
            if(factura_asociada == factura):
                del self.__facturas[i]

