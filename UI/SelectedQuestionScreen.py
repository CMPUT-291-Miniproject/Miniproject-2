from Terminal import Terminal

class SelectedQuestionScreen:

	def printTitle(post):
		Terminal.clear()
		usedKeys = ["Id", "Title", "Body", "Tags", "Score", 
					"CommentCount", "AnswerCount", "FavoriteCount"] 

		for key in usedKeys:
			if (key in post):
				Terminal.printCenter(key + ": " + str(post[key]) + "\n")

		Terminal.printCenter("\n\nMisc Info:\n")
		for key in post:
			if (key is not None and key not in usedKeys):
				Terminal.printCenter(str(key) + ": " + str(post[key]) + "\n\n")

	def printScreen(post):
		SelectedQuestionScreen.printTitle(post)


if __name__ == "__main__":
	from SearchForQuestionsScreen import SearchForQuestionsScreen

	sScreen = SearchForQuestionsScreen
	post = sScreen.printScreen()
	SelectedQuestionScreen.printScreen(post)