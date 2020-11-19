from Terminal import Terminal

class SelectedQuestionScreen:

	def __init__(self, post):
		self.__post__ = post

	def printTitle(self):
		Terminal.clear()
		for key in self.__post__:
			if (key is not None):
				Terminal.printCenter(key + ": " + self.__post__[key] + "\n\n")

	def printScreen(self):
		SelectedQuestionScreen()


if __name__ == "__main__":
	from SearchForQuestionsScreen import SearchForQuestionsScreen

	sScreen = SearchForQuestionsScreen
	post = sScreen.printScreen()
	SelectedQuestionScreen.printScreen(post)