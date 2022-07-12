import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import *

# create the main window of the game
class MainWindow(QMainWindow):
	# initiate the main window
	def __init__(self):
		super().__init__()
        
		# set the title of the window
		self.icons_path = os.path.abspath(os.path.dirname(__file__)) + '/icons/'
		self.setWindowIcon(QIcon(self.icons_path + 'app.png'))
		self.setWindowTitle("Eagle's Tic Tac Toe")

		# set the size of the window
		self.setFixedWidth(300)
		self.setFixedHeight(500)

		# initiate game settings
        # the first player is 'X', the second player is 'O'
		self.player1 = 'X'
		self.player2 = 'O'
        # the turn of the game, 0 means 'X' move, 1 means 'O' move
		self.turn = 0
        # the total turns, if it equals to 9 then the game is draw
		self.total = 0

		# set the layout of the game
		self.create_ui()

		# show the window
		self.show()

	# create 3*3 game layout by using buttons
	def create_ui(self):
		self.buttons = []

		# initiate 3*3 buttons list to form the game board
		for i in range(3):
			temp = []
			for j in range(3):
				temp.append((QPushButton(self)))
			self.buttons.append(temp)

		# initiate the position and size of buttons
		x = 90
		y = 90
		gap = 20
		width = 80
		height = 80
		fontsize = 20

		# layout 3*3 buttons
		for i in range(3):
			for j in range(3):
				# set the size of each button
				self.buttons[i][j].setGeometry(x*i + gap,
												y*j + gap,
												width, height)

				# set the font style to the button
				self.buttons[i][j].setFont(QFont(QFont('Times', fontsize)))

				# add action to the button
				self.buttons[i][j].clicked.connect(self.click_action)

		# initiate the result area
		self.result = QLabel(self)
		self.result.setGeometry(20, 310, 260, 50)
		self.result.setStyleSheet("QLabel"
								"{"
								"border : 2px solid black;"
								"background : white;"
								"}")
		self.result.setAlignment(Qt.AlignCenter)
		self.result.setFont(QFont('Times', fontsize))

		# initiate the reset button
		self.reset = QPushButton("Reset", self)
		self.reset.setGeometry(60, 390, 180, 40)
		self.reset.clicked.connect(self.reset_action)

	# reset the game
	def reset_action(self):
		self.turn = 0
		self.total = 0
		self.result.setText("")
		for buttons in self.buttons:
			for button in buttons:
				button.setEnabled(True)
				button.setText("")

	# calculate the result based on each click or move
	def click_action(self):
		# the total turn will be increased by each click
		self.total += 1

		# detect which button is clciked
		button = self.sender()
		button.setEnabled(False)

		# check the turn
		if self.turn == 0:
			button.setText(self.player1)
			self.turn = 1
		else:
			button.setText(self.player2)
			self.turn = 0

		# result of the game
		re = ""

		# check the winner
		win = self.check_winner()
		if win == True:
			if self.turn == 0:
				re = "O is Winner!"
			else:
				re = "X is Winner!"
			for buttons in self.buttons:
				for push in buttons:
					push.setEnabled(False)
		elif self.total == 9:
			re = "The game is Draw!"

		# set the result area
		self.result.setText(re)


	# check the winner
	def check_winner(self):
		# check all of 3 rows
		for i in range(3):
			if self.buttons[0][i].text() == self.buttons[1][i].text() \
					and self.buttons[0][i].text() == self.buttons[2][i].text() \
					and self.buttons[0][i].text() != "":
				return True

		# check all of 3 columns
		for i in range(3):
			if self.buttons[i][0].text() == self.buttons[i][1].text() \
					and self.buttons[i][0].text() == self.buttons[i][2].text() \
					and self.buttons[i][0].text() != "":
				return True

		# check 2 diagonals
		if self.buttons[0][0].text() == self.buttons[1][1].text() \
				and self.buttons[0][0].text() == self.buttons[2][2].text() \
				and self.buttons[0][0].text() != "":
			return True
		if self.buttons[0][2].text() == self.buttons[1][1].text() \
				and self.buttons[1][1].text() == self.buttons[2][0].text() \
				and self.buttons[0][2].text() != "":
			return True

		#if nothing then there is no winner
		return False