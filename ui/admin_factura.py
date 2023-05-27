from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from crud.CrudFacturas import CrudFacturas
from ui.facturas_UI import Ui_MainWindow
from crud.CrudControlFertilizantes import CrudControlFertilizantes
from crud.CrudControlPlagas import CrudControlPlagas
from crud.CrudAntibiotico import CrudAntibiotico
from ui.admin_popup import Popup
from model.Facturas import Facturas
from ui.admin_factura_buscada import Factura_buscadaWindow


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
        self.ui.btn_ver_factura_buscada.clicked.connect(self.open_factura)

    def abrir_popup(self):
        Popup.open_popup()

    @pyqtSlot()
    def open_factura(self):
        if(self.factura is not None):
            self.factura_buscadaWindow = Factura_buscadaWindow(self.factura, self.cliente)
            self.factura_buscadaWindow.show()

    @pyqtSlot()
    def crear_factura(self):
        factura = CrudFacturas.crear_Factura()
        if factura:
            self.factura = factura
            self.factura.recibir_datos_cliente(self.cliente)
            self.cliente.agregar_factura(self.factura)
            self.ui.mostrar_fecha.setText(str(self.factura.obtener_fecha))
            popup = Popup()
            popup.mensaje_popup("Factura creada exitosamente")
            popup.exec_()
        else:
            popup = Popup()
            popup.mensaje_popup("Error: No se pudo crear la factura")
            popup.exec_()

    @pyqtSlot()
    def buscar_factura(self):
        factura_buscada = CrudFacturas.buscar_factura(self.cliente, str(self.factura.obtener_fecha))
        if factura_buscada:
           self.ui.mostrar_total_buscar.setText("Factura encontrada")
        else:
           self.ui.mostrar_total_buscar.setText("Factura no encontrada")


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
