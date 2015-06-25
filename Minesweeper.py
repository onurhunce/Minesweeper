from random import randint
import random

class Cell(object):
	
	isOpen = False
	value = 0
	def __init__(self, row, column):

		self.row = row
		self.column = column

		
class MineSweeper(object):
		
	row_size = 0
	column_size = 0
	bomb_number = 0
	cells = []

	#Initiliaze game
	def __init__(self, row, column, difficulty):

		self.row_size = row
		self.column_size = column
		for i in range(1,(column+1)):
			for j in range(1, (row+1)):
				self.cells.append(Cell(i, j))				
	
		if difficulty == "Easy":

			if row * column < 30:			
				self.bomb_number = 5						
			elif row * column < 100:
				self.bomb_number = 10			
			else:
				self.bomb_number = 15		
		
		elif difficulty == "Medium":

			if row * column < 30:
				self.bomb_number = 10	
			elif row * column < 100:
				self.bomb_number = 15	
			else:
				self.bomb_number = 20

		elif difficulty == "Hard":	

			if row * column < 30:
				self.bomb_number = 15
			elif row * column < 100:
				self.bomb_number = 20		
			else:
				self.bomb_number = 30

		else:
			raise Exception("Your level input is wrong!")	

			
	#Prints field of the game.
	def print_field(self):

		gameEnd = False
		score = 0
		self.repeat_field()
		while gameEnd == False:
			print("\n"),
			print "Choose column and row(Ex: 5 4): "
			user_row, user_column = int(raw_input()), int(raw_input())
			if(self.cells[self.row_size * (user_row-1) + (user_column-1)].isOpen) == False:
				if self.cells[self.row_size * (user_row-1) + (user_column-1)].value == 99:
					gameEnd = True
					print("\n"),
					print "Bomba! Game is over"
					print "Your score is: %r" %score				
					self.open_field()
				else:
					self.cells[self.row_size * (user_row-1) + (user_column-1)].isOpen = True
					score += 5
					self.repeat_field()	

	def repeat_field(self):
		
		print("\n"),
		for k,v in enumerate(self.cells):			
			if k % self.row_size is 0:
				print("\n"),
			if v.isOpen == True:
				print("%s \t" %v.value),
			else:		
				print "X \t",

	def open_field(self):
		for k,v in enumerate(self.cells):			
			if k % self.row_size is 0:
				print("\n"),	
			print("%s \t" %v.value),		

		print "\n"				

	#Insert specified number of mines into the area, increase numbers of its neigbours.
	def insert_mines(self):
		
		bomb_position = random.sample(range(0,	
					    (self.row_size*self.column_size)-1), self.bomb_number)
		
		for bomb in bomb_position:
			self.cells[bomb].value = 99

		for locatedBomb in bomb_position:
			neigbourlist = []
			#except right corner
			if (locatedBomb+1) % self.row_size != 0:
				neigbourlist.append(locatedBomb+1) 
				neigbourlist.append(locatedBomb+self.row_size+1)
				neigbourlist.append(locatedBomb-self.row_size+1)
			#except left corner	
			if locatedBomb % self.row_size != 0:	
				neigbourlist.append(locatedBomb-1)
				neigbourlist.append(locatedBomb+self.row_size-1)  		 	
				neigbourlist.append(locatedBomb-self.row_size-1)
			
			#all fields
			neigbourlist.append(locatedBomb+self.row_size)
			neigbourlist.append(locatedBomb-self.row_size)
			
			#increase proper neighbours one
			for neigbour in neigbourlist:
				if neigbour > -1 and neigbour < len(self.cells):
					if self.cells[neigbour].value != 99:
						self.cells[neigbour].value += 1
#Testing class

print "Welcome to minesweeper game!"
print "Enter row number: " 
row = int(raw_input())
print "Enter column number: " 
column = int(raw_input())
print "Choose your level: Easy / Medium / Hard "
difficulty=raw_input()
try:
	Game= MineSweeper(row, column, difficulty)
	Game.insert_mines()		
	Game.print_field()
except Exception as e:
	print e
