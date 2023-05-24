from model.Antibiotico import Antibioticos

class CrudAntibiotico():
    lista_antibioticos = []

    @classmethod
    def crear_antibiotico(cls, nombre_producto, dosis, tipo_animal, valor_producto):
        nuevo_antibiotico = Antibioticos(nombre_producto, dosis, tipo_animal, valor_producto)
        cls.lista_antibioticos.append(nuevo_antibiotico)
        return nuevo_antibiotico

    @classmethod
    def buscar_antibiotico(cls, nombre_producto):
        for antibiotico in cls.lista_antibioticos:
            if(antibiotico.obtener_nombre == nombre_producto):
                return antibiotico

    @classmethod
    def actualizar_antibiotico(cls, nombre_producto_antes, nombre_producto_despues, dosis, tipo_animal, valor_producto):
        antibiotico = cls.buscar_antibiotico(nombre_producto_antes)

        if antibiotico is not None:
            antibiotico.actualizar_antibiotico(nombre_producto_despues, dosis, tipo_animal, valor_producto)

            # Actualizar la lista:
            for i, antibiotico_lista in enumerate(cls.lista_antibioticos):
                if antibiotico_lista == antibiotico:
                    cls.lista_antibioticos[i].actualizar_antibiotico(nombre_producto_despues, dosis, tipo_animal, valor_producto)


    @classmethod
    def eliminar_antibiotico(cls, nombre_producto):
        antibiotico = cls.buscar_antibiotico(nombre_producto)

        if antibiotico is not None:
            antibiotico.eliminar()

            #Eliminar de la lista
            cls.lista_antibioticos.remove(antibiotico)