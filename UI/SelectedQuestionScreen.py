from Terminal import Terminal

class SelectedQuestionScreen:

	def printTitle(post):
		Terminal.clear
		for key in post:
			if (key is not None):
				Terminal.printCenter(key + ": " + post[key] + "\n\n")

	def printScreen(post):
		SelectedQuestionScreen.printTitle(post)


if __name__ == "__main__":
	from SearchForQuestionsScreen import SearchForQuestionsScreen

	sScreen = SearchForQuestionsScreen
	post = sScreen.printScreen()
	SelectedQuestionScreen.printScreen(post)