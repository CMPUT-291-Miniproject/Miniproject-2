from Interface.Terminal import Terminal

class PostPrinter:
	"""
	PostPrinter is a module used to display posts

	PostPrinter takes a Dictionary object post and prints all of the keys it has in a
	formatted fashion
	"""
	def printKeyTitle(key):
		"""
		printKeyTitle prints a sort of descriptor for subcategories of the post
		delimited as Title, Body, Tags, Post Data (ViewCount, CommentCount, Score, etc.), 
		Dates (Creation, Edited, etc.)

		Parameters:
			key:
				A String object representing a key of the dictionary
		"""
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
		"""
		Prints the post in a formatted fashion

		Parameters:
			post:
				A dictionary object representing a post retrieved from the database

		"""
		Terminal.clear()
		usedKeys = ["Id", "Title", "Body", "Tags", "Score", 
					"ViewCount", "CommentCount", "AnswerCount", 
					"FavoriteCount", "ContentLicense","CreationDate", 
					"LastEditDate"]

		Terminal.printCenter("----------Post----------")
		for key in usedKeys:
			if (key in post):
				PostPrinter.printKeyTitle(key)
				Terminal.printCenter(key + ": " + str(post[key]) + "\n")

		Terminal.printCenter("----------Misc Info----------")
		for key in post:
			if (key is not None and key not in usedKeys and key != "_id"):
				Terminal.printCenter(str(key) + ": " + str(post[key]) + "\n")