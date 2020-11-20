from Terminal import Terminal

class SelectedQuestionScreen:

	def printKeyTitle(key):
		if key == "Title" or key == "Body":
			string = "----------" + key + "----------" + "\n\n"
			Terminal.printCenter(string)
		if key == "Score":
			string = "----------" + "Post Data" + "----------" + "\n\n"
			Terminal.printCenter(string)
		if key == "CreationDate":
			string = "----------" + "Dates" + "----------" + "\n\n"
			Terminal.printCenter(string)
		

	def printTitle(post):
		Terminal.clear()
		usedKeys = ["Id", "Title", "Body", "Tags", "Score", 
					"ViewCount", "CommentCount", "AnswerCount", 
					"FavoriteCount", "CreationDate", "LastEditDate",
					"ContentLicense"]

		Terminal.printCenter("----------Post----------")
		for key in usedKeys:
			if (key in post):
				SelectedQuestionScreen.printKeyTitle(key)
				Terminal.printCenter(key + ": " + str(post[key]) + "\n")

		Terminal.printCenter("----------Misc Info----------")
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