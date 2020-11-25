from Terminal import Terminal
class Menu:
	"""
	Menu is a way for the user to interface with the program.

	Menu is a module which displays items that are numbered and get's user
	input on which option they would like to select from said items

	"""
	def __init__(self):
		"""
		Creates an instance of Menu

		Parameters:
			terminal:
				A Terminal object allowing this module to interface
				with the OS terminal
		Returns:
			An instance of Menu
		"""
		self.__menuItems__ = []
		self.__length__ = 0

		Terminal.clear()

	def addMenuItem(self, string):
		"""
		Adds an item to Menu's list serving as an additional
		option to be displayed or selected

		Parameters:
			string:
				A String object containing the menu option to
				be added
		"""
		self.__menuItems__.append(string)
		self.__length__ += 1
	
	
	def clearMenu(self):
		"""
		Clears Menu's list serving to wipe all options
		from Menu
		"""
		self.__menuItems__ = []
		self.__length__ = 0

	def printItems(self):
		"""
		Prints all of the String objects within menuItems
		serving as a way to provide a userInterface which can
		be interfaced with through Menu's other methods
		"""
		for i, menuItem in enumerate(self.__menuItems__):
			print(str(i+1) + ". " + self.__menuItems__[i])
		print("\n")
	
	def isNumericalSelection(self, userInput):
		"""
		Serves as a way to validate input and ensure
		the input is not outside of the acceptable range
		or of an invalid type

		Returns:
			A Boolean object if the input is numerical
			None if the input is invalid due to being non-numerical
		"""
		try:
			userInput = int(userInput)
			if userInput <= self.__length__ and userInput >= 1:
				return True
			else:
				return False
		except Exception:
			return None
	
	def printScreen(self):
		"""
		The main loop of Menu. Serves to print all menu items,
		gather userInput and ensure that input is valid

		Returns:
			userInput if the input provided is valid
			None if the input provided is invalid
		"""
		while True:
			self.printItems()
			userInput = input("Type the number of the item you would like to select: ")
			try:
				userInput = int(userInput) - 1
				if (userInput <= self.__length__ - 1 and userInput >= 0):
					return userInput
				else:
					input("Invalid selection, press enter to continue: ")
			except Exception:
				try:
					if userInput.upper() == "EXIT":
						return None
				except Exception:
					input("Invalid input, press enter to continue: ") 
			Terminal.clear()

if __name__ == "__main__":
	menu = Menu()
	menu.addMenuItem("Just")
	menu.addMenuItem("A")
	menu.addMenuItem("Test")
	print(menu.printScreen())
