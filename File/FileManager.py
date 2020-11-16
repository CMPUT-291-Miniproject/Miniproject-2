class FileManager:
	READ_CONSTANT = "r"	

	def openRead(fileName):
		try:
			managedFile = open(fileName, FileManager.READ_CONSTANT)
		except OSError as OS:
			print("File does not exist!")
		else:
			return managedFile


if __name__ == "__main__":
	tagFile = FileManager.openRead("Tags.json")
	print(tagFile)
