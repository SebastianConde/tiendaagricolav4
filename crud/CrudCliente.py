from model.Clientes import Clientes

class CrudCliente():
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


    def eliminar_cliente(cls, numero_cedula):
        cliente = cls.buscar(numero_cedula)
        cliente.eliminar()

        #Eliminar de la lista
        cls.__clientes_creados.remove(cliente)

    def numero_clientes_registrados(cls):
        return len(cls.__clientes_creados)

    def obtener_clientes_registrados(cls):
        return cls.__clientes_creados

    def eliminar_todos_los_clientes(cls):
        cls.__clientes_creados = []






