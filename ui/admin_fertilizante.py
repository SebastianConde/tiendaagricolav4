from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from ui.fertilizantes_UI import Ui_MainWindow
from crud.CrudControlFertilizantes import CrudControlFertilizantes
from ui.admin_popup import Popup


class FertilizantesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_crear_fertilizante_2.clicked.connect(self.crear_fertilizante)
        self.ui.btn_buscar_fertilizante_2.clicked.connect(self.buscar_fertilizante)
        self.ui.btn_actualizar_fertilizante_2.clicked.connect(self.actualizar_fertilizante)
        self.ui.btn_eliminar_fertilizante_2.clicked.connect(self.eliminar_fertilizante)

    @pyqtSlot()
    def crear_fertilizante(self):
        registro_ICA = self.ui.recibe_registro_ica_2.text()
        nombre = self.ui.recibe_nombre_fertilizante_2.text()
        frecuencia = self.ui.recibe_frecuencia_2.text()
        valor = None
        if(self.ui.recibe_valor_2.text() != ''):
          valor_check = float(self.ui.recibe_valor_2.text())
          valor = valor_check


        ultima_aplicacion = self.ui.recibe_ultima_2.text()

        if registro_ICA and nombre and frecuencia and valor and ultima_aplicacion:
            crud_fertilizante = CrudControlFertilizantes()  # Crear una instancia de la clase
            fertilizante = crud_fertilizante.crear(registro_ICA=registro_ICA, nombre_producto=nombre, frecuencia_aplicacion=frecuencia, valor_producto=valor, ultima_aplicacion=ultima_aplicacion)
            if fertilizante:
                self.ui.recibe_registro_ica_2.clear()
                self.ui.recibe_nombre_fertilizante_2.clear()
                self.ui.recibe_frecuencia_2.clear()
                self.ui.recibe_valor_2.clear()
                self.ui.recibe_ultima_2.clear()
        else:
            popup = Popup()
            popup.mensaje_popup("Error: campos requeridos para crear")
            popup.exec_()

    @pyqtSlot()
    def buscar_fertilizante(self):
        registro_ICA = self.ui.recibe_registro_ica_buscar_2.text()

        if registro_ICA:
            crud_fertilizante = CrudControlFertilizantes()
            fertilizante = crud_fertilizante.buscar(registro_ICA=registro_ICA)
            if fertilizante:
                self.ui.mostrar_registro_ica_buscar.setText(fertilizante.obtener_registro_ICA)
                self.ui.mostrar_nombre_buscar.setText(fertilizante.obtener_nombre)
                self.ui.mostrar_frecuencia_buscar.setText(fertilizante.obtener_frecuencia)
                self.ui.mostrar_valor_buscar.setText(str(fertilizante.obtener_valor))
                self.ui.mostrar_ultima_buscar.setText(fertilizante.obtener_ultima)
            else:
                self.ui.mostrar_registro_ica_buscar.setText("Fertilizante no encontrado")
                self.ui.mostrar_nombre_buscar.clear()
                self.ui.mostrar_frecuencia_buscar.clear()
                self.ui.mostrar_valor_buscar.clear()
                self.ui.mostrar_ultima_buscar.clear()

    @pyqtSlot()
    def actualizar_fertilizante(self):
        registro_ICA_antes = self.ui.recibe_registro_ica_antes_actualizar.text()
        registro_ICA_nuevo = self.ui.recibe_registro_ica_actualizar_2.text()
        nombre_nuevo = self.ui.recibe_nombre_actualizar_2.text()
        frecuencia_nueva = self.ui.recibe_frecuencia_actualizar_2.text()
        valor_nuevo = float(self.ui.recibe_valor_actualizar_2.text())
        ultima_nuevo = self.ui.recibe_ultima_actualizar_2.text()

        if registro_ICA_antes and registro_ICA_nuevo and nombre_nuevo and frecuencia_nueva and valor_nuevo and ultima_nuevo:
            crud_fertilizante = CrudControlFertilizantes()
            crud_fertilizante.actualizar(registro_ICA_antes=registro_ICA_antes, registro_ICA_despues=registro_ICA_nuevo, nombre_producto_despues=nombre_nuevo, frecuencia_aplicacion_despues=frecuencia_nueva, valor_producto_despues=valor_nuevo, ultima_aplicacion_despues=ultima_nuevo)
            self.ui.recibe_registro_ica_antes_actualizar.clear()
            self.ui.recibe_registro_ica_actualizar_2.clear()
            self.ui.recibe_nombre_actualizar_2.clear()
            self.ui.recibe_frecuencia_actualizar_2.clear()
            self.ui.recibe_valor_actualizar_2.clear()
            self.ui.recibe_ultima_actualizar_2.clear()

    @pyqtSlot()
    def eliminar_fertilizante(self):
        registro_ICA = self.ui.recibe_registro_ica_eliminar_2.text()

        if registro_ICA:
            crud_fertilizante = CrudControlFertilizantes()
            crud_fertilizante.eliminar(registro_ICA=registro_ICA)
            self.ui.recibe_registro_ica_eliminar_2.clear()

    def abrir_popup(self):
        Popup.open_popup()


if __name__ == "__main__":
    app = QApplication([])
    fertilizantesWindow = FertilizantesWindow()
    fertilizantesWindow.show()
    app.exec_()
