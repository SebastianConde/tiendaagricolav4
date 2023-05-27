from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from crud.CrudFacturas import CrudFacturas
from ui.factura_buscada_UI import Ui_MainWindow

class Factura_buscadaWindow(QMainWindow):
    def __init__(self, factura, cliente):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.factura = factura
        self.cliente = cliente

        self.ui.recibir_nombre_cliente.setText(cliente.nombre_cliente)
        self.lista_productos_comprados = self.factura.lista_productos_comprados()
        self.ui.mostrar_nombre_productos.setText(self.mostrar_nombres())
        self.ui.total.setText(str(self.factura.obtener_total))

    @pyqtSlot()
    def mostrar_nombres(self):
        nombres_y_valores = ""
        for producto in self.lista_productos_comprados:
            nombres_y_valores += "Nombre: " + producto.obtener_nombre + ", valor: " + str(producto.obtener_valor) + "\n"

        return nombres_y_valores


if __name__ == "__main__":
    app = QApplication([])
    factura_buscadaWindow = Factura_buscadaWindow()
    factura_buscadaWindow.show()
    app.exec_()