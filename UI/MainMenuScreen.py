from Interface.Menu import Menu

class MainMenuScreen:
	"""
	A screen which allows the user to select
	an action they would like to perform.

	This module provides the ui for the main interface
	as well as handling the selection of an action within
	the program
	"""
	def __init__(self):
		"""
		Creates an instance of MainMenuScreen

		Parameters:
			N/A
		Returns:
			An instance of MainMenuScreen
		"""
		self.__menu__ = Menu()
	
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
	from Interface.Terminal import Terminal
	mainMenu = MainMenuScreen()
	mainMenu.printScreen()		
