from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from crud.CrudFacturas import CrudFacturas
from ui.facturas_UI import Ui_MainWindow
from crud.CrudControlFertilizantes import CrudControlFertilizantes
from crud.CrudControlPlagas import CrudControlPlagas
from crud.CrudAntibiotico import CrudAntibiotico
from ui.admin_popup import Popup

from model.Facturas import Facturas


class FacturasWindow(QMainWindow):
    def __init__(self, cliente):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cliente = cliente
        self.factura = None

        self.lista_fertilizantes = CrudControlFertilizantes.lista_fertilizantes
        self.lista_plagas = CrudControlPlagas.lista_plagas
        self.lista_antibioticos = CrudAntibiotico.lista_antibioticos

        self.ui.mostrar_cliente_asociado.setText(cliente.nombre_cliente)
        self.ui.btn_crear_factura.clicked.connect(self.crear_factura)
        self.ui.btn_buscar_factura.clicked.connect(self.buscar_factura)
        self.ui.btn_actualizar_factura.clicked.connect(self.actualizar_factura)
        self.ui.btn_eliminar_factura.clicked.connect(self.eliminar_factura)

    def abrir_popup(self):
        Popup.open_popup()

    @pyqtSlot()
    def crear_factura(self):
        fecha = self.ui.recibir_fecha.text()

        if fecha:
            factura = CrudFacturas.crear_Factura(fecha)
            self.factura = factura
            if factura:
                self.ui.recibir_fecha.clear()
        else:
            popup = Popup()
            popup.mensaje_popup("Error: campos requeridos para crear")
            popup.exec_()

    @pyqtSlot()
    def buscar_factura(self):
        fecha = self.ui.recibir_fecha_buscar.text()
        self.ui.mostrar_cliente_asociado.setText(fecha)

        if fecha:
            factura_buscada = CrudFacturas.buscar_factura(self.cliente, fecha)
            self.ui.mostrar_total_buscar.setText(str(factura_buscada.obtener_total))

                #self.ui.mostrar_total_buscar.setText("Factura no encontrada")


    @pyqtSlot()
    def actualizar_factura(self):
        nombre_producto = self.ui.recibir_nombre_actualizar.text()
        cantidad = int(self.ui.recibir_cantidad_actualizar.text())

        producto = self.buscar_producto(nombre_producto)

        if nombre_producto and cantidad:
            CrudFacturas.actualizar_factura(self.factura, producto, cantidad)
            self.ui.recibir_nombre_actualizar.clear()
            self.ui.recibir_cantidad_actualizar.clear()
            popup = Popup()
            popup.mensaje_popup("¡Producto agregado con exito!")
            popup.exec_()


    @pyqtSlot()
    def buscar_producto(self, nombre_producto):
        # Buscar en la primera lista
        for producto in self.lista_plagas:
            if producto.obtener_nombre == nombre_producto:
                # Acción a realizar cuando se encuentra el producto
                return producto

        # Buscar en la segunda lista
        for producto in self.lista_fertilizantes:
            if producto.obtener_nombre == nombre_producto:
                # Acción a realizar cuando se encuentra el producto
                return producto

        # Buscar en la tercera lista
        for producto in self.lista_antibioticos:
            if producto.obtener_nombre == nombre_producto:
                # Acción a realizar cuando se encuentra el producto
                return producto

        # Acción a realizar cuando no se encuentra el producto
        return None

    @pyqtSlot()
    def eliminar_factura(self):
        fecha = self.ui.recibir_fecha_eliminar.text()

        if fecha:
            CrudFacturas.eliminar_factura(self.cliente, fecha)
            self.ui.recibir_fecha_eliminar.clear()


if __name__ == "__main__":
    app = QApplication([])
    facturasWindow = FacturasWindow()
    facturasWindow.show()
    app.exec_()
