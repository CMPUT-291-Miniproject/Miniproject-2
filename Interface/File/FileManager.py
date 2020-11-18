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
