class WelcomeScreen:
	"""
	A Screen which is used to welcome the user.

	This module is used to welcome the user and asks
	the user for their status which is either registered
	or not registered.
	"""
	def __init__(self, terminal):
		"""
		Creates an instance of WelcomeScreen, which is the UI interface for welcoming users to the
		program. Gets user input for deciding whether the user needs to register or login
		Parameters:
			Terminal: 
				Terminal object. Used as an interface between this module and the terminal of the OS
		Returns:
			An instance of WelcomeScreen
		"""
		self.__terminal__ = terminal
		self.__terminal__.clear()

	def printTitle(self):
		"""
		Prints main elements of the UI
		"""
		self.__terminal__.printCenter("--- Welcome User ---")
		self.__terminal__.printCenter("(Type exit to quit at any time)")
		
	def printScreen(self):
		"""
		The main loop of the module. Prints the title and get's users input on whether they
		are registering or logging in
		"""
		while True:
			self.printTitle()
			userInput = input("If you're an existing user, please enter your id. Otherwise, press enter: ").upper()
			
			#if the user presses enter
			if userInput == "":
				return 1
			#if the user enters an id
			elif userInput.strip() != "EXIT":
				#TODO: verify the uid, return it if applicable
				uid = self.get_uid()
				if uid:
					return uid
			elif userInput.strip() == "EXIT":
				return None
			else:
				input("Invalid input, press enter to continue: ")
				self.__terminal__.clear()

	def get_uid(self):
		#TODO: get the uid and return it if it exists
		pass
		
if __name__ == "__main__":
	from Terminal import Terminal
	welcomeScreen = WelcomeScreen(Terminal())
	welcomeScreen.printScreen()
