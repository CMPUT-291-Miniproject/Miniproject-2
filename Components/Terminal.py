from os import system
import shutil
import sys

class Terminal:
	"""
	Terminal serves as an interface to interact with the OS terminal.

	Terminal is a module which other modules can use to perform actions
	on the operating systems terminal.
	"""
	screenSize = shutil.get_terminal_size().columns
	
	def clear():
		"""
		Clears the OS terminal
		"""
		system("clear")
	
	def printCenter(string):
		"""
		Prints a string at the center of the screen.

		Parameters:
			string:
				A String object which contains the string to be printed at the center of the screen

		"""
		print(string.center(Terminal.screenSize))		
	
	def getPort():
		"""
		Grabs the port assuming it is the first argument given in the command line on start
		"""
		return sys.argv[1]

	def getDBName():
		"""
		Grabs the db name as per the spec
		"""
		return "291db"

if __name__ == "__main__":
	Terminal.clear()
	Terminal.printCenter("Hello World")
	Terminal.getPort()
	input("Press enter to continue: ")
	Terminal.clear()	
