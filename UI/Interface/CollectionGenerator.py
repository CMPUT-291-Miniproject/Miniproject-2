from Terminal import Terminal

import os.path
import json
import pymongo

class CollectionGenerator:
	"""
	Collection Generator is a module which creates mongo db collections

	Collection Generator creates three mongo db collections from files located in 
	the main directory.
	"""
	
	client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
	db = client['291db']
	
	def generateCollections():
		"""
		Generates the three collections by calling various methods
		"""
		CollectionGenerator.generateTagCollection()
		CollectionGenerator.generatePostCollection()
		CollectionGenerator.generateVoteCollection()

	def generateTagCollection():
		"""
		Generates the Tags collection by reading Tags.json to get a Dictionary
		object and calls a method which turns the dictionary into a mongo db collection
		"""
		tagDict = FileManager.readJsonFile("Tags.json")
		CollectionGenerator.dictToCollection(tagDict, "Tags")

	def generatePostCollection():
		"""
		Generates the Posts collection by reading Posts.json to get a Dictionary
		object and calls a method which turns the dictionary into a mongo db collection
		"""
		postDict = FileManager.readJsonFile("Posts.json")
		CollectionGenerator.dictToCollection(postDict, "Posts")

	def generateVoteCollection():
		"""
		Generates the Votes collection by reading Votes.json to get a Dictionary
		object and calls a method which turns the dictionary into a mongo db collection
		"""
		voteDict = FileManager.readJsonFile("Votes.json")
		CollectionGenerator.dictToCollection(voteDict, "Votes")

	def dictToCollection(dictionary, name):
		"""
		Creates a collection from name, empties it then appends all
		of the dictionaries entries (which are dictionaries themselves)
		to a list before inserting all of them into the created collection

		Parameters:
			dictionary:
				A Dictionary object retrieved from one of the three json files
			name:
				A String object representing the name of the collection 
		"""
		collection = CollectionGenerator.db[name]
		collection.delete_many({})
		batchInsert = []
		for row in dictionary[name.lower()]["row"]:
			batchInsert.append(row)
		
		collection.insert_many(batchInsert)
		

class FileManager:
	"""
	FileManager allows for the reading of files

	FileManager reads json files and returns their contents as a Dictionary object
	"""
	READ_CONSTANT = "r"	
	
	def readJsonFile(fileName):
		"""
		reads json files and returns them as a Dictionary object

		Parameters:
			fileName:
				A String object representing the name of the file to be read
		"""
		directory = os.path.dirname(__file__) + "../" + fileName		#Directory where file is contained

		if os.path.splitext(directory)[1] != ".json":				#Raise error if file is of wrong type
			raise ValueError("Wrong File Type")

		managedFile = open(directory, FileManager.READ_CONSTANT)		#Open file or throw exception if file does not exist
		fileContent = json.loads(managedFile.read())					#
		return fileContent


if __name__ == "__main__":
	#Test FileManager Class
	try:
		f = FileManager
		invalid = f.readJsonFile("Tag.txt")
	except ValueError as e:
		print(e)
	jsonDict = f.readJsonFile("Tags.json")
	#for row in jsonDict["tags"]["row"]:
	#	print(row)
	
	#Test CollectionGenerator Class
	c = CollectionGenerator
	c.generateCollections()

