from PySide6.QtWidgets import QDialog, QDialogButtonBox, QRadioButton, QVBoxLayout, QLabel
from PySide6.QtGui import Qt, QFont

# Choose player
class ChoosePlayer(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose Player!")
        qbtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(qbtn)
        self.buttonBox.accepted.connect(self.accept)
        
        # The palyer is 'X' by default
        self.layout = QVBoxLayout()
        self.player = 'X'
        rbtn1 = QRadioButton('Player X', self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)
        rbtn1.toggled.connect(self.updateResult)
        rbtn2 = QRadioButton('Player O', self)
        rbtn2.move(50, 70)
        rbtn2.toggled.connect(self.updateResult)
        self.info = QLabel(self)
        self.info.setGeometry(50, 90, 260, 30)
        self.info.setStyleSheet("QLabel"
                                      "{"
                                      "border : 2px solid black;"
                                      "background : white;"
                                      "}")
        self.info.setAlignment(Qt.AlignCenter)
        self.info.setFont(QFont('Times', 14))
        self.info.setText("You're X, please click any button to start")
        self.layout.addWidget(rbtn1)
        self.layout.addWidget(rbtn2)
        self.layout.addWidget(self.info)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        
    def updateResult(self, value):
        rbtn = self.sender()
        if rbtn.text() == 'Player X':
            self.player = 'X'
            self.info.setText("You're X, please click any button to start")
        else:
            self.player = 'O'
            self.info.setText("You're O, please click any button to continue")

