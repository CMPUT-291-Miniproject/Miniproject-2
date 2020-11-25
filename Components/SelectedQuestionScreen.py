from Terminal import Terminal
from PostPrinter import PostPrinter

class SelectedQuestionScreen:
	"""
	SelectedQuestionScreen is a Screen object which displays a question post

	SelectedQuestionScreen displays a question post and various actions one can take
	on it
	"""
	def printMenu():
		"""
		Prints the menu of actions the user can take on the question post
		"""
		menuOptions = ["Answer Question","List Answers","Vote","Exit"]
		for i,option in enumerate(menuOptions):
			print(str(i+1) + ". " + option)

	def printScreen(post):
		"""
		Provides the main functionality of SelectedQuestionScreen
		Prints the question post using PostPrinter object before printing
		the menu of user options and prompting the user for input
		vets user input before returning it

		Parameters:
			post:
				A Dictionary object representing a question from the database
		Returns:
			An Integer object representing the user selected menu option
		"""
		MAX_MENU_OPTION = 4
		MIN_MENU_OPTION = 1
		invalidInput = True
		while invalidInput:
			PostPrinter.printTitle(post)
			SelectedQuestionScreen.printMenu()

			userInput = input("Select Option: ")
			if userInput.upper() == "EXIT" or userInput.upper() == "QUIT":
				return None

			try:
				userInput = int(userInput)
				if userInput > MAX_MENU_OPTION or userInput < MIN_MENU_OPTION:
					print("Selection out of range!")
				else:
					invalidInput = False
			except Exception:
				print("Invalid Input!")
			finally:
				input("Press Enter to Continue: ")
		return userInput

		

		


if __name__ == "__main__":
	from SearchForQuestionsScreen import SearchForQuestionsScreen

	sScreen = SearchForQuestionsScreen
	post = sScreen.printScreen()
	SelectedQuestionScreen.printScreen(post)