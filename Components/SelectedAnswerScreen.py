from Terminal import Terminal
from PostPrinter import PostPrinter

class SelectedAnswerScreen:
	"""
	SelectedAnswerScreen is a Screen object which displays an answer post

	SelectedAnswerScreen displays an answer post and various actions one can take
	on it
	"""
	def printMenu():
		"""
		Prints the menu of actions the user can take on the answer post
		"""
		menuOptions = ["Vote","Exit"]
		for i,option in enumerate(menuOptions):
			print(str(i+1) + ". " + option)

	def printScreen(post):
		"""
		Provides the main functionality of SelectedAnswerScreen
		Prints the answer post using PostPrinter object before printing
		the menu of user options and prompting the user for input
		vets user input before returning it

		Parameters:
			post:
				A Dictionary object representing an answer from the database
		Returns:
			An Integer object representing the user selected menu option
		"""
		MAX_MENU_OPTION = 2
		MIN_MENU_OPTION = 1
		invalidInput = True
		while invalidInput:
			PostPrinter.printTitle(post)
			SelectedAnswerScreen.printMenu()

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
	from SelectedQuestionScreen import SelectedQuestionScreen
	from AnswerListScreen import AnswerListScreen

	search = SearchForQuestionsScreen
	select = SelectedQuestionScreen
	listAnswer = AnswerListScreen

	question = search.printScreen()
	if (SelectedQuestionScreen.printScreen(question) == 2):
		answer = listAnswer.printScreen(question)
		if (answer):
			SelectedAnswerScreen.printScreen(answer)