from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QTableWidget,
    QInputDialog, 
    QMessageBox,
    QTableWidgetItem
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Change_the_address")
        self.setGeometry(300, 300, 1200, 600)

        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        label_layout = QHBoxLayout()
        form_layout = QHBoxLayout()
        table_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addLayout(label_layout)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(table_layout)
        button_layout.setAlignment(Qt.AlignLeft)
        label_layout.setAlignment(Qt.AlignLeft)
        form_layout.setAlignment(Qt.AlignLeft)
        table_layout.setAlignment(Qt.AlignLeft)
        main_layout.setAlignment(Qt.AlignTop)

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setFixedWidth(1200)
        self.tableWidget.setFixedHeight(500)
        table_layout.addWidget(self.tableWidget)
        self.tableWidget.setHorizontalHeaderLabels(
            [
                "邮箱",
                "密码",
                "名",
                "姓",
                "公司名称",
                "街道地址",
                "公寓",
                "邮政编码",
                "城市",
                "州",
                "国家地区",
                "电话号码",
            ]
        )

        self.button1 = QPushButton("导入")
        self.button2 = QPushButton("修改")
        self.button3 = QPushButton("导出")
        self.button4 = QPushButton("清空")
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)
        button_layout.addWidget(self.button4)
        self.button1.clicked.connect(self.on_click_button1)
        self.button2.clicked.connect(self.on_click_button2)
        self.button3.clicked.connect(self.on_click_button3)
        self.button4.clicked.connect(self.on_click_button4)

        self.label1 = QLabel("名")
        self.label1.setFixedWidth(50)
        label_layout.addWidget(self.label1)
        self.line_edit1 = QLineEdit()
        self.line_edit1.setFixedWidth(50)
        form_layout.addWidget(self.line_edit1)

        self.label2 = QLabel("姓")
        self.label2.setFixedWidth(50)
        label_layout.addWidget(self.label2)
        self.line_edit2 = QLineEdit()
        self.line_edit2.setFixedWidth(50)
        form_layout.addWidget(self.line_edit2)

        self.label3 = QLabel("公司名称")
        self.label3.setFixedWidth(70)
        label_layout.addWidget(self.label3)
        self.line_edit3 = QLineEdit()
        self.line_edit3.setFixedWidth(70)
        form_layout.addWidget(self.line_edit3)

        self.label4 = QLabel("街道地址")
        self.label4.setFixedWidth(70)
        label_layout.addWidget(self.label4)
        self.line_edit4 = QLineEdit()
        self.line_edit4.setFixedWidth(70)
        form_layout.addWidget(self.line_edit4)

        self.label5 = QLabel("公寓")
        self.label5.setFixedWidth(70)
        label_layout.addWidget(self.label5)
        self.line_edit5 = QLineEdit()
        self.line_edit5.setFixedWidth(70)
        form_layout.addWidget(self.line_edit5)

        self.label6 = QLabel("邮政编码")
        self.label6.setFixedWidth(70)
        label_layout.addWidget(self.label6)
        self.line_edit6 = QLineEdit()
        self.line_edit6.setFixedWidth(70)
        form_layout.addWidget(self.line_edit6)

        self.label7 = QLabel("城市")
        self.label7.setFixedWidth(70)
        label_layout.addWidget(self.label7)
        self.line_edit7 = QLineEdit()
        self.line_edit7.setFixedWidth(70)
        form_layout.addWidget(self.line_edit7)

        self.label8 = QLabel("州")
        self.label8.setFixedWidth(70)
        label_layout.addWidget(self.label8)
        self.line_edit8 = QLineEdit()
        self.line_edit8.setFixedWidth(70)
        form_layout.addWidget(self.line_edit8)

        self.label9 = QLabel("国家地区")
        self.label9.setFixedWidth(70)
        label_layout.addWidget(self.label9)
        self.line_edit9 = QLineEdit()
        self.line_edit9.setFixedWidth(70)
        form_layout.addWidget(self.line_edit9)

        self.label10 = QLabel("电话号码")
        self.label10.setFixedWidth(80)
        label_layout.addWidget(self.label10)
        self.line_edit10 = QLineEdit()
        self.line_edit10.setFixedWidth(80)
        form_layout.addWidget(self.line_edit10)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def on_click_button1(self):
        text, ok = QInputDialog.getMultiLineText(self, "导入信息", "请输入邮箱和密码（每行一个，用空格分隔）:")
        if ok and text:
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line:
                    email, password = line.split(' ', 1)
                    self.add_email_and_password_to_table(email, password)
            QMessageBox.information(self, "导入成功", "所有邮箱和密码已成功导入")

    def add_email_and_password_to_table(self, email, password):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        email_item = QTableWidgetItem(email)
        password_item = QTableWidgetItem(password)
        self.tableWidget.setItem(row_position, 0, email_item)
        self.tableWidget.setItem(row_position, 1, password_item) 










    def on_click_button2(self):
        print('2')
    def on_click_button3(self):
        print('3')
    def on_click_button4(self):
        print('4')




def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":

    main()
