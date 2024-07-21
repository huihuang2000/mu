from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
    QVBoxLayout,
    QTextEdit,
    QDialogButtonBox,
    QMessageBox,
    QTableWidgetItem,
    QHeaderView,
)
from PySide6.QtCore import QThread, Signal
from ui.Ui_untitled import Ui_Form
from modo.change_password import APPLE


class APPLE_UI(QWidget, Ui_Form):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.header = self.tableWidget.horizontalHeader()
        self.header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.import_2.clicked.connect(self.show_input_dialog)
        self.clean.clicked.connect(self.clear_table)
        self.start.clicked.connect(self.start_process)

        self.threads = []  # 用于存储所有线程

    def start_process(self):
        self.threads = []
        for row in range(self.tableWidget.rowCount()):
            username = self.tableWidget.item(row, 0).text()
            password = self.lineEdit.text()
            year_item = self.lineEdit_2.text()
            monthOfYear_item = self.lineEdit_3.text()
            dayOfMonth_item = self.lineEdit_4.text()

            Question_one = self.tableWidget.item(row, 2).text()
            Answer_one = self.tableWidget.item(row, 3).text()

            Question_two = self.tableWidget.item(row, 4).text()
            Answer_two = self.tableWidget.item(row, 5).text()

            Question_three = self.tableWidget.item(row, 6).text()
            Answer_three = self.tableWidget.item(row, 7).text()

            kwargs = {
                "username": username,
                "password": password,
                "year_item": year_item,
                "monthOfYear_item": monthOfYear_item,
                "dayOfMonth_item": dayOfMonth_item,
                "Question_one": Question_one,
                "Answer_one": Answer_one,
                "Question_two": Question_two,
                "Answer_two": Answer_two,
                "Question_three": Question_three,
                "Answer_three": Answer_three,
                "row": row,
            }
            thread = APPLEThread(self, **kwargs)
            thread.progress_signal.connect(self.update_progress)
            self.threads.append(thread)
            thread.start()

    def clear_table(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

    def show_input_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Import Accounts")

        layout = QVBoxLayout()

        # 创建一个多行文本编辑框
        account_input = QTextEdit()
        account_input.setPlaceholderText(
            "Paste your accounts here (one account per line)"
        )
        layout.addWidget(account_input)

        # 创建按钮
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # 连接按钮信号
        buttons.accepted.connect(
            lambda: self.add_accounts(account_input.toPlainText(), dialog)
        )
        buttons.rejected.connect(dialog.reject)

        layout.addWidget(buttons)

        dialog.setLayout(layout)

        if dialog.exec() == QDialog.Accepted:
            QMessageBox.information(self, "Success", "Accounts imported successfully!")

    def add_accounts(self, accounts_text, dialog):
        accounts = accounts_text.strip().split("\n")
        for account in accounts:
            if account:  # 确保不导入空行
                try:
                    # 假设账号和密码以及其他信息以 "----" 分隔
                    fields = account.split("----")
                    if len(fields) != 8:
                        raise ValueError("每行必须有8个字段")

                    username, password, field3, field4, field5, field6, field7, field8 = fields
                except ValueError as e:
                    QMessageBox.critical(dialog, "导入错误", str(e))
                    continue  # 终止导入

                # 添加新行到 tableWidget
                new_row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(new_row)

                # 创建并设置 QTableWidgetItem
                username_item = QTableWidgetItem(username.strip())
                password_item = QTableWidgetItem(password.strip())
                field3_item = QTableWidgetItem(field3.strip())
                field4_item = QTableWidgetItem(field4.strip())
                field5_item = QTableWidgetItem(field5.strip())
                field6_item = QTableWidgetItem(field6.strip())
                field7_item = QTableWidgetItem(field7.strip())
                field8_item = QTableWidgetItem(field8.strip())

                # 将 QTableWidgetItem 添加到 tableWidget
                self.tableWidget.setItem(new_row, 0, username_item)
                self.tableWidget.setItem(new_row, 1, password_item)
                self.tableWidget.setItem(new_row, 2, field3_item)
                self.tableWidget.setItem(new_row, 3, field4_item)
                self.tableWidget.setItem(new_row, 4, field5_item)
                self.tableWidget.setItem(new_row, 5, field6_item)
                self.tableWidget.setItem(new_row, 6, field7_item)
                self.tableWidget.setItem(new_row, 7, field8_item)

            dialog.accept() 


    def update_progress(self, message, row):
        # 更新指定行的第三列
        status_item = QTableWidgetItem(message)
        self.tableWidget.setItem(row, 2, status_item)


class APPLEThread(QThread):
    progress_signal = Signal(str, int)

    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.year_item = kwargs.get('year_item')
        self.monthOfYear_item = kwargs.get('monthOfYear_item')
        self.dayOfMonth_item = kwargs.get('dayOfMonth_item')
        self.question_one = kwargs.get('Question_one')
        self.answer_one = kwargs.get('Answer_one')
        self.question_two = kwargs.get('Question_two')
        self.answer_two = kwargs.get('Answer_two')
        self.question_three = kwargs.get('Question_three')
        self.answer_three = kwargs.get('Answer_three')
        self.row = kwargs.get('row')
        # print(self.username,self.password,self.year_item,self.monthOfYear_item,self.dayOfMonth_item,self.question_one,self.answer_one,self.question_two,self.answer_two,self.question_three,self.answer_three,self.row )
    def run(self):
        self.apple = APPLE(
            self.username,
            self.password,
            self.year_item,
            self.monthOfYear_item,
            self.dayOfMonth_item,
            self.question_one,
            self.answer_one,
            self.question_two,
            self.answer_two,
            self.question_three,
            self.answer_three,
             )

        result_get_sstt = self.apple.Get_sstt()
        self.emit_progress("获取SSTT", self.row)

        result_get_verification_code = self.apple.get_verification_code()
        self.emit_progress("获取验证码", self.row)

        result_identification_codes = self.apple.Identification_codes()
        self.emit_progress("识别验证码", self.row)

        result_submit_302_1 = self.apple.Submit_302_1()
        self.emit_progress("过302第一次", self.row)

        result_change_password = self.apple.Change_password()
        self.emit_progress("选择密码模式", self.row)

        result_convert = self.apple.Convert()
        self.emit_progress("转换", self.row)

        result_passed_302_2 = self.apple.Passed_302_2()
        self.emit_progress("过302第二次", self.row)

        result_show_brief_information = self.apple.Show_brief_information()
        self.emit_progress("过简介信息", self.row)

        result_passed_302_3 = self.apple.passed_302_3()
        self.emit_progress("过302第三次", self.row)

        result_detailed_year_month_day = self.apple.Detailed_year_month_day()
        self.emit_progress("过年月日", self.row)

        result_passed_302_4 = self.apple.passed_302_4()
        self.emit_progress("过302第四次", self.row)

        result_confidential_judgment_information = (
            self.apple.Confidential_judgment_information()
        )
        self.emit_progress("判断密保信息", self.row)

        result_password_detail = self.apple.Please_password_detail()
        self.emit_progress("过密码详细信息", self.row)

        result_passed_302_5 = self.apple.passed_302_5()
        self.emit_progress("过302第五次", self.row)

        result_check_password = self.apple.Check_password()
        self.emit_progress("校验密码", self.row)

        result_change_password_2 = self.apple.Change_password_2()
        self.emit_progress("更改密码", self.row)

        if "resetCompleted" in result_change_password_2:
            result = str(result_change_password_2["resetCompleted"])
            self.emit_progress(result, self.row)
        elif (
            "service_errors" in result_change_password_2
            and result_change_password_2["service_errors"]
        ):
            result = result_change_password_2["service_errors"][0]["message"]
            self.emit_progress(result, self.row)
        else:
            result = None
            self.emit_progress(result, self.row)

    def emit_progress(self, message, row):
        self.progress_signal.emit(message, row)


if __name__ == "__main__":
    app = QApplication([])
    window = APPLE_UI()
    window.show()
    app.exec()
