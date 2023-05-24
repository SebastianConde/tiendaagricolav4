from model.Facturas import Facturas
from ui.facturas_UI import Ui_MainWindow

class CrudFacturas():
    @classmethod
    def crear_Factura(cls, fecha):
        nueva_factura = Facturas(fecha)
        return nueva_factura

    @classmethod
    def buscar_factura(cls, cliente, fecha):
        lista_facturas_cliente = cliente.lista_facturas_asociadas()

        for factura_cliente in lista_facturas_cliente:
            fecha_obtenida = factura_cliente.obtener_fecha
            if fecha_obtenida == fecha:
                return factura_cliente

    @classmethod
    def actualizar_factura(cls, factura, producto, cantidad):
        factura.agregar_productos(producto, cantidad)

    @classmethod
    def eliminar_factura(cls, cliente, fecha):
        factura = cls.buscar_factura(cliente, fecha)

        cliente.eliminar_factura(factura)
