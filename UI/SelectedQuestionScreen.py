from Terminal import Terminal

class SelectedQuestionScreen:

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

	def printMenu():
		menuOptions = ["Answer Question","List Answers","Vote","Exit"]
		for i,option in enumerate(menuOptions):
			print(str(i+1) + ". " + option)

	def printScreen(post):
		MAX_MENU_OPTION = 5
		MIN_MENU_OPTION = 1
		invalidInput = True
		while invalidInput:
			SelectedQuestionScreen.printTitle(post)
			SelectedQuestionScreen.printMenu()
			userInput = input("Select Option: ")

			if userInput.upper() == "EXIT" or userInput.upper() == "QUIT":
				return None

			try:
				int(userInput)
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