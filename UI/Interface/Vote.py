import mongopy
import datetime
from Terminal import Terminal
class Vote:
	client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
	db = client[Terminal.getDBName()]

	def makeVote(userID=None, post):
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
		result = collection.find_one(sort=["Id",-1])
		print(result)

if __name__ == "__main__":
	import 

