from os import system
import shutil
import sys

class Terminal:
	"""
	Terminal serves as an interface to interact with the OS terminal.

	Terminal is a module which other modules can use to perform actions
	on the operating systems terminal.
	"""	
	def __init__(self):
		"""
		Creates an instance of LoginScreen, which is the UI interface for logging into the program.
		
		Parameters:
			Terminal: 
				Terminal object. Used for extra console commands, like clearing the screen and printing to the center of it.
			
		Returns: N/A
		"""
		self.__screenSize__ = shutil.get_terminal_size().columns
	
	def clear(self):
		"""
		Clears the OS terminal
		"""
		system("clear")
	
	def printCenter(self, string):
		"""
		Prints a string at the center of the screen.

		Parameters:
			string:
				A String object which contains the string to be printed at the center of the screen

		"""
		print(string.center(self.__screenSize__))		
	
	def getPort(self):
		"""
		Grabs the port assuming it is the first argument given in the command line on start
		"""
		return sys.argv[1]		
