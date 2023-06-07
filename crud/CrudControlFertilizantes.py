from model.ControlFertilizantes import ControlFertilizantes
from crud import ICrud

class CrudControlFertilizantes(ICrud.ICrud):
    lista_fertilizantes = []

    def crear(self, **kwargs):
        nuevo_fertilizante = ControlFertilizantes(kwargs['registro_ICA'], kwargs['nombre_producto'], kwargs['frecuencia_aplicacion'], kwargs['valor_producto'], kwargs['ultima_aplicacion'])
        self.lista_fertilizantes.append(nuevo_fertilizante)
        return nuevo_fertilizante

    def buscar(self, **kwargs):
        for fertilizante in self.lista_fertilizantes:
            if(fertilizante.obtener_registro_ICA == kwargs['registro_ICA']):
                return fertilizante

    def actualizar(self, **kwargs):
        fertilizante = self.buscar(registro_ICA=kwargs['registro_ICA_antes'])
        if fertilizante is not None:
            fertilizante.actualizar_fertilizante(kwargs['registro_ICA_despues'], kwargs['nombre_producto_despues'],kwargs['frecuencia_aplicacion_despues'], kwargs['valor_producto_despues'],kwargs['ultima_aplicacion_despues'])

            # Actualizar la lista:
            for i, fertilizante_lista in enumerate(self.lista_fertilizantes):
                if fertilizante_lista == fertilizante:
                    self.lista_fertilizantes[i].actualizar_fertilizante(kwargs['registro_ICA_despues'], kwargs['nombre_producto_despues'],kwargs['frecuencia_aplicacion_despues'], kwargs['valor_producto_despues'],kwargs['ultima_aplicacion_despues'])


    def eliminar(self, **kwargs):
        fertilizante = self.buscar(registro_ICA=kwargs['registro_ICA'])
        if fertilizante is not None:
            fertilizante.eliminar()

            # Eliminar de la lista
            self.lista_fertilizantes.remove(fertilizante)

    def relacion( self , ** kwargs ):
        pass