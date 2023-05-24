from PyQt5.QtWidgets import QDialog
from popup import Ui_Dialog_fecha

class Popup(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog_fecha()
        self.ui.setupUi(self)

    @staticmethod
    def open_popup():
        app = QDialog()
        popupWindow = Popup()
        popupWindow.exec_()

    def mensaje_popup(self, texto):
        self.ui.dialog_mensaje.setText(texto)


if __name__ == "__main__":
    app = QDialog()
    popupWindow = Popup()
    popupWindow.show()
    app.exec_()