from model.ControlPlagas import ControlPlagas
from crud import ICrud

class CrudControlPlagas(ICrud.ICrud):
    lista_plagas = []

    def crear(self, **kwargs):
        nueva_plaga = ControlPlagas(kwargs['registro_ICA'], kwargs['nombre_producto'], kwargs['frecuencia_aplicacion'], kwargs['valor_producto'], kwargs['periodo_carencia'])
        self.lista_plagas.append(nueva_plaga)
        return nueva_plaga

    def buscar(self, **kwargs):
        for plaga in self.lista_plagas:
            if(plaga.obtener_registro_ICA == kwargs['registro_ICA']):
                return plaga

    def actualizar(self, **kwargs):
        plaga = self.buscar(registro_ICA=kwargs['registro_ICA_antes'])

        if plaga is not None:
            plaga.actualizar_plaga(kwargs['registro_ICA_despues'], kwargs['nombre_producto_despues'],kwargs['frecuencia_aplicacion_despues'], kwargs['valor_producto_despues'], kwargs['periodo_carencia_despues'])

            #Actualizar la lista:
            for i, plaga_lista in enumerate(self.lista_plagas):
                if plaga_lista == plaga:
                   self.lista_plagas[i].actualizar_plaga(kwargs['registro_ICA_despues'], kwargs['nombre_producto_despues'],kwargs['frecuencia_aplicacion_despues'], kwargs['valor_producto_despues'], kwargs['periodo_carencia_despues'])


    def eliminar(self, **kwargs):
        plaga = self.buscar(registro_ICA=kwargs['registro_ICA'])
        if plaga is not None:
            plaga.eliminar()

            # Eliminar de la lista
            self.lista_plagas.remove(plaga)

    def relacion( self , ** kwargs ):
        pass