# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'antibioticos.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(734, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mostrar_antibiotico_recibido = QtWidgets.QTextBrowser(self.centralwidget)
        self.mostrar_antibiotico_recibido.setGeometry(QtCore.QRect(340, 260, 161, 21))
        self.mostrar_antibiotico_recibido.setObjectName("mostrar_antibiotico_recibido")
        self.ingreso_dosis = QtWidgets.QLabel(self.centralwidget)
        self.ingreso_dosis.setGeometry(QtCore.QRect(160, 110, 41, 20))
        self.ingreso_dosis.setObjectName("ingreso_dosis")
        self.btn_crear_antibiotico = QtWidgets.QPushButton(self.centralwidget)
        self.btn_crear_antibiotico.setGeometry(QtCore.QRect(220, 210, 101, 23))
        self.btn_crear_antibiotico.setObjectName("btn_crear_antibiotico")
        self.mostrar_dosis_buscar = QtWidgets.QLabel(self.centralwidget)
        self.mostrar_dosis_buscar.setGeometry(QtCore.QRect(510, 290, 131, 21))
        self.mostrar_dosis_buscar.setText("")
        self.mostrar_dosis_buscar.setObjectName("mostrar_dosis_buscar")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(370, 380, 20, 231))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.recibe_nombre_buscar = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_nombre_buscar.setGeometry(QtCore.QRect(190, 260, 113, 20))
        self.recibe_nombre_buscar.setText("")
        self.recibe_nombre_buscar.setObjectName("recibe_nombre_buscar")
        self.recibe_tipo_actualizar = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_tipo_actualizar.setGeometry(QtCore.QRect(210, 480, 141, 20))
        self.recibe_tipo_actualizar.setText("")
        self.recibe_tipo_actualizar.setObjectName("recibe_tipo_actualizar")
        self.mostrar_valor_buscar = QtWidgets.QLabel(self.centralwidget)
        self.mostrar_valor_buscar.setGeometry(QtCore.QRect(510, 350, 131, 21))
        self.mostrar_valor_buscar.setText("")
        self.mostrar_valor_buscar.setObjectName("mostrar_valor_buscar")
        self.mostrar_tipo_buscar = QtWidgets.QLabel(self.centralwidget)
        self.mostrar_tipo_buscar.setGeometry(QtCore.QRect(510, 320, 131, 21))
        self.mostrar_tipo_buscar.setText("")
        self.mostrar_tipo_buscar.setObjectName("mostrar_tipo_buscar")
        self.ingreso_nombre_eliminar = QtWidgets.QLabel(self.centralwidget)
        self.ingreso_nombre_eliminar.setGeometry(QtCore.QRect(430, 430, 51, 20))
        self.ingreso_nombre_eliminar.setObjectName("ingreso_nombre_eliminar")
        self.btn_eliminar_antibiotico = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eliminar_antibiotico.setGeometry(QtCore.QRect(440, 460, 111, 23))
        self.btn_eliminar_antibiotico.setObjectName("btn_eliminar_antibiotico")
        self.recibe_valor = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_valor.setGeometry(QtCore.QRect(200, 170, 141, 20))
        self.recibe_valor.setText("")
        self.recibe_valor.setObjectName("recibe_valor")
        self.recibe_nombre_antibiotico = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_nombre_antibiotico.setGeometry(QtCore.QRect(200, 80, 141, 20))
        self.recibe_nombre_antibiotico.setText("")
        self.recibe_nombre_antibiotico.setObjectName("recibe_nombre_antibiotico")
        self.recibe_tipo = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_tipo.setGeometry(QtCore.QRect(200, 140, 141, 20))
        self.recibe_tipo.setText("")
        self.recibe_tipo.setObjectName("recibe_tipo")
        self.ingreso_tipo_actualizar = QtWidgets.QLabel(self.centralwidget)
        self.ingreso_tipo_actualizar.setGeometry(QtCore.QRect(100, 480, 111, 20))
        self.ingreso_tipo_actualizar.setObjectName("ingreso_tipo_actualizar")
        self.ingreso_nombre_nuevo_actualizar = QtWidgets.QLabel(self.centralwidget)
        self.ingreso_nombre_nuevo_actualizar.setGeometry(QtCore.QRect(130, 420, 81, 20))
        self.ingreso_nombre_nuevo_actualizar.setObjectName("ingreso_nombre_nuevo_actualizar")
        self.ingreso_nombre_antibiotico = QtWidgets.QLabel(self.centralwidget)
        self.ingreso_nombre_antibiotico.setGeometry(QtCore.QRect(150, 80, 51, 20))
        self.ingreso_nombre_antibiotico.setObjectName("ingreso_nombre_antibiotico")
        self.recibe_nombre_eliminar = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_nombre_eliminar.setGeometry(QtCore.QRect(480, 430, 113, 20))
        self.recibe_nombre_eliminar.setObjectName("recibe_nombre_eliminar")
        self.ingreso_nombre_antes_actualizar = QtWidgets.QLabel(self.centralwidget)
        self.ingreso_nombre_antes_actualizar.setGeometry(QtCore.QRect(130, 390, 91, 20))
        self.ingreso_nombre_antes_actualizar.setObjectName("ingreso_nombre_antes_actualizar")
        self.ingreso_valor = QtWidgets.QLabel(self.centralwidget)
        self.ingreso_valor.setGeometry(QtCore.QRect(100, 170, 101, 20))
        self.ingreso_valor.setObjectName("ingreso_valor")
        self.btn_actualizar_antibiotico = QtWidgets.QPushButton(self.centralwidget)
        self.btn_actualizar_antibiotico.setGeometry(QtCore.QRect(230, 550, 111, 23))
        self.btn_actualizar_antibiotico.setObjectName("btn_actualizar_antibiotico")
        self.ingreso_tipo = QtWidgets.QLabel(self.centralwidget)
        self.ingreso_tipo.setGeometry(QtCore.QRect(120, 140, 81, 20))
        self.ingreso_tipo.setObjectName("ingreso_tipo")
        self.recibe_dosis_actualizar = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_dosis_actualizar.setGeometry(QtCore.QRect(210, 450, 141, 20))
        self.recibe_dosis_actualizar.setText("")
        self.recibe_dosis_actualizar.setObjectName("recibe_dosis_actualizar")
        self.mostrar_nombre_buscar = QtWidgets.QLabel(self.centralwidget)
        self.mostrar_nombre_buscar.setGeometry(QtCore.QRect(510, 260, 131, 21))
        self.mostrar_nombre_buscar.setText("")
        self.mostrar_nombre_buscar.setObjectName("mostrar_nombre_buscar")
        self.recibe_nombre_antes_actualizar = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_nombre_antes_actualizar.setGeometry(QtCore.QRect(210, 390, 141, 20))
        self.recibe_nombre_antes_actualizar.setText("")
        self.recibe_nombre_antes_actualizar.setObjectName("recibe_nombre_antes_actualizar")
        self.recibe_nombre_nuevo_actualizar = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_nombre_nuevo_actualizar.setGeometry(QtCore.QRect(210, 420, 141, 20))
        self.recibe_nombre_nuevo_actualizar.setText("")
        self.recibe_nombre_nuevo_actualizar.setObjectName("recibe_nombre_nuevo_actualizar")
        self.ingreso_valor_actualizar = QtWidgets.QLabel(self.centralwidget)
        self.ingreso_valor_actualizar.setGeometry(QtCore.QRect(80, 510, 131, 20))
        self.ingreso_valor_actualizar.setObjectName("ingreso_valor_actualizar")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 240, 761, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.ingreso_dosis_actualizar = QtWidgets.QLabel(self.centralwidget)
        self.ingreso_dosis_actualizar.setGeometry(QtCore.QRect(140, 450, 71, 20))
        self.ingreso_dosis_actualizar.setObjectName("ingreso_dosis_actualizar")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 370, 771, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.ingreso_nombre_buscar = QtWidgets.QLabel(self.centralwidget)
        self.ingreso_nombre_buscar.setGeometry(QtCore.QRect(140, 260, 51, 20))
        self.ingreso_nombre_buscar.setObjectName("ingreso_nombre_buscar")
        self.recibe_valor_actualizar = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_valor_actualizar.setGeometry(QtCore.QRect(210, 510, 141, 20))
        self.recibe_valor_actualizar.setText("")
        self.recibe_valor_actualizar.setObjectName("recibe_valor_actualizar")
        self.btn_buscar_antibiotico = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buscar_antibiotico.setGeometry(QtCore.QRect(220, 340, 101, 23))
        self.btn_buscar_antibiotico.setObjectName("btn_buscar_antibiotico")
        self.recibe_dosis = QtWidgets.QLineEdit(self.centralwidget)
        self.recibe_dosis.setGeometry(QtCore.QRect(200, 110, 141, 20))
        self.recibe_dosis.setText("")
        self.recibe_dosis.setObjectName("recibe_dosis")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(210, 10, 181, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mostrar_antibiotico_recibido.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Antibiotico encontrado:</p></body></html>"))
        self.ingreso_dosis.setText(_translate("MainWindow", "Dosis:"))
        self.btn_crear_antibiotico.setText(_translate("MainWindow", "Crear Antibiotico"))
        self.ingreso_nombre_eliminar.setText(_translate("MainWindow", "Nombre:"))
        self.btn_eliminar_antibiotico.setText(_translate("MainWindow", "Eliminar Antibiotico"))
        self.ingreso_tipo_actualizar.setText(_translate("MainWindow", "Tipo de animal nuevo: "))
        self.ingreso_nombre_nuevo_actualizar.setText(_translate("MainWindow", "Nombre nuevo:"))
        self.ingreso_nombre_antibiotico.setText(_translate("MainWindow", "Nombre:"))
        self.ingreso_nombre_antes_actualizar.setText(_translate("MainWindow", "Nombre antes:"))
        self.ingreso_valor.setText(_translate("MainWindow", "Valor del producto: "))
        self.btn_actualizar_antibiotico.setText(_translate("MainWindow", "Actualizar Antibiotico"))
        self.ingreso_tipo.setText(_translate("MainWindow", "Tipo de animal:"))
        self.ingreso_valor_actualizar.setText(_translate("MainWindow", "Valor del producto nuevo:"))
        self.ingreso_dosis_actualizar.setText(_translate("MainWindow", "Dosis nueva:"))
        self.ingreso_nombre_buscar.setText(_translate("MainWindow", "Nombre:"))
        self.btn_buscar_antibiotico.setText(_translate("MainWindow", "Buscar Antibiotico"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Antibioticos</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt; font-weight:600;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())