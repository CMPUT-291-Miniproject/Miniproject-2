from Terminal import Terminal
from Interface.PostPrinter import PostPrinter

class SelectedAnswerScreen:
	def printMenu():
		menuOptions = ["Vote","Exit"]
		for i,option in enumerate(menuOptions):
			print(str(i+1) + ". " + option)

	def printScreen(post):
		MAX_MENU_OPTION = 2
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
	from SelectedQuestionScreen import SelectedQuestionScreen
	from AnswerListScreen import AnswerListScreen

	search = SearchForQuestionsScreen
	select = SelectedQuestionScreen
	listAnswer = AnswerListScreen

	question = search.printScreen()
	if (SelectedQuestionScreen.printScreen(question) == 2):
		answer = listAnswer.printScreen(question)
		if (answer):
			SelectedAnswerScreen.print(answer)