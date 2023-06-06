from abc import ABC , abstractmethod

class ICrud ( ABC ) :
    @abstractmethod
    def crear ( self , ** kwargs ):
        raise NotImplementedError

    @abstractmethod
    def relacion ( self , ** kwargs ) :
        raise NotImplementedError

    @abstractmethod
    def buscar( self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def eliminar(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def actualizar(self, **kwargs):
        raise NotImplementedError