import pymongo
import datetime
from Terminal import Terminal
class Vote:
	client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
	db = client[Terminal.getDBName()]
	#BUG VOTETYPEID IS NOT DEFINED STILL NEED TO INSERT AFTER FINISH
	def makeVote(post, userID=None):
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
				return False
		else:
			voteID = Vote.getUniqueID(votesCollection)
			voteDict = {'Id' : voteID, 'PostId' : postID, 'VoteTypeId' : voteTypeID, 'CreationDate' : creationDate}
		
		votesCollection.insert_one(voteDict)
		Vote.updatePostVotes(post, postCollection)
		return True


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
		return collection.find_one(query) is not None

	def updatePostVotes(post, collection):
		updatedScore = post['Score'] + 1
		updateQuery = { '$set' : { 'Score' : updatedScore } }
		collection.update_one(selectedPost.Post, updateQuery)

		
if __name__ == "__main__":
	from SearchForQuestionsScreen import SearchForQuestionsScreen
	from SelectedQuestionScreen import SelectedQuestionScreen

	search = SearchForQuestionsScreen
	select = SelectedQuestionScreen

	post = search.printScreen()
	if (select.printScreen(post) == 3):
		Vote.makeVote(post, '50')

