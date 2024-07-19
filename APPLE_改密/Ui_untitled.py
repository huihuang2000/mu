# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1372, 604)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.import_2 = QPushButton(Form)
        self.import_2.setObjectName(u"import_2")

        self.horizontalLayout.addWidget(self.import_2)

        self.start = QPushButton(Form)
        self.start.setObjectName(u"start")

        self.horizontalLayout.addWidget(self.start)

        self.clean = QPushButton(Form)
        self.clean.setObjectName(u"clean")

        self.horizontalLayout.addWidget(self.clean)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setReadOnly(False)

        self.horizontalLayout.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(Form)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(Form)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout.addWidget(self.lineEdit_7)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.import_2.setText(QCoreApplication.translate("Form", u"import", None))
        self.start.setText(QCoreApplication.translate("Form", u"start", None))
        self.clean.setText(QCoreApplication.translate("Form", u"clean up", None))
#if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u5e74", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u6708", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"\u65e5", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"\u5bc6\u4fdd\u4e00", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Form", u"\u5bc6\u4fdd\u4e8c", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("Form", u"\u5bc6\u4fdd\u4e09", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"username", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"password", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"status", None));
    # retranslateUi

