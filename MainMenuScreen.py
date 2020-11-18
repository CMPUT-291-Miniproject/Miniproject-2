from Menu import Menu

class MainMenuScreen:
	"""
	A screen which allows the user to select
	an action they would like to perform.

	This module provides the ui for the main interface
	as well as handling the selection of an action within
	the program
	"""
	def __init__(self, terminal):
		"""
		Creates an instance of MainMenuScreen

		Parameters:
			terminal:
				A Terminal object that allows the module to interface
				with the OS terminal
		Returns:
			An instance of MainMenuScreen
		"""
		self.__menu__ = Menu(terminal)
	
		self.__menu__.addMenuItem("Post a question")
		self.__menu__.addMenuItem("Search for posts")
		self.__menu__.addMenuItem("Logout")
		self.__menu__.addMenuItem("Exit Program")

	def printScreen(self):
		"""
		Prints MainMenu's menu
		"""
		return self.__menu__.printScreen()

if __name__ == "__main__":
	from Terminal import Terminal
	mainMenu = MainMenuScreen(Terminal())
	mainMenu.printScreen()		
