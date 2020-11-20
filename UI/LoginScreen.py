from LoginUser import LoginUser
from Terminal import Terminal

class LoginScreen:
	"""
	A screen which handles logging in and the processes
	associated within it.

	This module is responsible for providing the UI of the log in
	screen as well as handleing calls to the database to authenticate
	users. 
	"""
	
	def __init__(self, terminal):
		"""
		Creates an instance of LoginScreen, which is the UI interface for logging into the program.
		
		Parameters:
			Terminal: Terminal object. Used for extra console commands, like clearing the screen and printing to the center of it.
			
		Returns: N/A
		"""
		self.__terminal__ = terminal
		self.__dbName__ = terminal.getDBName()
		
	def log_in(self):
		"""
		UI interface for logging in, using the framework from LoginUser.py.
		
		Parameters: N/A
		
		Returns: UID of user.
		"""
		
		#Main input loop. Asks for the uid of the user, validates it is formatted correctly, then does the same for the password
		#if the password and uid are valid, returns the uid. User is reprompted otherwise.
		while True:
			self.__terminal__.clear()
			self.__terminal__.printCenter("---LOGIN---")
			print("\n")
			uid = input("Please enter your UID, or enter \"exit\" to go back. ").strip()
			
			#If the user opts to register, exits the function
			if uid == "exit":
				return None
			#If the uid is not exactly 4 character long, restart loop
			elif len(uid) != 4:
				input("A UID is four lowercase characters long, Please try again. Press enter to continue:")
				continue
			
			pswd = input("Please enter your password: ")
			
			#If the login was successful, break the loop and return the uid
			if LoginUser.logIn(self.__dbName__, uid, pswd):
				break
			#if the login was unsuccessful, restart loop
			else:
				input("Incorrect UID or password. Press enter to try again:")
		
		return uid
		
		
if __name__ == "__main__":
	terminal = Terminal()
	test = LoginScreen(terminal, 'Miniproject_1.db')
	
	print(test.log_in())
