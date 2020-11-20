import pymongo
import datetime
from Terminal import Terminal
class Vote:
	client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
	db = client[Terminal.getDBName()]

	def makeVote(post, userID=None):
		postCollection = Vote.db['Posts']
		votesCollection = Vote.db['Votes']

		
		postID = post['Id']
		voteTypeId = '2'
		creationDate = str(datetime.datetime.utcnow().isoformat())
		
		if userID:
			if (Vote.userVoted(votesCollection, post, userID)):
				return False
			voteID = Vote.getUniqueID(votesCollection)
			voteDict = {voteID, postID, voteTypeID, userID, creationDate}
			print(voteDict)
		else:
			voteID = Vote.getUniqueID(votesCollection)
			voteDict = {voteID, postID, voteTypeId, creationDate}
			print(voteDict)


	def getUniqueID(collection):
		maxId = 0
		results = collection.find();
		for result in results:
			if int(result['Id']) > maxId:
				maxId = int(result['Id'])
		return str(maxId + 1)

	def userVoted(collection, post, userID):
		query = {'$and' : 
						[{ 'UserId' : userID},
						{ 'PostId' : post['Id']}] 
				}
		return collection.find_one(query).count() == 1

		
if __name__ == "__main__":
	from SearchForQuestionsScreen import SearchForQuestionsScreen
	from SelectedQuestionScreen import SelectedQuestionScreen

	search = SearchForQuestionsScreen
	select = SelectedQuestionScreen

	post = search.printScreen()
	if (select.printScreen(post) == 3):
		Vote.makeVote(post)

