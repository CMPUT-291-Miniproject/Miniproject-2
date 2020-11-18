
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
		
import os.path
import json
class FileManager:
	READ_CONSTANT = "r"	
	
	def readJsonFile(fileName):
		directory = os.path.dirname(__file__) + "/../../" + fileName		#Directory where file is contained

		if os.path.splitext(directory)[1] != ".json":				#Raise error if file is of wrong type
			raise ValueError("Wrong File Type")

		managedFile = open(directory, FileManager.READ_CONSTANT)		#Open file or throw exception if file does not exist
		fileContent = json.loads(managedFile.read())					#
		return fileContent

if __name__ == "__main__":
	try:
		invalid = FileManager.readJsonFile("Tag.txt")
	except ValueError as e:
		print(e)
	jsonDict = FileManager.readJsonFile("Tags.json")
	for row in jsonDict["tags"]["row"]:
		print(row)

if __name__ == "__main__":
	c = CollectionGenerator
	c.generateCollections()
