# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQTLabelerVer1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPen
from PyQt5.QtCore import Qt, QRectF, QEvent
from PyQt5.QtWidgets import QGraphicsScene, QFileDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1207, 840)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 790, 311, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prev_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.prev_button.setObjectName("prev_button")
        self.horizontalLayout.addWidget(self.prev_button)
        self.next_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout.addWidget(self.next_button)
        self.image_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.horizontalLayout.addWidget(self.image_label)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(10, 40, 971, 741))
        self.graphicsView.setObjectName("graphicsView")
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 971, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.directory_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.directory_label.setObjectName("directory_label")
        self.horizontalLayout_2.addWidget(self.directory_label)
        self.directory_tbrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.directory_tbrowser.setObjectName("directory_tbrowser")
        self.horizontalLayout_2.addWidget(self.directory_tbrowser)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(990, 0, 211, 781))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cd_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cd_button.setObjectName("cd_button")
        self.verticalLayout.addWidget(self.cd_button)
        self.finish_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.finish_button.setObjectName("finish_button")
        self.verticalLayout.addWidget(self.finish_button)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.bbox_tbrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.bbox_tbrowser.setObjectName("bbox_tbrowser")
        self.verticalLayout.addWidget(self.bbox_tbrowser)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(340, 790, 121, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.goto_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.goto_button.setObjectName("goto_button")
        self.horizontalLayout_3.addWidget(self.goto_button)
        self.index_ledit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.index_ledit.setObjectName("index_ledit")
        self.horizontalLayout_3.addWidget(self.index_ledit)

        # Events
        # set up drawing flag and box coordinates
        self.isDrawing = False
        self.startPos = None
        self.endPos = None

        # Connections
        self.cd_button.clicked.connect(self.load_image)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.prev_button.setText(_translate("Dialog", "<< Prev"))
        self.next_button.setText(_translate("Dialog", "Next >>"))
        self.directory_label.setText(_translate("Dialog", "Directory"))
        self.cd_button.setText(_translate("Dialog", "Change Directory"))
        self.finish_button.setText(_translate("Dialog", "Finish"))
        self.goto_button.setText(_translate("Dialog", "Go To"))

    def load_image(self):
        # Get the path to the image file using a file dialog
        self.filename, _ = QFileDialog.getOpenFileName(directory="C:/Users/LAPTOP/Desktop/Pics",
                                                       filter="Images (*.png *.xpm *.jpg *.bmp);;All Files (*)")
        if not self.filename:
            return
        # Load the image file as a pixmap
        pixmap = QPixmap(self.filename)
        if pixmap.isNull():
            return
        # Set the pixmap as the background for the QGraphicsView widget
        self.scene.clear()
        self.scene.addPixmap(pixmap)
        self.graphicsView.setSceneRect(QRectF(pixmap.rect()))
        self.graphicsView.fitInView(QRectF(pixmap.rect()), Qt.KeepAspectRatio)


    def drawBox(self):
        # remove previous box item if it exists
        if self.scene.items():
            self.scene.removeItem(self.scene.items()[-1])

        # create a new box item and add it to the scene
        pen = QPen(Qt.green)
        pen.setWidth(2)
        rect = QRectF(self.startPos, self.endPos)
        item = self.scene.addRect(rect, pen)
        item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)

class MyDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)
        self.graphicsView.viewport().installEventFilter(self)

    def eventFilter(self, source, event):
        print('here')
        if (event.type() == QtCore.QEvent.MouseButtonPress and
                event.button() == QtCore.Qt.LeftButton):
            self.startPos = event.pos()
            self.endPos = event.pos()
            self.isDrawing = True
            return True
        return super(MyDialog, self).eventFilter(source, event)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())

