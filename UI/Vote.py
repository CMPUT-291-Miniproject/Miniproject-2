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
		voteTypeId = '2'
		creationDate = str(datetime.datetime.utcnow().isoformat())
		
		if userID:
			if (not Vote.userVoted(votesCollection, post, userID)):
				voteID = Vote.otherGetId(votesCollection)
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

	def otherGetId(collection):
		min,max = Vote.getMaxMin()
		while min <= max-1:
			mid = (max + min)//2
			if collection.find_one({'Id' : str(mid)}) is None:
				max = mid
			else:
				min = mid

		return max



	def getMaxMin(collection):
    	maxNum = 1
    	minNum = 1
    	while  collection.find_one({'Id': str(maxNum)}) is not None:
        	minNum = maxNum
        	maxNum *= 2
        return (minNum, maxNum)
    
    return [minNum, maxNum

	def userVoted(collection, post, userID):
		query = {'$and' : 
						[{ 'UserId' : userID},
						{ 'PostId' : post['Id']}] 
				}
		return collection.find_one(query) is not None

		
if __name__ == "__main__":
	from SearchForQuestionsScreen import SearchForQuestionsScreen
	from SelectedQuestionScreen import SelectedQuestionScreen

	search = SearchForQuestionsScreen
	select = SelectedQuestionScreen

	post = search.printScreen()
	if (select.printScreen(post) == 3):
		Vote.makeVote(post, '50')

