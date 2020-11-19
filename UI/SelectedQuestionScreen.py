from Terminal import Terminal

class SelectedQuestionScreen:

	def printTitle(post):
		for key in post:
			if (key is not None):
				Terminal.printCenter(key + ": " + post[key] + "\n\n")

	def printScreen(post):
		SelectedQuestionScreen(post)


if __name__ == "__main__":
	from SearchForPostsScreen import SearchForPostsScreen

	sScreen = SearchForQuestionsScreen
	post = sScreen.printScreen()
	SelectedQuestionScreen.printScreen(post)