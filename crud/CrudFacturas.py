from model.Facturas import Facturas
from crud.CrudCliente import CrudCliente
from ui.facturas_UI import Ui_MainWindow
from crud import ICrud

class CrudFacturas(ICrud.ICrud):
    def crear(self, **kwargs):
        nueva_factura = Facturas()
        return nueva_factura

    def buscar(self, **kwargs):
        lista_facturas_cliente = kwargs['cliente'].lista_facturas_asociadas()

        for factura_cliente in lista_facturas_cliente:
            fecha_obtenida = str(factura_cliente.obtener_fecha)
            if fecha_obtenida == kwargs['fecha']:
                return factura_cliente

    def actualizar(self, **kwargs):
        kwargs['factura'].agregar_productos(producto=kwargs['producto'], cantidad=kwargs['cantidad'])

    def eliminar(self, **kwargs):
        factura = self.buscar(cliente=kwargs['cliente'], fecha=kwargs['fecha'])

        kwargs['cliente'].eliminar_factura(factura)

    def relacion(self, **kwargs):
        cliente = kwargs.get('cliente')
        factura = kwargs.get('factura')

        if cliente and factura:
            factura.recibir_datos_cliente(cliente)

