class ProductoControl:
    __productos_control = []

    def __init__(self, registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto):

        self.__registro_ICA = registro_ICA
        self.__nombre_producto = nombre_producto
        self.__frecuencia_aplicacion = frecuencia_aplicacion
        self.__valor_producto = valor_producto
        self.__cantidad = 0.00
        self.__class__.__productos_control.append(self)

    def actualizar_producto_control(self, registro_ICA_despues, nombre_producto_despues, frecuencia_aplicacion_despues, valor_producto_despues):
        self.__registro_ICA = registro_ICA_despues
        self.__nombre_producto = nombre_producto_despues
        self.__frecuencia_aplicacion = frecuencia_aplicacion_despues
        self.__valor_producto = valor_producto_despues

    @property
    def obtener_cantidad(self):
        return self.__cantidad

    @obtener_cantidad.setter
    def obtener_cantidad(self, cantidad):
        self.__cantidad = cantidad

    @property
    def obtener_registro_ICA(self):
        return self.__registro_ICA

    @property
    def obtener_nombre(self):
        return self.__nombre_producto

    @property
    def obtener_frecuencia(self):
        return self.__frecuencia_aplicacion

    @property
    def obtener_valor(self):
        return self.__valor_producto



