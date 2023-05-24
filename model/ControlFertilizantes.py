from .ProductoControl import ProductoControl

class ControlFertilizantes(ProductoControl):
    def __init__(self, registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto, ultima_aplicacion):
        super().__init__(registro_ICA, nombre_producto, frecuencia_aplicacion, valor_producto)
        self.__ultima_aplicacion = ultima_aplicacion

    @property
    def obtener_registro_ICA(self):
        return super().obtener_registro_ICA

    def actualizar_fertilizante(self, registro_ICA_despues, nombre_producto_despues, frecuencia_aplicacion_despues, valor_producto_despues, ultima_aplicacion_despues):
        self.actualizar_producto_control(registro_ICA_despues, nombre_producto_despues, frecuencia_aplicacion_despues, valor_producto_despues)
        self.__ultima_aplicacion = ultima_aplicacion_despues

    def eliminar(self):
        self.actualizar_producto_control(None, None, None, None)
        self.__ultima_aplicacion = None
        del self

    @property
    def obtener_nombre(self):
        return super().obtener_nombre

    @property
    def obtener_frecuencia(self):
        return super().obtener_frecuencia

    @property
    def obtener_valor(self):
        return super().obtener_valor

    @property
    def obtener_ultima(self):
        return self.__ultima_aplicacion


