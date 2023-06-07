from model.Clientes import Clientes
from crud import ICrud

class CrudCliente(ICrud.ICrud):
    __clientes_creados = []

    def crear(self, **kwargs):
        nuevo_cliente = Clientes(kwargs['nombre'], kwargs['numero_cedula'])
        self.__clientes_creados.append(nuevo_cliente)
        return nuevo_cliente

    def buscar(self, **kwargs):
        for cliente in self.__clientes_creados:
            if(cliente.obtener_cedula == kwargs['numero_cedula']):
                return cliente

    #Solo se actualiza nombre porque la cedula no es actualizable
    def actualizar(self, **kwargs):
        cliente = self.buscar(numero_cedula=kwargs['numero_cedula'])
        cliente.nombre_cliente = kwargs['nombre_nuevo']

        #Actualizar nombre en la lista:
        for i, cliente_lista in enumerate(self.__clientes_creados):
            if cliente_lista == cliente:
                self.__clientes_creados[i].nombre_cliente = kwargs['nombre_nuevo']


    def eliminar(self, **kwargs):
        cliente = self.buscar(numero_cedula=kwargs['numero_cedula'])
        cliente.eliminar()

        #Eliminar de la lista
        self.__clientes_creados.remove(cliente)

    def relacion(self, **kwargs):
        cliente = kwargs['cliente']
        factura = kwargs['factura']

        if cliente is not None and factura is not None:
            cliente.agregar_factura(factura)
            return cliente

    @classmethod
    def numero_clientes_registrados(cls):
        return len(cls.__clientes_creados)

    @classmethod
    def obtener_clientes_registrados(cls):
        return cls.__clientes_creados

    @classmethod
    def eliminar_todos_los_clientes(cls):
        cls.__clientes_creados = []






