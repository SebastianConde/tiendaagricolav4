from model.Antibiotico import Antibioticos
from crud import ICrud

class CrudAntibiotico(ICrud.ICrud):
    lista_antibioticos = []

    def crear(self, **kwargs):
        nuevo_antibiotico = Antibioticos(kwargs['nombre_producto'], kwargs['dosis'], kwargs['tipo_animal'], kwargs['valor_producto'])
        self.lista_antibioticos.append(nuevo_antibiotico)
        return nuevo_antibiotico

    def actualizar(self, **kwargs):
        antibiotico = self.buscar(nombre_producto=kwargs['nombre_producto_antes'])

        if antibiotico is not None:
            antibiotico.actualizar_antibiotico(kwargs['nombre_producto_despues'], kwargs['dosis'], kwargs['tipo_animal'], kwargs['valor_producto'])

            for i, antibiotico_lista in enumerate(self.lista_antibioticos):
                if antibiotico_lista == antibiotico:
                    self.lista_antibioticos[i].actualizar_antibiotico(kwargs['nombre_producto_despues'], kwargs['dosis'], kwargs['tipo_animal'], kwargs['valor_producto'])

    def eliminar(self, **kwargs):
        antibiotico = self.buscar(nombre_producto=kwargs['nombre_producto'])

        if antibiotico is not None:
            antibiotico.eliminar()
            self.lista_antibioticos.remove(antibiotico)

    def buscar(self, **kwargs):
        for antibiotico in self.lista_antibioticos:
            if antibiotico.obtener_nombre == kwargs['nombre_producto']:
                return antibiotico

    def relacion( self , ** kwargs ):
        pass