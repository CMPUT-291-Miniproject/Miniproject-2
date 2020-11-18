
from File.FileManager import FileManager
from Terminal import Terminal

import pymongo


class CollectionGenerator:
	
	client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
	db = client['291db']
	
	def generateCollections():
		CollectionGenerator.generateTagCollection()
		CollectionGenerator.generatePostCollection()
		CollectionGenerator.generateVoteCollection()


	def generateTagCollection():
		tagDict = FileManager.readJsonFile("Tags.json")
		CollectionGenerator.dictToCollection(tagDict, "Tags")

	def generatePostCollection():
		postDict = FileManager.readJsonFile("Posts.json")
		CollectionGenerator.dictToCollection(postDict, "Posts")

	def generateVoteCollection():
		voteDict = FileManager.readJsonFile("Votes.json")
		CollectionGenerator.dictToCollection(voteDict, "Votes")

	def dictToCollection(dictionary, name):
		collection = CollectionGenerator.db[name]
		collection.delete_many({})
		batchInsert = []
		for row in dictionary[name.lower()]["row"]:
			batchInsert.append(row)
		
		collection.insert_many(batchInsert)
			

if __name__ == "__main__":
	c = CollectionGenerator
	c.generateCollections()
