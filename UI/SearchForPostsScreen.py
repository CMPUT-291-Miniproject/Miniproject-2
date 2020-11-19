import pymongo
import threading
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
	client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
	db = client[Terminal.getDBName()]

	def getQuestions(searchKeys):
		posts = [None]*3

		titleThread = threading.Thread(target = SearchForQuestions.getMatchingTitle(searchKeys), args = (posts))
		bodyThread = threading.Thread(target = SearchForQuestions.getMatchingBody(searchKeys), args = (posts))
		tagThread = threading.Thread(target = SearchForQuestions.getMatchingTag(searchKeys), args = (posts))
(target=foo, args=('world!', results, i))
		threads = [titleThread, bodyThread, tagThread]
		for thread in threads:
			thread.start()
		for thread in threads:
			thread.join()

		seen = []
		posts = []
		for post in postsMatchingTitle:
			print(post['Id'])
			if post['Id'] not in seen:
				seen.append(post['Id'])
				posts.append(post)
		for post in postsMatchingBody:
			print(post['Id'])
			if post['Id'] not in seen:
				seen.append(post['Id'])
				posts.append(post)
		for post in postsMatchingTag:
			print(post['Id'])
			if post['Id'] not in seen:
				seen.append(post['Id'])
				posts.append(post)
		return seen

	def getMatchingTitle(searchKeys):
		postsMatchingTitle = []
		collection = SearchForQuestions.db["Posts"]

		for keyWord in searchKeys:
			searchQuery = 	{'$and' : 
						[ { 'Title' : { '$regex' : keyWord, '$options' : 'i' }},
						{ 'PostTypeId' : '1'} ]
					}

			queryResults = collection.find(searchQuery)
			for result in queryResults:
				postsMatchingTitle.append(result)

		post[0] = postsMatchingTitle

	def getMatchingBody(searchKeys):
		postsMatchingBody = []
		collection = SearchForQuestions.db["Posts"]

		for keyWord in searchKeys:
			searchQuery = 	{'$and' : 
						[ { 'Body' : { '$regex' : keyWord, '$options' : 'i' }},
						{ 'PostTypeId' : '1'} ]
					}

			queryResults = collection.find(searchQuery)
			for result in queryResults:
				postsMatchingBody.append(result)
		
		post[1] = postsMatchingBody

	def getMatchingTag(searchKeys, posts):
		postsMatchingTag = []
		collection = SearchForQuestions.db["Posts"]

		for keyWord in searchKeys:
			searchQuery = 	{'$and' : 
						[ { 'Tags' : { '$regex' : keyWord, '$options' : 'i' }},
						{ 'PostTypeId' : '1'} ]
					}

			queryResults = collection.find(searchQuery)
			for result in queryResults:
				postsMatchingTag.append(result)

		posts[2] = postsMatchingTag
			


			
if __name__ == "__main__":
	#SearchForQuestions.getMatchingTitle(['What'])
	#SearchForQuestions.getMatchingBody(['The'])
	#SearchForQuestions.getMatchingTag(['mac'])

	print(SearchForQuestions.getQuestions(['I have Google Chrome']))
