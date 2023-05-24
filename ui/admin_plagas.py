from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from ui.plagas_UI import Ui_MainWindow
from crud.CrudControlPlagas import CrudControlPlagas
from ui.admin_popup import Popup


class PlagaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_crear_plaga_2.clicked.connect(self.crear_plaga)
        self.ui.btn_buscar_plaga_2.clicked.connect(self.buscar_plaga)
        self.ui.btn_actualizar_plaga_2.clicked.connect(self.actualizar_plaga)
        self.ui.btn_eliminar_plaga_2.clicked.connect(self.eliminar_plaga)

    @pyqtSlot()
    def crear_plaga(self):
        registro_ICA = self.ui.recibe_registro_ica_2.text()
        nombre = self.ui.recibe_nombre_plaga_2.text()
        frecuencia = self.ui.recibe_frecuencia_2.text()
        valor = None
        if (self.ui.recibe_valor_2.text() != ''):
            valor_check = float(self.ui.recibe_valor_2.text())
            valor = valor_check

        periodo_carencia = self.ui.recibe_ultima_2.text()

        if registro_ICA and nombre and frecuencia and valor and periodo_carencia:
            plaga = CrudControlPlagas.crear_plaga(registro_ICA, nombre, frecuencia, valor, periodo_carencia)
            if plaga:
                self.ui.recibe_registro_ica_2.clear()
                self.ui.recibe_nombre_plaga_2.clear()
                self.ui.recibe_frecuencia_2.clear()
                self.ui.recibe_valor_2.clear()
                self.ui.recibe_ultima_2.clear()
        else:
            popup = Popup()
            popup.mensaje_popup("Error: campos requeridos para crear")
            popup.exec_()

    @pyqtSlot()
    def buscar_plaga(self):
        registro_ICA = self.ui.recibe_registro_ica_buscar_2.text()

        if registro_ICA:
            plaga = CrudControlPlagas.buscar_plaga(registro_ICA)
            if plaga:
                self.ui.mostrar_registro_ica_buscar.setText(plaga.obtener_registro_ICA)
                self.ui.mostrar_nombre_buscar.setText(plaga.obtener_nombre)
                self.ui.mostrar_frecuencia_buscar.setText(plaga.obtener_frecuencia)
                self.ui.mostrar_valor_buscar.setText(str(plaga.obtener_valor))
                self.ui.mostrar_periodo_buscar.setText(plaga.obtener_periodo)
            else:
                self.ui.mostrar_registro_ica_buscar.setText("Control de plagas no encontrado")
                self.ui.mostrar_nombre_buscar.clear()
                self.ui.mostrar_frecuencia_buscar.clear()
                self.ui.mostrar_valor_buscar.clear()
                self.ui.mostrar_periodo_buscar.clear()

    @pyqtSlot()
    def actualizar_plaga(self):
        registro_ICA_antes = self.ui.recibe_registro_ica_antes_actualizar.text()
        registro_ICA_nuevo = self.ui.recibe_registro_ica_actualizar_2.text()
        nombre_nuevo = self.ui.recibe_nombre_actualizar_2.text()
        frecuencia_nueva = self.ui.recibe_frecuencia_actualizar_2.text()
        valor_nuevo = float(self.ui.recibe_valor_actualizar_2.text())
        periodo_nuevo = self.ui.recibe_periodo_actualizar_2.text()

        if registro_ICA_antes and registro_ICA_nuevo and nombre_nuevo and frecuencia_nueva and valor_nuevo and periodo_nuevo:
            CrudControlPlagas.actualizar_plaga(registro_ICA_antes, registro_ICA_nuevo, nombre_nuevo, frecuencia_nueva, valor_nuevo, periodo_nuevo)
            self.ui.recibe_registro_ica_antes_actualizar.clear()
            self.ui.recibe_registro_ica_actualizar_2.clear()
            self.ui.recibe_nombre_actualizar_2.clear()
            self.ui.recibe_frecuencia_actualizar_2.clear()
            self.ui.recibe_valor_actualizar_2.clear()
            self.ui.recibe_periodo_actualizar_2.clear()

    @pyqtSlot()
    def eliminar_plaga(self):
        registro_ICA = self.ui.recibe_registro_ica_eliminar_2.text()

        if registro_ICA:
            CrudControlPlagas.eliminar_plaga(registro_ICA)
            self.ui.recibe_registro_ica_eliminar_2.clear()


    def abrir_popup(self):
        Popup.open_popup()


if __name__ == "__main__":
    app = QApplication([])
    plagaWindow = PlagaWindow()
    plagaWindow.show()
    app.exec_()
