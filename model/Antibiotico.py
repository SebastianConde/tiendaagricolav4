class Antibioticos:
    def __init__(self, nombre_producto, dosis, tipo_animal, valor_producto):
        self.__nombre_producto = nombre_producto
        self.__dosis = dosis
        self.__tipo_animal = tipo_animal
        self.__valor_producto = valor_producto
        self.__cantidad = 0.00

    @property
    def obtener_cantidad(self):
        return self.__cantidad

    @obtener_cantidad.setter
    def obtener_cantidad(self, cantidad):
        self.__cantidad = cantidad

    @property
    def obtener_valor(self):
        return self.__valor_producto

    @property
    def obtener_nombre(self):
        return self.__nombre_producto

    @property
    def obtener_dosis(self):
        return self.__dosis

    @property
    def obtener_tipo(self):
        return self.__tipo_animal

    def actualizar_antibiotico(self, nombre_producto_despues, dosis_despues, tipo_animal_despues, valor_producto_despues):
        self.__nombre_producto = nombre_producto_despues
        self.__dosis = dosis_despues
        self.__tipo_animal = tipo_animal_despues
        self.__valor_producto = valor_producto_despues

    def eliminar(self):
        self.__nombre_producto = None
        self.__dosis = None
        self.__tipo_animal = None
        self.__valor_producto = None
        del self
