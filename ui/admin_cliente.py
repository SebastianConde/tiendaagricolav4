from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from ui.clientes_UI import Ui_btn_crear_cliente
from crud.CrudCliente import CrudCliente
from crud.CrudFacturas import CrudFacturas
from model.Facturas import Facturas
from ui.admin_factura import FacturasWindow
from ui.admin_popup import Popup

class ClientesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_btn_crear_cliente()
        self.ui.setupUi(self)
        self.cliente_activo = None

        self.ui.btn_crear_cliente_2.clicked.connect(self.crear_cliente)
        self.ui.btn_buscar_cliente.clicked.connect(self.buscar_cliente)
        self.ui.btn_actualizar_cliente.clicked.connect(self.actualizar_cliente)
        self.ui.btn_eliminar_cliente.clicked.connect(self.eliminar_cliente)
        self.ui.btn_asociar_factura.clicked.connect(self.open_facturas)


    @pyqtSlot()
    def crear_cliente(self):
        numero_cedula = self.ui.recibe_numero_cedula.text()
        nombre = self.ui.recibe_nombre_cliente.text()

        if numero_cedula and nombre:
            crud_cliente = CrudCliente()  # Crear una instancia de la clase
            cliente = crud_cliente.crear(nombre=nombre, numero_cedula=numero_cedula)
            if cliente:
                self.ui.recibe_numero_cedula.clear()
                self.ui.recibe_nombre_cliente.clear()
        else:
            popup = Popup()
            popup.mensaje_popup("Error: campos requeridos para crear")
            popup.exec_()

    @pyqtSlot()
    def buscar_cliente(self):
        numero_cedula = self.ui.recibe_cedula_buscar.text()

        if numero_cedula:
            crud_cliente = CrudCliente()
            cliente = crud_cliente.buscar(numero_cedula=numero_cedula)
            if cliente:
                self.ui.mostrar_cedula_cliente_buscar.setText(cliente.obtener_cedula)
                self.ui.mostrar_nombre_cliente_buscar.setText(cliente.nombre_cliente)
                self.cliente_activo = cliente
            else:
                self.ui.mostrar_cedula_cliente_buscar.setText("")
                self.ui.mostrar_nombre_cliente_buscar.setText("Cliente no encontrado")


    @pyqtSlot()
    def open_facturas(self):
        if (self.cliente_activo != None):
            self.facturasWindow = FacturasWindow(self.cliente_activo)
            self.facturasWindow.show()

    @pyqtSlot()
    def actualizar_cliente(self):
        numero_cedula = self.ui.recibe_cedula_actualizar.text()
        nombre_nuevo = self.ui.recibe_nombre_cliente_actualizar.text()

        if numero_cedula and nombre_nuevo:
            crud_cliente = CrudCliente()
            crud_cliente.actualizar(numero_cedula=numero_cedula, nombre_nuevo=nombre_nuevo)
            self.ui.recibe_cedula_actualizar.clear()
            self.ui.recibe_nombre_cliente_actualizar.clear()

    @pyqtSlot()
    def eliminar_cliente(self):
        numero_cedula = self.ui.recibe_cedula_eliminar.text()

        if numero_cedula:
            crud_cliente = CrudCliente()
            crud_cliente.eliminar(numero_cedula=numero_cedula)
            self.ui.recibe_cedula_eliminar.clear()


    def abrir_popup(self):
        Popup.open_popup()


if __name__ == "__main__":
    app = QApplication([])
    clientesWindow = ClientesWindow()
    clientesWindow.show()
    app.exec_()
