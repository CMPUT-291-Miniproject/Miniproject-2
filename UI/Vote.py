import pymongo
import datetime
from Terminal import Terminal
class Vote:
	client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
	db = client[Terminal.getDBName()]

	def makeVote(post, userID=None):
		postCollection = Vote.db['Posts']
		votesCollection = Vote.db['Votes']

		voteID = Vote.getUniqueID(votesCollection)
		postID = post['Id']
		voteTypeId = '2'
		creationDate = str(datetime.datetime.utcnow().isoformat())
		
		if userID:
			voteDict = {voteID, postID, voteTypeID, userID, creationDate}
			print(voteDict)
		else:
			voteDict = {voteID, postID, voteTypeId, creationDate}
			print(voteDict)


	def getUniqueID(collection):
		result = collection.find().sort([('Id', -1)]).limit(1)
		print(result['Id'])
		
if __name__ == "__main__":
	from SearchForQuestionsScreen import SearchForQuestionsScreen
	from SelectedQuestionScreen import SelectedQuestionScreen

	search = SearchForQuestionsScreen
	select = SelectedQuestionScreen

	post = search.printScreen()
	if (select.printScreen(post) == 3):
		Vote.makeVote(post)

