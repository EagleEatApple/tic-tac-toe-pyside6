import os
import random
import time
from chooseplayer import ChoosePlayer
from PySide6.QtWidgets import QMainWindow, QPushButton, QLabel
from PySide6.QtGui import Qt, QIcon, QFont

# Create the main window of the game
class MainWindow(QMainWindow):
    # Initiate the main window
    def __init__(self):
        super().__init__()
        
        # Set the icon and the title of the window
        self.iconsPath = os.path.abspath(os.path.dirname(__file__)) + '/icons/'
        self.setWindowIcon(QIcon(self.iconsPath + 'app.png'))
        self.setWindowTitle("Eagle's Tic Tac Toe")
        
        # Set the size of the window
        self.setFixedWidth(300)
        self.setFixedHeight(500)
        
        # Initiate game settings
        self.initGame()
        
        # Set the layout of the window
        self.createUI()
        
        # Show the window
        self.show()
        
		# Choose player
        # The first player is 'X', the second player is 'O'
        dlg = ChoosePlayer()
        dlg.exec_()
        if dlg.player == 'X':
            self.resultArea.setText("You're X, please move")
            self.humanFirst = 0
        else:
            self.resultArea.setText("You're O, please move")
            self.humanFirst = 1
            self.setRandomPlace()
            time.sleep(1)
            
    def initGame(self):
        # The turn of the game, 0 means 'X' move, 1 means 'O' move
        self.turn = 0
        
        # The total turns, if it equals to 9 then the game is tie
        self.total = 0
        
        # The game board made by buttons
        self.boardButtons = []

    def createUI(self):
        # Create 3*3 game board by using buttons
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append((QPushButton(self)))
            self.boardButtons.append(temp)
        
        # Initiate the position and size of buttons
        for i in range(3):
            for j in range(3):
                self.boardButtons[i][j].setGeometry(90 * i + 20,
                                                    90 * j + 20,
                                                    80, 80)
                self.boardButtons[i][j].setFont(QFont(QFont('Times', 30)))
                self.boardButtons[i][j].clicked.connect(self.clickAction)
        
        # Initiate the result area
        self.resultArea = QLabel(self)
        self.resultArea.setGeometry(20, 310, 260, 50)
        self.resultArea.setStyleSheet("QLabel"
                                      "{"
                                      "border : 2px solid black;"
                                      "background : white;"
                                      "}")
        self.resultArea.setAlignment(Qt.AlignCenter)
        self.resultArea.setFont(QFont('Times', 14))
        
        # Initiate the reset button
        self.resetButton = QPushButton("Reset", self)
        self.resetButton.setGeometry(60, 390, 180, 40)
        self.resetButton.clicked.connect(self.resetAction)
    
    # Reset the game
    def resetAction(self):
        self.turn = 0
        self.total = 0
        for btns in self.boardButtons:
            for btn in btns:
                btn.setEnabled(True)
                btn.setText("")
        if self.humanFirst == 1:
            self.setRandomPlace()
            time.sleep(1)
            self.resultArea.setText("You're O, please move")
        else:
            self.resultArea.setText("You're X, please move")
                
    # When the button is clicked
    def clickAction(self):
        self.total += 1
        button = self.sender()
        button.setEnabled(False)
        self.resultArea.setText("The game is progressing")
        if self.humanFirst == 0:
            if self.turn == 0:
                button.setText('X')
                self.turn = 1
                if self.evaluateResult() != 1 and self.evaluateResult() != -1:
                    self.setRandomPlace()
            else:
                button.setText('O')
                self.turn = 0
                self.evaluateResult()
        else:
            if self.turn == 0:
                button.setText('X')
                self.turn = 1
                self.evaluateResult()
            else:
                button.setText('O')
                self.turn = 0
                if self.evaluateResult() != 1 and self.evaluateResult() != -1:
                    self.setRandomPlace()
        
    # Evaluate the result of the game then show the result
    def evaluateResult(self):
        result = ""
        win = self.checkWinner()
        if self.total == 9 and win == False:
            result = "The game is tie!"
            self.resultArea.setText(result)
            return -1
        else:
            if win == True:
                if self.humanFirst == 0:
                    if self.turn == 0:
                        result = "You lost!"
                    else:
                        result = "You Won!"
                else:
                    if self.turn == 0:
                        result = "You Won!"
                    else:
                        result = "You lost!"
                for btns in self.boardButtons:
                    for btn in btns:
                        btn.setEnabled(False)
                self.resultArea.setText(result)
                return 1
    
    # Check the winner
    def checkWinner(self):
        # Check all of 3 rows
        for i in range(3):
            if self.boardButtons[0][i].text() == self.boardButtons[1][i].text() \
                and self.boardButtons[0][i].text() == self.boardButtons[2][i].text() \
                and self.boardButtons[0][i].text() != "":
                return True

        # Check all of 3 columns
        for i in range(3):
            if self.boardButtons[i][0].text() == self.boardButtons[i][1].text() \
                and self.boardButtons[i][0].text() == self.boardButtons[i][2].text() \
                and self.boardButtons[i][0].text() != "":
                return True
        
        # Check 2 diagonals
        if self.boardButtons[0][0].text() == self.boardButtons[1][1].text() \
            and self.boardButtons[0][0].text() == self.boardButtons[2][2].text() \
            and self.boardButtons[0][0].text() != "":
            return True
        if self.boardButtons[0][2].text() == self.boardButtons[1][1].text() \
            and self.boardButtons[1][1].text() == self.boardButtons[2][0].text() \
            and self.boardButtons[0][2].text() != "":
            return True
        
        # otherwise there is no winner
        return False
    
    # Check available positions
    def CheckAvailablePositions(self):
        states = []
        for i in range(3):
            for j in range(3):
                if self.boardButtons[i][j].text() == "":
                    states.append((i, j))
        return (states)
                    
    # Get next move randomly
    def setRandomPlace(self):
        if self.total < 9:
            selection = self.CheckAvailablePositions()
            newPlace = random.choice(selection)
            print(newPlace, newPlace[0], newPlace[1])
            self.boardButtons[newPlace[0]][newPlace[1]].animateClick()
