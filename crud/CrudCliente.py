from model.Clientes import Clientes

class CrudCliente():
    __clientes_creados = []

    @classmethod
    def crear_cliente(cls, nombre, numero_cedula):
        nuevo_cliente = Clientes(nombre, numero_cedula)
        cls.__clientes_creados.append(nuevo_cliente)
        return nuevo_cliente

    @classmethod
    def buscar_por_cedula(cls, numero_cedula):
        for cliente in cls.__clientes_creados:
            if(cliente.obtener_cedula == numero_cedula):
                return cliente

    @classmethod
    #Solo se actualiza nombre porque la cedula no es actualizable
    def actualizar_nombre_cliente(cls, numero_cedula, nombre_nuevo):
        cliente = cls.buscar_por_cedula(numero_cedula)
        cliente.nombre_cliente = nombre_nuevo

        #Actualizar nombre en la lista:
        for i, cliente_lista in enumerate(cls.__clientes_creados):
            if cliente_lista == cliente:
                cls.__clientes_creados[i].nombre_cliente = nombre_nuevo

    @classmethod
    def eliminar_cliente(cls, numero_cedula):
        cliente = cls.buscar_por_cedula(numero_cedula)
        cliente.eliminar()

        #Eliminar de la lista
        cls.__clientes_creados.remove(cliente)

    @classmethod
    def numero_clientes_registrados(cls):
        return len(cls.__clientes_creados)

    @classmethod
    def obtener_clientes_registrados(cls):
        return cls.__clientes_creados

    @staticmethod
    def mostrar_clientes():
        print("Clientes registrados:")
        print("------------------------------")
        for cliente_registrado in CrudCliente.__clientes_creados:
            cliente_registrado.mostrar_cliente()
            print("------------------------------")


    @classmethod
    def eliminar_todos_los_clientes(cls):
        cls.__clientes_creados = []






