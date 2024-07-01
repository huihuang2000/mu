import sys
import re
import asyncio
import aiohttp
from itertools import zip_longest
import winsound
import pygame
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
)
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal, Qt,QTimer

# Pyinstaller -F -w 链接查订单-自动.py

pygame.mixer.init()
sound = pygame.mixer.Sound('apple-Query_model/测试/1.wav')

class AsyncRequest(QObject):
    finished = Signal()
    result = Signal(int, dict)

    def __init__(self, row, url):
        super().__init__()
        self.row = row
        self.url = url

    async def fetch_data(self, max_retries=10):
        for attempt in range(max_retries):
            try:
                async with aiohttp.ClientSession() as session:
                    response = await session.get(self.url, timeout=5)
                    response.raise_for_status()
                    response_text = await response.text()

                    # 正则表达式匹配逻辑
                    if '"Track shipment” link' in response_text:
                        Track_shipment = "Track shipment"
                    else:
                        Track_shipment = ""

                    modo = r'"productName"\s*:\s*"([^"]+)"'
                    time = r'"orderPlacedDate"\s*:\s*"([^"]+)"'
                    dd = r'/shop/order/detail/\d+/([^"/]+)'
                    status = r'"deliveryDate"\s*:\s*"([^"]+)"'
                    pattern = r'"currentStatus"\s*:\s*"([^"]+)"'
                    Order_number = r"trackingURLMap\":\s*\{\"(.*?)\"\:\s*\"(.*?)\""
                    # 仓库
                    first_names = re.findall(r'"firstName":"([^"]+)"', response_text)
                    last_names = re.findall(r'"lastName":"([^"]+)"', response_text)
                    name_pairs = [
                        f"{name1.strip()} {name2.strip()}"
                        for name1, name2 in zip_longest(
                            first_names, last_names, fillvalue=""
                        )
                    ]
                    unique_name_pairs = list(set(name_pairs))
                    sorted_unique_name_pairs = sorted(
                        unique_name_pairs,
                        key=lambda pair: (len(pair.split()[0]), pair.lower()),
                    )
                    first_variable = (
                        sorted_unique_name_pairs[0] if sorted_unique_name_pairs else ""
                    )
                    second_variable = (
                        sorted_unique_name_pairs[1]
                        if len(sorted_unique_name_pairs) > 1
                        else ""
                    )

                    MODO = re.search(modo, response_text)
                    TIME = re.search(time, response_text)
                    DD = re.search(dd, response_text)
                    STATUS = re.search(status, response_text)
                    The_status_of_the_goods = re.search(pattern, response_text)

                    Order_number = re.search(Order_number, response_text)

                    if MODO and TIME and DD and STATUS:
                        result_data = {
                            "productName": MODO.group(1) if MODO else "",
                            "orderPlacedDate": TIME.group(1) if TIME else "",
                            "orderNumber": DD.group(1) if DD else "",
                            "status": STATUS.group(1) if STATUS else "",
                            "Track_shipment": Track_shipment,
                            "The_status_of_the_goods": (
                                The_status_of_the_goods.group(1)
                                if The_status_of_the_goods
                                else ""
                            ),
                            "Order_number": (
                                Order_number.group(1) if Order_number else ""
                            ),
                            "Delivers": first_variable,
                            "Bills_to": second_variable,
                        }
                        # print(result_data)
                        self.result.emit(self.row, result_data)
                        return  # 成功获取数据后退出函数

                    raise ValueError("Data not found in response")

            except Exception as e:
                if attempt < max_retries:
                    # print(attempt)
                    await asyncio.sleep(2)
                    pass
                else:
                    self.result.emit(self.row, error_message)  # 发射错误信息
                error_message = {"error": f"Error: {e}"}
            finally:
                self.finished.emit()


class AsyncRequestWorker(QRunnable):
    def __init__(self, async_request):
        super().__init__()
        self.async_request = async_request

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.async_request.fetch_data())


class InterFace(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.threadpool = QThreadPool()
        self.auto_query_timer = QTimer(self)
        self.auto_query_timer.timeout.connect(self.auto_query)
        # self.auto_query_timer.start(1000)
        self.auto_query_timer.start(100000)

    def initUI(self):
        self.setWindowTitle("Async HTTP Requests with PyQt6")
        self.setGeometry(100, 100, 1800, 600)

        h_layout_buttons = QHBoxLayout()
        self.button_import1 = QPushButton("import", self)
        self.button_import2 = QPushButton("clean", self)
        self.button_import3 = QPushButton("Inquire", self)
        h_layout_buttons.addWidget(self.button_import1)
        h_layout_buttons.addWidget(self.button_import2)
        h_layout_buttons.addWidget(self.button_import3)
        h_layout_buttons.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.table_widget = QTableWidget(0, 10, self)
        self.table_widget.setHorizontalHeaderLabels(
            [
                "url",
                "modo",
                "order number",
                "order time",
                "status",
                "The_status_of_the_goods",
                "Order_number",
                "Track shipment",
                "Delivers",
                "Bills to",
            ]
        )
        self.table_widget.setShowGrid(True)
        self.table_widget.setColumnWidth(0, 500)
        self.table_widget.setColumnWidth(1, 300)
        self.table_widget.setColumnWidth(2, 100)
        self.table_widget.setColumnWidth(3, 100)
        self.table_widget.setColumnWidth(4, 200)
        self.table_widget.setColumnWidth(5, 200)
        self.table_widget.setColumnWidth(6, 200)
        self.table_widget.setColumnWidth(7, 200)
        self.table_widget.setColumnWidth(8, 70)
        self.table_widget.setColumnWidth(9, 70)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_buttons)
        v_layout.addWidget(self.table_widget)
        self.setLayout(v_layout)

        self.button_import1.clicked.connect(self.Get_link)
        self.button_import2.clicked.connect(self.clear_table)
        self.button_import3.clicked.connect(self.on_query_clicked)

    def auto_query(self):
        if not self.button_import3.hasFocus():
            self.button_import3.click()

    def on_query_clicked(self):
        for row in range(self.table_widget.rowCount()):
            for col in range(1, 10):
                self.table_widget.setItem(row, col, QTableWidgetItem(""))

        for row in range(self.table_widget.rowCount()):
            url_item = self.table_widget.item(row, 0)
            if url_item and url_item.text():
                async_request = AsyncRequest(row, url_item.text())
                async_request.result.connect(self.update_table)
                worker = AsyncRequestWorker(async_request)
                self.threadpool.start(worker)

    def update_table(self, row, result):
        if "error" in result:
            self.table_widget.setItem(row, 1, QTableWidgetItem(""))
            self.table_widget.setItem(row, 2, QTableWidgetItem(""))
            self.table_widget.setItem(row, 3, QTableWidgetItem(""))
            self.table_widget.setItem(row, 4, QTableWidgetItem(""))
            self.table_widget.setItem(row, 5, QTableWidgetItem(""))
            self.table_widget.setItem(row, 6, QTableWidgetItem(""))
            self.table_widget.setItem(row, 7, QTableWidgetItem(""))
            self.table_widget.setItem(row, 8, QTableWidgetItem(""))
            self.table_widget.setItem(row, 9, QTableWidgetItem(""))
        else:
            self.table_widget.setItem(
                row, 1, QTableWidgetItem(str(result["productName"]))
            )
            self.table_widget.setItem(
                row, 2, QTableWidgetItem(str(result["orderNumber"]))
            )
            self.table_widget.setItem(
                row, 3, QTableWidgetItem(str(result["orderPlacedDate"]))
            )
            self.table_widget.setItem(row, 4, QTableWidgetItem(str(result["status"])))
            self.table_widget.setItem(
                row, 5, QTableWidgetItem(str(result["The_status_of_the_goods"]))
            )
            self.table_widget.setItem(
                row, 6, QTableWidgetItem(str(result["Order_number"]))
            )
            self.table_widget.setItem(
                row, 7, QTableWidgetItem(str(result["Track_shipment"]))
            )
            self.table_widget.setItem(row, 8, QTableWidgetItem(str(result["Delivers"])))
            self.table_widget.setItem(row, 9, QTableWidgetItem(str(result["Bills_to"])))
            # if result['The_status_of_the_goods'] == "DELIVERED":
                # winsound.Beep(800, 200)
            # !!!
            if result['The_status_of_the_goods'] == "DELIVERED":
                    sound.play() 

    def Get_link(self):
        clipboard = QApplication.clipboard().text()
        if clipboard:
            items = clipboard.split()
            self.table_widget.setRowCount(len(items))
            for i, item in enumerate(items):
                self.table_widget.setItem(i, 0, QTableWidgetItem(item))

    def clear_table(self):
        self.table_widget.clearContents()
        self.table_widget.setRowCount(0)


if __name__ == "__main__":
    app = QApplication([])
    window = InterFace()
    window.show()
    sys.exit(app.exec())
