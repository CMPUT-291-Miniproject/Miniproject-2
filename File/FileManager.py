class FileManager:
	READ_CONSTANT = "r"	

	def readJsonFile(fileName):
		try:
			managedFile = open(fileName, FileManager.READ_CONSTANT)
		except OSError as OS:
			print("File does not exist!")
		else:
			fileContent = managedFile.read()
			return fileContent

if __name__ == "__main__":
	jsonDict = FileManager.readJsonFile("Tags.json")
	print(jsonDict)
