import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.main import Ui_MainWindow
from ui.admin_cliente import ClientesWindow
from ui.admin_fertilizante import FertilizantesWindow
from ui.admin_plagas import PlagaWindow
from ui.admin_antibiotico import AntibioticosWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_clientes.clicked.connect(self.open_clientes)
        self.ui.btn_fertilizantes.clicked.connect(self.open_fertilizantes)
        self.ui.btn_control_plagas.clicked.connect(self.open_control_plagas)
        self.ui.btn_antibioticos.clicked.connect(self.open_antibioticos)

    def open_clientes(self):
        self.clientesWindow = ClientesWindow()
        self.clientesWindow.show()

    def open_fertilizantes(self):
        self.fertilizantesWindow = FertilizantesWindow()
        self.fertilizantesWindow.show()

    def open_control_plagas(self):
        self.plagaWindow = PlagaWindow()
        self.plagaWindow.show()

    def open_antibioticos(self):
        self.antibioticosWindow = AntibioticosWindow()
        self.antibioticosWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
