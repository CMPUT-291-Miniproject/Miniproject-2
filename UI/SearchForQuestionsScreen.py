import pymongo
from Terminal import Terminal
import collections

class SearchForQuestionsScreen:
	"""
	A screen which handles searching for posts and the processes
	associated with it.

	This module is responsible for providing the UI of the post
	search screen
	"""

	MenuOption = collections.namedtuple('Post', 'PostID Post' )

	def printTitleKeyword():
		"""
		Prints identifying information telling the user what screen
		they are on and information about how to give keywords
		"""
		Terminal.clear()
		Terminal.printCenter("Search for Posts")
		Terminal.printCenter("Enter terms delimited by commas")
	
	def getParsedKeywords():
		"""
		Gets input from user and parses it
		into a list of terms that can be used to query the database

		Returns:
			A List of strings that can be used to query the database
		"""
		userInput = input("Enter search term(s): ")
		searchTermList = userInput.split(",")
		for i, string in enumerate(searchTermList):
			searchTermList[i] = string.strip()
		return searchTermList
	
	def printScreenKeyword():
		SearchForQuestionsScreen.printTitleKeyword()
		searchKeys = SearchForQuestionsScreen.getParsedKeywords()
		return SearchForQuestions.getQuestions(searchKeys)

	def printTitleMenu():
		Terminal.printCenter("ENTER ACTUAL TEXT LATER")

	def printScreenMenu(posts):
		searchQuestionMenu = SearchQuestionMenu(posts)
		post = searchQuestionMenu.printScreen()
		return post

	def printScreen():
		posts = SearchForQuestionsScreen.printScreenKeyword()
		post = SearchForQuestionsScreen.printScreenMenu(posts)
		return post

class SearchQuestionMenu():
	POSTS_PER_PAGE = 100

	def __init__(self, posts):
		self.__menuItems__ = []
		self.fillMenu(posts)

	def fillMenu(self, posts):
		for key in posts:
			if key is not None:
				self.__menuItems__.append(SearchForQuestionsScreen.MenuOption(PostID=key, Post=posts[key]))

	def printPost(self, item, index):
		stringToPrint = ""

		stringToPrint += str(index+1) + ". "
		stringToPrint += item.Post['Title'] + " " + "|"
		stringToPrint += item.Post['CreationDate'] + "|"
		stringToPrint += str(item.Post['Score']) + "   |"
		stringToPrint += str(item.Post['AnswerCount']) + "\n"

		print(stringToPrint)

	def printMenu(self, index):
		if index + POSTS_PER_PAGE > len(self.__menuItems__[index:]):
			for  i,item in enumerate(self.__menuItems__[index:]):
				self.printPost(item, i)
		else:
			for i in range POSTS_PER_PAGE):
				self.printPost(self.__menuItems__[i+index], i)

	def printScreen(self):
		continueRunning = True
		index = 0
		while continueRunning:
			self.printMenu(index)
			userInput = input("Enter Selection: ")
			if userInput.upper() == "EXIT" or userInput.upper() == "QUIT":
				return None
			elif userInput.upper() == "NEXT":
				if index + POSTS_PER_PAGE < len(self.__menuItems__):
					index += POSTS_PER_PAGE
				else:
					print("You are currently on the last page!")
					input("Type Enter to Continue: ")
			elif userInput.upper() == "PREV":
				if index >= POSTS_PER_PAGE:
					index +=  POSTS_PER_PAGE
				else:
					print("You are currently on the first page!")
					input("Press Enter to Continue: ")
			else:
				try:
					userInput = int(userInput)
					if (userInput < 1 or userInput > POSTS_PER_PAGE or userInput > len(self.__menuItems__[index:])):
						print("Input is out of range")
					else:
						continueRunning = False
				except Exception:
					print("Entered input is invalid!")
				finally:
					input("Press Enter to Continue: ")



		userInput += -1 + index

		selectedPost = self.__menuItems__[userInput]

		client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
		db = client[Terminal.getDBName()]
		collection = SearchForQuestions.db["Posts"]

		updatedViewCount = selectedPost.Post['ViewCount'] + 1
		updateQuery = { '$set' : { 'ViewCount' : updatedViewCount } }

		collection.update_one(selectedPost.Post, updateQuery)


		return selectedPost.Post
		

class SearchForQuestions:
	client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
	db = client[Terminal.getDBName()]

	def getQuestions(searchKeys):
		posts = {}
		posts = SearchForQuestions.getMatchingTitle(searchKeys, posts)
		posts = SearchForQuestions.getMatchingBody(searchKeys, posts)
		posts = SearchForQuestions.getMatchingTag(searchKeys, posts)
		return posts

	def getMatchingTitle(searchKeys, posts):
		collection = SearchForQuestions.db["Posts"]

		for keyWord in searchKeys:
			searchQuery = 	{'$and' : 
						[ { 'Title' : { '$regex' : keyWord, '$options' : 'i' }},
						{ 'PostTypeId' : '1'} ]
					}

			queryResults = collection.find(searchQuery)
			for result in queryResults:
				posts[result['Id']] = result

		return posts

	def getMatchingBody(searchKeys, posts):
		collection = SearchForQuestions.db["Posts"]

		for keyWord in searchKeys:
			searchQuery = 	{'$and' : 
						[ { 'Body' : { '$regex' : keyWord, '$options' : 'i' }},
						{ 'PostTypeId' : '1'} ]
					}

			queryResults = collection.find(searchQuery)
			for result in queryResults:
				posts[result['Id']] = result
		
		return posts

	def getMatchingTag(searchKeys, posts):
		collection = SearchForQuestions.db["Posts"]

		for keyWord in searchKeys:
			searchQuery = 	{'$and' : 
						[ { 'Tags' : { '$regex' : keyWord, '$options' : 'i' }},
						{ 'PostTypeId' : '1'} ]
					}

			queryResults = collection.find(searchQuery)
			for result in queryResults:
				posts[result['Id']] = result

		return posts




			
if __name__ == "__main__":
	sScreen = SearchForQuestionsScreen
	#s = SearchForQuestions
	#SearchForQuestions.getMatchingTitle(['What'])
	#SearchForQuestions.getMatchingBody(['The'])
	#SearchForQuestions.getMatchingTag(['mac'])
	#sScreen.printTitleKeyword()
	#searchWords = sScreen.getParsedKeywords()
	#print(SearchForQuestions.getQuestions(searchWords))
	sScreen.printScreen()
