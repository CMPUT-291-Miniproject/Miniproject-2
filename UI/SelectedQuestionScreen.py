from Terminal import Terminal

class SelectedQuestionScreen:

	def printTitle(post):
		Terminal.clear()
		usedKeys = ["Id", "Title", "Body", "Tags", "Score", 
					"ViewCount", "CommentCount", "AnswerCount", 
					"FavoriteCount", "CreationDate", "LastEditDate",
					"ContentLicense"]

		Terminal.printCenter("----------Post----------")
		for key in usedKeys:
			if (key in post):
				if key == "Score":
					Terminal.printCenter("----------Post Info-----------")
				if key == "CreationDate":
					Terminal.printCenter("----------Post Date Info----------")
				Terminal.printCenter(key + ": " + str(post[key]) + "\n")

		Terminal.printCenter("\n\nMisc Info:\n")
		for key in post:
			if (key is not None and key not in usedKeys and key != "_id"):
				Terminal.printCenter(str(key) + ": " + str(post[key]) + "\n\n")

	def printScreen(post):
		SelectedQuestionScreen.printTitle(post)


if __name__ == "__main__":
	from SearchForQuestionsScreen import SearchForQuestionsScreen

	sScreen = SearchForQuestionsScreen
	post = sScreen.printScreen()
	SelectedQuestionScreen.printScreen(post)