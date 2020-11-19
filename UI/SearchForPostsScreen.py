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
		searchQuestionMenu.printScreen()

	def printScreen():
		posts = SearchForQuestionsScreen.printScreenKeyword()
		SearchForQuestionsScreen.printScreenMenu(posts)


class SearchQuestionMenu():
	def __init__(self, posts):
		self.__menuItems__ = []
		#self.__maxTitleLength__ == self.getMaxTitleLength()	Might make list look better to align
		self.fillMenu(posts)

	def fillMenu(self, posts):
		for key in posts:
			if key is not None:
				self.__menuItems__.append(SearchForQuestionsScreen.MenuOption(PostID=key, Post=posts[key]))

	def printScreen(self):
		for i,item in enumerate(self.__menuItems__):
			print(str(i) + ". " + item.Post['Title'] + "|" + item.Post['CreationDate'] + "|" + str(item.Post['Score']) + "|" + str(item.Post['AnswerCount']))
		input("Enter selection: ")

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
	s = SearchForQuestions
	#SearchForQuestions.getMatchingTitle(['What'])
	#SearchForQuestions.getMatchingBody(['The'])
	#SearchForQuestions.getMatchingTag(['mac'])
	#sScreen.printTitleKeyword()
	#searchWords = sScreen.getParsedKeywords()
	#print(SearchForQuestions.getQuestions(searchWords))
	sScreen.printScreen()
