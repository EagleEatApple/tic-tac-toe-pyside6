import sys
from PySide6.QtWidgets import *
from mainwindow import MainWindow

# start the app
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
