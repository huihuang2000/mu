# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(370, 203)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.setObjectName("comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 4, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 1)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName("comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName("comboBox")

        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.label.setMaximumSize(QSize(100, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setKerning(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.label_2.setMaximumSize(QSize(100, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName("pushButton")

        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 2)

        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label.setText(QCoreApplication.translate("Form", "TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", "TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Form", "PushButton", None))

    # retranslateUi
