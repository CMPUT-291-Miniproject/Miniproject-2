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
		"""
		calls various methods to inform the user of what they need to do
		and collect key words from the user for searching 

		Returns:
			A List of String objects representing search terms
		"""
		SearchForQuestionsScreen.printTitleKeyword()
		searchKeys = SearchForQuestionsScreen.getParsedKeywords()
		return SearchForQuestions.getQuestions(searchKeys)

	def printScreenMenu(posts):
		"""
		Instantiates a SearchQuestionMenu object using posts
		returns from the search and calls it's method to print
		the menu

		Parameters:
			posts:
				A Dictionary object of dictionary objects representing posts
				from the database 
		Returns:
			A Dictionary object representing the post selected by the user from
			the menu
		"""
		searchQuestionMenu = SearchQuestionMenu(posts)
		post = searchQuestionMenu.printScreen()
		return post

	def printScreen():
		"""
		Provides the main functionality of SearchForQuestionsScreen
		by calling various methods

		Returns:
			A Dictionay object representing the post selected by the user
		"""
		posts = SearchForQuestionsScreen.printScreenKeyword()
		post = SearchForQuestionsScreen.printScreenMenu(posts)
		return post

class SearchQuestionMenu():
	"""
	SearchQuestionMenu is a Menu object

	SearchQuestionMenu displays posts and allows
	the user to select one of them
	"""
	POSTS_PER_PAGE = 100

	def __init__(self, posts):
		"""
		Instantiates a SearchQuestionMenu object

		Parameters:
			posts:
				A Dictionary object representing various posts from the database
		Returns:
			An instance of SearchQuestionMenu
		"""
		self.__menuItems__ = []
		self.fillMenu(posts)

	def fillMenu(self, posts):
		"""
		Fills SearchQuestionMenu's List with Named Tuple objects representing posts from the database
		"""
		for key in posts:
			if key is not None:
				self.__menuItems__.append(SearchForQuestionsScreen.MenuOption(PostID=key, Post=posts[key]))

	def printPost(self, item, index):
		"""
		Formats and prints a post

		Parameters:
			item:
				A Named Tuple object representing a post from the database
			index:
				An Integer object representing the index which the Named Tuple is at
				in SearchQuestionMenu's List
		"""
		stringToPrint = ""

		stringToPrint += str(index+1) + ". "
		stringToPrint += item.Post['Title'] + " " + "|"
		stringToPrint += item.Post['CreationDate'] + "|"
		stringToPrint += str(item.Post['Score']) + "   |"
		stringToPrint += str(item.Post['AnswerCount']) + "\n"

		print(stringToPrint)

	def printMenu(self, index):
		"""
		Prints 100 posts from SearchQuestionMenu's list

		Parameters:
			index:
				An Integer used as a pointed to point to the first of the next
				100 posts to be printed
		"""
		if index + SearchQuestionMenu.POSTS_PER_PAGE > len(self.__menuItems__[index:]):
			for  i,item in enumerate(self.__menuItems__[index:]):
				self.printPost(item, i)
		else:
			for i in range (SearchQuestionMenu.POSTS_PER_PAGE):
				self.printPost(self.__menuItems__[i+index], i)

	def printScreen(self):
		"""
		Provides the main functionality of SearchQuestionMenu
		Prints various posts and prompts the user for input
		checks said input before returning the post selected

		Returns:
			A Dictionary object representing a post from the database
		"""
		continueRunning = True
		index = 0
		while continueRunning:
			self.printMenu(index)
			userInput = input("Enter Selection: ")
			if userInput.upper() == "EXIT" or userInput.upper() == "QUIT":
				return None
			elif userInput.upper() == "NEXT":
				if index + SearchQuestionMenu.POSTS_PER_PAGE < len(self.__menuItems__):
					index += SearchQuestionMenu.POSTS_PER_PAGE
				else:
					print("You are currently on the last page!")
					input("Type Enter to Continue: ")
			elif userInput.upper() == "PREV":
				if index >= SearchQuestionMenu.POSTS_PER_PAGE:
					index +=  SearchQuestionMenu.POSTS_PER_PAGE
				else:
					print("You are currently on the first page!")
					input("Press Enter to Continue: ")
			else:
				try:
					userInput = int(userInput)
					if (userInput < 1 or userInput > SearchQuestionMenu.POSTS_PER_PAGE or userInput > len(self.__menuItems__[index:])):
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
	"""
	SearchForQuestions serves as an interface between SearchForQuestionsScreen
	and the database

	SearchForQuestions allows SearchForQuestionsScreen to query the database through
	it's methods
	"""
	client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
	db = client[Terminal.getDBName()]

	def getQuestions(searchKeys):
		"""
		getQuestions fetches any posts matching the searchKeys
		by calling various methods

		Parameters:
			searchKeys:
				A List of String objects representing search terms entered by
				the user
		Returns:
			A Dictionary object of dictionaries representing posts that match the search
			terms
		"""
		posts = {}
		posts = SearchForQuestions.getMatchingTitle(searchKeys, posts)
		posts = SearchForQuestions.getMatchingBody(searchKeys, posts)
		posts = SearchForQuestions.getMatchingTag(searchKeys, posts)
		return posts

	def getMatchingTitle(searchKeys, posts):
		"""
		Fetches any posts whose title matches one of the
		searchTerms

		Parameters:
			searchKeys:
				A List of String objects representing search terms entered by
				the user
			posts:
				A Dictionary object of Dictionaries to append any posts
				retrieved through the query
		Returns:
			A Dictionary object of dictionaries representing posts that match the search
		"""
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
		"""
		Fetches any posts whose body matches one of the searchTerms

		Parameters:
			searchKeys:
				A List of String objects representing search terms entered by
				the user
			posts: A Dictionary object of dictionaries representing posts that match the search
			terms

		Returns:
			A Dictionary object of dictionaries representing posts that match the search
			terms
		"""
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
		"""
		Fetches any posts whose tags match one of the searchTerms

		Parameters:
			searchKeys:
				A List of String objects representing search terms entered by
				the user
			posts: A Dictionary object of dictionaries representing posts that match the search
			terms

		Returns:
			A Dictionary object of dictionaries representing posts that match the search
			terms
		"""
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
