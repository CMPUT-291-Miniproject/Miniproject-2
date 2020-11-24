import pymongo
import datetime
from Interface.Terminal import Terminal
class Vote:
	"""
	Vote is an Interface which allows the user to interact with posts
	
	Vote allows the user to upvote posts and handles database updating
	to represent that
	"""
	client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
	db = client[Terminal.getDBName()]
	def makeVote(post, userID=None):
		"""
		Provides the main functionality of Vote
		Creates a dictionary object representing a vote before inserting it
		into the vote collection. It then updates the post collections by increasing
		the number of votes on the given post

		Parameters:
			post:
				A Dictionary object representing the selected post from the database
			userID:
				A String object whose default value is none which represents the current
				users ID
		Returns:
			A Boolean object representing whether the vote was successfully added to the database
		"""
		postCollection = Vote.db['Posts']
		votesCollection = Vote.db['Votes']

		
		postID = post['Id']
		voteTypeID = '2'
		creationDate = str(datetime.datetime.utcnow().isoformat())
		
		if userID:
			if (not Vote.userVoted(votesCollection, post, userID)):
				voteID = Vote.getUniqueID(votesCollection)
				voteDict = {'Id' : voteID, 'PostId' : postID, 'VoteTypeId' : voteTypeID, 'UserId' : userID, 'CreationDate' : creationDate}
			else:
				print("You have already voted on this post!")
				input("Press Enter to Continue: ")
				return False
		else:
			voteID = Vote.getUniqueID(votesCollection)
			voteDict = {'Id' : voteID, 'PostId' : postID, 'VoteTypeId' : voteTypeID, 'CreationDate' : creationDate}
		
		votesCollection.insert_one(voteDict)
		Vote.updatePostVotes(post, postCollection)
		print("Vote Successfully added!")
		input("Press Enter to Continue: ")
		return True


	def getUniqueID(collection):
		"""
		Gets a unique ID for the vote being created by querying the database for all votes
		iterating to the last Dictionary object (representing a vote) grabbing it's id and incrementing
		by one

		Parameters:
			collection:
				A pymongo Collection Reference representing the current collection with which
				we are finding the unique ID for

		Returns:
			A String object representing a unique ID
		"""
		maxId = 0
		results = collection.find();
		for result in results:
			if int(result['Id']) > maxId:
				maxId = int(result['Id'])
		return str(maxId + 1)


	def userVoted(collection, post, userID):
		"""
		Checks if the current user has voted on this post

		Parameters:
			collection:
				A pymongo Collection Reference representing the current collection with which
				we are finding the unique ID for
			post:
				A Dictionary object representing a post currently being voted on
			userID:
				A String object representing the current user's ID

		Returns:
			A Boolean representing whether the current user has voted
		"""
		query = {'$and' : 
						[{ 'UserId' : userID},
						{ 'PostId' : post['Id']}] 
				}
		return collection.find_one(query) is not None

	def updatePostVotes(post, collection):
		updatedScore = post['Score'] + 1
		updateQuery = { '$set' : { 'Score' : updatedScore } }
		collection.update_one({'Id' : post['Id']}, updateQuery)

		
if __name__ == "__main__":
	from SearchForQuestionsScreen import SearchForQuestionsScreen
	from SelectedQuestionScreen import SelectedQuestionScreen
	from AnswerListScreen import AnswerListScreen as listAnswer
	from SelectedAnswerScreen import SelectedAnswerScreen as selectedAnswer

	search = SearchForQuestionsScreen
	select = SelectedQuestionScreen



	post = search.printScreen()
	selected = select.printScreen(post)

	if (selected == 3):
		Vote.makeVote(post, '50')
	if (selected == 2):
		answer = listAnswer.printScreen(post)
		if (answer):
			selected = selectedAnswer.printScreen(answer)
			if selected == 1:
				Vote.makeVote(answer)
				Vote.makeVote(answer, 50)
				Vote.makeVote(answer, 50) 


