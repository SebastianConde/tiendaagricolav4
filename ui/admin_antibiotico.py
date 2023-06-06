from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from ui.antibioticos_UI import Ui_MainWindow
from crud.CrudAntibiotico import CrudAntibiotico
from ui.admin_popup import Popup

class AntibioticosWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_crear_antibiotico.clicked.connect(self.crear_antibiotico)
        self.ui.btn_buscar_antibiotico.clicked.connect(self.buscar_antibiotico)
        self.ui.btn_actualizar_antibiotico.clicked.connect(self.actualizar_antibiotico)
        self.ui.btn_eliminar_antibiotico.clicked.connect(self.eliminar_antibiotico)

    @pyqtSlot()
    def crear_antibiotico(self):
        nombre = self.ui.recibe_nombre_antibiotico.text()
        dosis = self.ui.recibe_dosis.text()
        tipo = self.ui.recibe_tipo.text()
        valor = None
        if (self.ui.recibe_valor.text() != ''):
            valor_check = float(self.ui.recibe_valor.text())
            valor = valor_check

        if nombre and dosis and tipo and valor:
            crud_antibiotico = CrudAntibiotico()  # Crear una instancia de la clase
            antibiotico = crud_antibiotico.crear(nombre_producto=nombre, dosis=dosis, tipo_animal=tipo, valor_producto=valor)
            if antibiotico:
                self.ui.recibe_nombre_antibiotico.clear()
                self.ui.recibe_dosis.clear()
                self.ui.recibe_tipo.clear()
                self.ui.recibe_valor.clear()
        else:
            popup = Popup()
            popup.mensaje_popup("Error: campos requeridos para crear")
            popup.exec_()

    @pyqtSlot()
    def buscar_antibiotico(self):
        nombre = self.ui.recibe_nombre_buscar.text()

        if nombre:
            crud_antibiotico = CrudAntibiotico()  # Crear una instancia de la clase
            antibiotico = crud_antibiotico.buscar(nombre_producto=nombre)
            if antibiotico:
                self.ui.mostrar_nombre_buscar.setText(antibiotico.obtener_nombre)
                self.ui.mostrar_dosis_buscar.setText(antibiotico.obtener_dosis)
                self.ui.mostrar_tipo_buscar.setText(antibiotico.obtener_tipo)
                self.ui.mostrar_valor_buscar.setText(str(antibiotico.obtener_valor))
            else:
                self.ui.mostrar_nombre_buscar.setText("Antibiotico no encontrado")
                self.ui.mostrar_dosis_buscar.clear()
                self.ui.mostrar_tipo_buscar.clear()
                self.ui.mostrar_valor_buscar.clear()

    @pyqtSlot()
    def actualizar_antibiotico(self):
        nombre_antes = self.ui.recibe_nombre_antes_actualizar.text()
        nombre_nuevo = self.ui.recibe_nombre_nuevo_actualizar.text()
        dosis = self.ui.recibe_dosis_actualizar.text()
        tipo = self.ui.recibe_tipo_actualizar.text()
        valor = float(self.ui.recibe_valor_actualizar.text())

        if nombre_antes and nombre_nuevo and dosis and tipo and valor:
            crud_antibiotico = CrudAntibiotico()  # Crear una instancia de la clase
            antibiotico = crud_antibiotico.actualizar(
                nombre_producto_antes=nombre_antes,
                nombre_producto_despues=nombre_nuevo,
                dosis=dosis,
                tipo_animal=tipo,
                valor_producto=valor
            )
            self.ui.recibe_nombre_antes_actualizar.clear()
            self.ui.recibe_nombre_nuevo_actualizar.clear()
            self.ui.recibe_dosis_actualizar.clear()
            self.ui.recibe_tipo_actualizar.clear()
            self.ui.recibe_valor_actualizar.clear()

    @pyqtSlot()
    def eliminar_antibiotico(self):
        nombre = self.ui.recibe_nombre_eliminar.text()

        if nombre:
            crud_antibiotico = CrudAntibiotico()  # Crear una instancia de la clase
            crud_antibiotico.eliminar(nombre_producto=nombre)
            self.ui.recibe_nombre_eliminar.clear()


    def abrir_popup(self):
        Popup.open_popup()


if __name__ == "__main__":
    app = QApplication([])
    antibioticosWindow = AntibioticosWindow()
    antibioticosWindow.show()
    app.exec_()
