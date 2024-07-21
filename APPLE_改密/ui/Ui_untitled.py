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
    QHBoxLayout,
    QHeaderView,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(1370, 582)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(10, 10))
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.import_2 = QPushButton(self.tab)
        self.import_2.setObjectName("import_2")

        self.horizontalLayout.addWidget(self.import_2)

        self.start = QPushButton(self.tab)
        self.start.setObjectName("start")

        self.horizontalLayout.addWidget(self.start)

        self.clean = QPushButton(self.tab)
        self.clean.setObjectName("clean")

        self.horizontalLayout.addWidget(self.clean)

        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.horizontalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.tab)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.horizontalLayout.addWidget(self.lineEdit_4)

        self.lineEdit_5 = QLineEdit(self.tab)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setReadOnly(False)

        self.horizontalLayout.addWidget(self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.tab)
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.horizontalLayout.addWidget(self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.tab)
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.horizontalLayout.addWidget(self.lineEdit_7)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(self.tab)
        if self.tableWidget.columnCount() < 3:
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName("tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.import_2.setText(QCoreApplication.translate("Form", "import", None))
        self.start.setText(QCoreApplication.translate("Form", "start", None))
        self.clean.setText(QCoreApplication.translate("Form", "clean up", None))
        # if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.lineEdit.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("Form", "\u5bc6\u7801", None)
        )
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("Form", "\u5e74", None)
        )
        self.lineEdit_3.setPlaceholderText(
            QCoreApplication.translate("Form", "\u6708", None)
        )
        self.lineEdit_4.setPlaceholderText(
            QCoreApplication.translate("Form", "\u65e5", None)
        )
        self.lineEdit_5.setPlaceholderText(
            QCoreApplication.translate("Form", "\u5bc6\u4fdd\u4e00", None)
        )
        self.lineEdit_6.setPlaceholderText(
            QCoreApplication.translate("Form", "\u5bc6\u4fdd\u4e8c", None)
        )
        self.lineEdit_7.setPlaceholderText(
            QCoreApplication.translate("Form", "\u5bc6\u4fdd\u4e09", None)
        )
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("Form", "username", None)
        )
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("Form", "password", None)
        )
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", "status", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("Form", "\u4e3b\u9875", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("Form", "\u914d\u7f6e", None),
        )

    # retranslateUi
