from FileManager import FileManager
class CollectionGenerator:
	
	def generateTagCollection():
		FileManager("Tags.json")

	def generatePostCollection():
		FileManager("Posts.json")

	def generateVoteCollection():
		FileManager("Votes.json")
