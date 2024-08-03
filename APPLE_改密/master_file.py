from ast import Import
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
from modo.Security_Code import APPLE_2
from modo.Remove_copy import APPLE_Remove


class APPLE_UI(QWidget, Ui_Form):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.header = self.tableWidget.horizontalHeader()
        self.header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.import_2.clicked.connect(self.show_input_dialog)
        self.clean.clicked.connect(self.clear_table)
        self.comboBox.currentIndexChanged.connect(self.on_comboBox_changed)
        self.start.clicked.connect(self.start_process)

        self.threads = []

    def on_comboBox_changed(self):

        current = self.comboBox.currentText()
        if current == "改密码":
            self.start.clicked.disconnect()
            self.start.clicked.connect(self.start_process)
        elif current == "改密保":
            self.start.clicked.disconnect()
            self.start.clicked.connect(self.start_process_2)
        elif current == "删设备":
            self.start.clicked.disconnect()
            self.start.clicked.connect(self.start_process_3)
        else:
            QMessageBox.information(self, "提示", "你选择了其他选项")

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

    def start_process_2(self):
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

            pass_1 = self.lineEdit_5.text()
            pass_2 = self.lineEdit_6.text()
            pass_3 = self.lineEdit_7.text()

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
                "pass_1": pass_1,
                "pass_2": pass_2,
                "pass_3": pass_3,
                "row": row,
            }
            thread = APPLEThread_2(self, **kwargs)
            thread.progress_signal.connect(self.update_progress)
            self.threads.append(thread)
            thread.start()

    def start_process_3(self):
        self.threads = []
        for row in range(self.tableWidget.rowCount()):
            username = self.tableWidget.item(row, 0).text()
            password = self.tableWidget.item(row, 1).text()

            Question_one = self.tableWidget.item(row, 2).text()
            Answer_one = self.tableWidget.item(row, 3).text()

            Question_two = self.tableWidget.item(row, 4).text()
            Answer_two = self.tableWidget.item(row, 5).text()

            Question_three = self.tableWidget.item(row, 6).text()
            Answer_three = self.tableWidget.item(row, 7).text()

            kwargs = {
                "username": username,
                "password": password,
                "Question_one": Question_one,
                "Answer_one": Answer_one,
                "Question_two": Question_two,
                "Answer_two": Answer_two,
                "Question_three": Question_three,
                "Answer_three": Answer_three,
                "row": row,
            }
            thread = APPLEThread_3(self, **kwargs)
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

                    (
                        username,
                        password,
                        field3,
                        field4,
                        field5,
                        field6,
                        field7,
                        field8,
                    ) = fields
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
        status_item = QTableWidgetItem(message)
        self.tableWidget.setItem(row, 8, status_item)


class APPLEThread(QThread):
    progress_signal = Signal(str, int)

    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        self.kwargs = {
            "username": kwargs.get("username"),
            "password": kwargs.get("password"),
            "year_item": kwargs.get("year_item"),
            "monthOfYear_item": kwargs.get("monthOfYear_item"),
            "dayOfMonth_item": kwargs.get("dayOfMonth_item"),
            "Question_one": kwargs.get("Question_one"),
            "Answer_one": kwargs.get("Answer_one"),
            "Question_two": kwargs.get("Question_two"),
            "Answer_two": kwargs.get("Answer_two"),
            "Question_three": kwargs.get("Question_three"),
            "Answer_three": kwargs.get("Answer_three"),
        }

        self.row = kwargs.get("row")

    def run(self):
        self.emit_progress("开始", self.row)
        self.apple = APPLE(**self.kwargs)

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


class APPLEThread_2(QThread):
    progress_signal = Signal(str, int)

    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        self.kwargs = {
            "username": kwargs.get("username"),
            "password": kwargs.get("password"),
            "year_item": kwargs.get("year_item"),
            "monthOfYear_item": kwargs.get("monthOfYear_item"),
            "dayOfMonth_item": kwargs.get("dayOfMonth_item"),
            "Question_one": kwargs.get("Question_one"),
            "Answer_one": kwargs.get("Answer_one"),
            "Question_two": kwargs.get("Question_two"),
            "Answer_two": kwargs.get("Answer_two"),
            "Question_three": kwargs.get("Question_three"),
            "Answer_three": kwargs.get("Answer_three"),
            "pass_1": kwargs.get("pass_1"),
            "pass_2": kwargs.get("pass_2"),
            "pass_3": kwargs.get("pass_3"),
        }
        self.row = kwargs.get("row")

    def run(self):
        self.apple = APPLE_2(**self.kwargs)

        result_get_sstt = self.apple.Get_sstt()
        self.emit_progress("获取SSTT", self.row)

        result_get_verification_code = self.apple.get_verification_code()
        self.emit_progress("获取验证码", self.row)

        result_identification_codes = self.apple.Identification_codes()
        self.emit_progress("识别验证码", self.row)

        result_submit_302_1 = self.apple.Submit_302_1()
        self.emit_progress("带验证码过302第一次", self.row)

        result_change_password = self.apple.Change_password()
        self.emit_progress("选择模式", self.row)

        result_convert = self.apple.Convert()
        self.emit_progress("转换", self.row)

        result_passed_302_2 = self.apple.Passed_302_2()
        self.emit_progress("选择密保模式", self.row)

        result_show_brief_information = self.apple.Show_brief_information()
        self.emit_progress("过简介信息", self.row)

        result_passed_302_3 = self.apple.passed_302_3()
        self.emit_progress("带密码过302第三次", self.row)

        result_passed_302_4 = self.apple.passed_302_4()
        self.emit_progress("过302第四次", self.row)

        result_confidential_judgment_information = (
            self.apple.three_factor_authentication()
        )
        self.emit_progress("判断原生密保信息", self.row)

        result_passed_302_5 = self.apple.passed_302_5()
        self.emit_progress("三选一过密保校验", self.row)

        result_all_security_information = self.apple.all_security_information()
        self.emit_progress("出所有密保信息", self.row)

        result_change_security_settings = self.apple.change_security_settings()
        self.emit_progress("更改密保", self.row)

        # if "resetCompleted" in result_change_security_settings:
        #     result = str(result_change_security_settings["resetCompleted"])
        #     self.emit_progress(result, self.row)
        # elif (
        #     "service_errors" in result_change_security_settings
        #     and result_change_security_settings["service_errors"]
        # ):
        #     result = result_change_security_settings["service_errors"][0]["message"]
        #     self.emit_progress(result, self.row)
        # else:
        #     result = None
        #     self.emit_progress(result, self.row)

    def emit_progress(self, message, row):
        self.progress_signal.emit(message, row)


class APPLEThread_3(QThread):
    progress_signal = Signal(str, int)

    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        self.kwargs = {
            "username": kwargs.get("username"),
            "password": kwargs.get("password"),
            "Question_one": kwargs.get("Question_one"),
            "Answer_one": kwargs.get("Answer_one"),
            "Question_two": kwargs.get("Question_two"),
            "Answer_two": kwargs.get("Answer_two"),
            "Question_three": kwargs.get("Question_three"),
            "Answer_three": kwargs.get("Answer_three"),
        }

        self.row = kwargs.get("row")

    def run(self):
        self.emit_progress("开始", self.row)
        self.apple_remove = APPLE_Remove(**self.kwargs)

        result_one = self.apple_remove.one()
        self.emit_progress("获取SSTT", self.row)
        result_two = self.apple_remove.two()
        result_three = self.apple_remove.three()
        result_four = self.apple_remove.four()
        result_five = self.apple_remove.five()
        result_six = self.apple_remove.six()
        result_seven = self.apple_remove.seven()
        result_eight = self.apple_remove.eight()
        result_nine = self.apple_remove.nine()
        result_ten = self.apple_remove.ten()
        result_eleven = self.apple_remove.eleven()
        result_twelve = self.apple_remove.twelve()
        result_thirteen = self.apple_remove.thirteen()
        result_fourteen = self.apple_remove.fourteen()
        result_fifteen = self.apple_remove.fifteen()
        result_sixteen = self.apple_remove.sixteen()
        result_seventeen = self.apple_remove.seventeen()
        result_eighteen = self.apple_remove.eighteen()
        result_nineteen = self.apple_remove.nineteen()
        result_twenty = self.apple_remove.twenty()
        result_twenty_one = self.apple_remove.twenty_one()
        result_twenty_two = self.apple_remove.twenty_two()
        result_twenty_three = self.apple_remove.twenty_three()
        result_twenty_four = self.apple_remove.twenty_four()
        result_twenty_five = self.apple_remove.twenty_five()
        result_twenty_six = self.apple_remove.twenty_six()
        result_twenty_seven = self.apple_remove.twenty_seven()
        result_twenty_eight = self.apple_remove.twenty_eight()
        result_twenty_nine = self.apple_remove.twenty_nine()
        result_thirty = self.apple_remove.thirty()
        result_thirty_one = self.apple_remove.thirty_one()
        result_thirty_two = self.apple_remove.thirty_two()
        result_thirty_three = self.apple_remove.thirty_three()
        result_thirty_four = self.apple_remove.thirty_four()
        result_thirty_five = self.apple_remove.thirty_five()
        result_thirty_six = self.apple_remove.thirty_six()
    def emit_progress(self, message, row):
        self.progress_signal.emit(message, row)


if __name__ == "__main__":
    app = QApplication([])
    window = APPLE_UI()
    window.show()
    app.exec()
