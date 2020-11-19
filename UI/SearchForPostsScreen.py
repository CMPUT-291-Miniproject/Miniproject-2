import pymongo
import multiprocessing
from Interface.Terminal import Terminal

class SearchForQuestionsScreen:
	"""
	A screen which handles searching for posts and the processes
	associated with it.

	This module is responsible for providing the UI of the post
	search screen
	"""

	def printTitleKeyword(self):
		"""
		Prints identifying information telling the user what screen
		they are on and information about how to give keywords
		"""
		self.__terminal__.clear()
		self.__terminal__.printCenter("Search for Posts")
		self.__terminal__.printCenter("Enter terms delimited by commas")
		
	def getParsedKeywords(self):
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

class SearchForQuestions:
	def getQuestions(searchKeys):
		searchTypes = [[],[],[]]

		titleProcess = multiprocessing.Process(target = SearchForQuestions.getMatchingTitle, args = (searchKeys, searchTypes[0]))
		bodyProcess = multiprocessing.Process(target = SearchForQuestions.getMatchingBody, args = (searchKeys, searchTypes[1]))
		tagProcess = multiprocessing.Process(target = SearchForQuestions.getMatchingTag, args = (searchKeys, searchTypes[2]))

		processes = [titleProcess, bodyProcess, tagProcess]
		for process in processes:
			process.start()
		for process in processes:
			process.join()

		seen = []
		posts = []
		for searchType in searchTypes:
			print(searchType)
			for post in searchType:
				print(post['Id'])
				if post['Id'] not in seen:
					seen.append(post['Id'])
					posts.append(post)
		return seen

	def getMatchingTitle(searchKeys, posts):
		postsMatchingTitle = []
		db = SearchForQuestions.connectToDB()
		collection = db["Posts"]

		for keyWord in searchKeys:
			searchQuery = 	{'$and' : 
						[ { 'Title' : { '$regex' : keyWord, '$options' : 'i' }},
						{ 'PostTypeId' : '1'} ]
					}

			queryResults = collection.find(searchQuery)
			for result in queryResults:
				posts.append(result)
		print(post[0])

	def getMatchingBody(searchKeys, posts):
		postsMatchingBody = []
		db = SearchForQuestions.connectToDB()
		collection = db["Posts"]

		for keyWord in searchKeys:
			searchQuery = 	{'$and' : 
						[ { 'Body' : { '$regex' : keyWord, '$options' : 'i' }},
						{ 'PostTypeId' : '1'} ]
					}

			queryResults = collection.find(searchQuery)
			for result in queryResults:
				posts.append(result)
		print(posts[0])

	def getMatchingTag(searchKeys, posts):
		postsMatchingTag = []
		db = SearchForQuestions.connectToDB()
		collection = db["Posts"]

		for keyWord in searchKeys:
			searchQuery = 	{'$and' : 
						[ { 'Tags' : { '$regex' : keyWord, '$options' : 'i' }},
						{ 'PostTypeId' : '1'} ]
					}

			queryResults = collection.find(searchQuery)
			for result in queryResults:
				posts.append(result)
		print(posts[0])

	def connectToDB():
		client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
		db = client[Terminal.getDBName()]
		return db
			


			
if __name__ == "__main__":
	#SearchForQuestions.getMatchingTitle(['What'])
	#SearchForQuestions.getMatchingBody(['The'])
	#SearchForQuestions.getMatchingTag(['mac'])

	print(SearchForQuestions.getQuestions(['I have Google Chrome']))
