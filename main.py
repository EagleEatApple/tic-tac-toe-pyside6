import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

# Start the tic tac toe app
def main():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

