import sys
from PySide6 import QtWidgets
from ui3 import Ui_MainWindow

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MainUi()
    widget.show()

    sys.exit(app.exec())