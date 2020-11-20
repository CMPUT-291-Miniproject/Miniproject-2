import Terminal from Terminal

class PostPrinter:

	def printKeyTitle(key):
			if key == "Title" or key == "Body" or key == "Tags":
				string = "----------" + key + "----------" + "\n"
				Terminal.printCenter(string)
			if key == "Score":
				string = "----------" + "Post Data" + "----------" + "\n"
				Terminal.printCenter(string)
			if key == "CreationDate":
				string = "----------" + "Dates" + "----------" + "\n"
				Terminal.printCenter(string)
			
	def printTitle(post):
		Terminal.clear()
		usedKeys = ["Id", "Title", "Body", "Tags", "Score", 
					"ViewCount", "CommentCount", "AnswerCount", 
					"FavoriteCount", "ContentLicense","CreationDate", 
					"LastEditDate"]

		Terminal.printCenter("----------Post----------")
		for key in usedKeys:
			if (key in post):
				SelectedQuestionScreen.printKeyTitle(key)
				Terminal.printCenter(key + ": " + str(post[key]) + "\n")

		Terminal.printCenter("----------Misc Info----------")
		for key in post:
			if (key is not None and key not in usedKeys and key != "_id"):
				Terminal.printCenter(str(key) + ": " + str(post[key]) + "\n")