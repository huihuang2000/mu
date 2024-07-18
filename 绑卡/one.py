from PySide6.QtWidgets import QApplication, QWidget, QInputDialog
from PySide6.QtCore import Qt


class mywindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.read = QInputDialog.getInt(self, "标题", "提示信息")

        self.addAction(self.read)


if __name__ == "__main__":
    app = QApplication([])
    window = mywindow()
    window.show()
    app.exec()
