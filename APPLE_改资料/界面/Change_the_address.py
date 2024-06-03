import pandas as pd
import asyncio
from datetime import datetime
import os
from pathlib import Path
from one import APPLE
from concurrent.futures import ThreadPoolExecutor
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from PySide6.QtCore import Qt, Slot, QRunnable, QThreadPool, Signal, QObject
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
    QTableWidgetItem,
    QMessageBox,
)


class Asynctask(QRunnable):
    def __init__(self, row, email, callback, **address_details):
        super().__init__()
        self.row = row
        self.email = email
        self.callback = callback
        self.address_details = address_details

    def run(self):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self.run_on_executor())
        loop.close()

    async def run_on_executor(self):
        loop = asyncio.get_running_loop()
        executor = ThreadPoolExecutor()
        apple = await loop.run_in_executor(executor, self.run_sync_method)
        self.callback(self.row, self.email, apple)

    def run_sync_method(self):
        apple = APPLE(**self.address_details)
        apple.t0()
        if hasattr(apple, 'stast') and apple.stast == "账号异常，无法获取必要的信息。":
            result = {"firstName": "账号异常"}
        else:
            result = {
                "firstName": apple.firstName,
                "lastName": apple.lastName,
                "companyName": apple.companyName,
                "street": apple.street,
                "street2": apple.street2,
                "postalCode": apple.postalCode,
                "city": apple.city,
                "state": apple.state,
                "countryCode": apple.countryCode,
                "fullDaytimePhone": apple.fullDaytimePhone,
            }
        return result


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Change_the_address")
        self.setGeometry(300, 300, 1200, 600)

        self.thread_pool = QThreadPool()

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
        text, ok = QInputDialog.getMultiLineText(
            self, "导入信息", "请输入邮箱和密码(每行一个，用空格分隔)"
        )
        if ok and text:
            lines = text.split("\n")
            for line in lines:
                line = line.strip()
                if line:
                    email, password, *rest = line.split(maxsplit=1)
                    if rest:
                        print(f"警告：格式错误 - 多余的空格被忽略。行内容：{line}")
                    self.add_email_and_password_to_table(email, password)

    def add_email_and_password_to_table(self, email, password):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        email_item = QTableWidgetItem(email)
        password_item = QTableWidgetItem(password)
        self.tableWidget.setItem(row_position, 0, email_item)
        self.tableWidget.setItem(row_position, 1, password_item)

    def on_click_button2(self):
        for row in range(self.tableWidget.rowCount()):
            if self.tableWidget.item(row, 0) and self.tableWidget.item(row, 1):
                email = self.tableWidget.item(row, 0).text()
                password = self.tableWidget.item(row, 1).text()
                # address_details = {
                #     "name":email,
                #     "pwd":password,
                #     "fullDaytimePhone": self.line_edit1.text(),
                #     "street2": self.line_edit2.text(),
                #     "lastName": self.line_edit3.text(),
                #     "firstName": self.line_edit4.text(),
                #     "companyName": self.line_edit5.text(),
                #     "street": self.line_edit6.text(),
                #     "city": self.line_edit7.text(),
                #     "state": self.line_edit8.text(),
                #     "postalCode": self.line_edit9.text(),
                #     "countryCode": self.line_edit10.text(),
                # }
                params = {
                    "name": email,
                    "pwd": password,
                    "fullDaytimePhone": "111111-2222",
                    "street2": "212231312",
                    "lastName": "lllll3333",
                    "firstName": "hhhjjj11166666",
                    "companyName": "122332",
                    "street": "777776667777",
                    "city": "Albany",
                    "state": "CH",
                    "postalCode": "11111-1111",
                    "countryCode": "CH",
                }
                params = {**params}
                task = Asynctask(row, email, self.update_table_item, **params)
                self.thread_pool.start(task)

    def update_table_item(self, row, email, result):
        if result.get('firstName') == "账号异常":
            self.tableWidget.setItem(row, 2, QTableWidgetItem(result["firstName"]))
        else:
            if self.tableWidget.item(row, 0).text() == email:
                self.tableWidget.setItem(row, 2, QTableWidgetItem(result.get('firstName', '')))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(result.get('lastName', '')))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(result.get('companyName', '')))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(result.get('street', '')))
                self.tableWidget.setItem(row, 6, QTableWidgetItem(result.get('street2', '')))
                self.tableWidget.setItem(row, 7, QTableWidgetItem(result.get('postalCode', '')))
                self.tableWidget.setItem(row, 8, QTableWidgetItem(result.get('city', '')))
                self.tableWidget.setItem(row, 9, QTableWidgetItem(result.get('state', '')))
                self.tableWidget.setItem(row, 10, QTableWidgetItem(result.get('countryCode', '')))
                self.tableWidget.setItem(row, 11, QTableWidgetItem(result.get('fullDaytimePhone', '')))


        
    def on_click_button3(self):
        desktop_path = str(Path.home() / "Desktop")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"地址_{timestamp}.xlsx"
        file_path = os.path.join(desktop_path, filename)
        df = self.tableWidgetToDataFrame(self.tableWidget)
        df.to_excel(file_path, index=False, engine="openpyxl")
        wb = load_workbook(file_path)
        ws = wb.active
        for col in range(1, ws.max_column + 1):
            max_length = 0
            for row in range(1, ws.max_row + 1):
                cell = ws.cell(row=row, column=col)
                if cell.value is not None:
                    max_length = max(max_length, len(str(cell.value)))
            ws.column_dimensions[get_column_letter(col)].width = max_length + 5
        wb.save(file_path)
        wb.close()
        QMessageBox.information(self, "导出完成", f"数据已导出到 {file_path}")

    def tableWidgetToDataFrame(self, tableWidget):
        num_rows = tableWidget.rowCount()
        num_cols = tableWidget.columnCount()
        columns = [tableWidget.horizontalHeaderItem(i).text() for i in range(num_cols)]
        df = pd.DataFrame(columns=columns)
        for i in range(num_rows):
            row_data = [
                tableWidget.item(i, j).text() if tableWidget.item(i, j) else ""
                for j in range(num_cols)
            ]
            df.loc[i] = row_data
        return df

    def on_click_button4(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
