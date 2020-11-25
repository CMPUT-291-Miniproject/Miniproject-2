import pymongo
import collections
from Components.PostPrinter import PostPrinter
from Components.Terminal import Terminal

class AnswerListScreen:
	"""
	AnswerListScreen is a Screen which displays a list of answers

	AnswerListScreen displays a list of answers to a given question
	"""

	MenuOption = collections.namedtuple('Post', 'PostID Post Accepted')			#A named tuple object

	def printScreen(question):
		"""
		Provides the main functionality of AnswerListScreen
		Grabs all of the answers to a given question through a method
		then passes them to an object which displays them

		Parameters:
			question:
				A Dictionary object representing a question from the db
		Returns:
			A Dictionary object representing the answer selected or
			None if no answer was selected
		"""
		answers = AnswerList.getAnswers(question)
		menu = AnswerListMenu(answers, question)
		return menu.printScreen()



class AnswerListMenu:
	"""
	AnswerListMenu is a Menu

	AnswerListMenu displays all of the answers given to it on
	initialization then allows the user to select one of them
	"""
	def __init__(self, answers, question):
		"""
		Instantiates an AnswerListMenu object and ensures that if an
		accepted answer exists it is at the top of menuItems List

		Parameters:
			answers:
				A List of Dictionary objects representing all of the answers to question
			question:
				A Dictionary object representing a question retrieved from the db
		Returns:
			An AnswerListMenu object
		"""
		self.__question__ = question
		self.__menuItems__ = []
		if ('AcceptedAnswerId' in question):
			acceptedAnswerId = question['AcceptedAnswerId']
			self.__menuItems__.append(AnswerListScreen.MenuOption(PostID=acceptedAnswerId, Post=answers.pop(acceptedAnswerId), Accepted=True))
		self.fillMenu(answers)

	def fillMenu(self, posts):
		"""
		Fills List object menuItems with a series of named tuples representing each answer and information about said answer

		Parameters:
			posts: A Dictionary of Dictionaries where each Dictionary represents an answer to a question post
		"""
		for key in posts:
			if key is not None:
				self.__menuItems__.append(AnswerListScreen.MenuOption(PostID=key, Post=posts[key], Accepted=False))

	def printAnswer(self, item, index, accepted = False):
		"""
		Prints an answer with various formatting and if the answer is accepted prints stars around it

		Parameters:
			item:
				A Named Tuple object representing an answer and information about that answer
			index:
				An Integer object representing the current index of the List where item resides
			accepted:
				DEPRECATED (Unused parameter)
		"""
		string = ""
		if item.Accepted:
			string += "*********************************\n"
		string += str(index + 1) + ". " +"\n"
		if len(item.Post['Body']) > 80:
			string += item.Post['Body'][:80] + "\n"
		else:
			string += item.Post['Body'] + "\n"

		string += "CreationDate: " + item.Post['CreationDate'] + "\n"
		string += "Score: " + str(item.Post['Score']) + "\n" 
		if item.Accepted:
			string += "*********************************\n"

		print(string)

	def printMenu(self):
		"""
		Calls a method to print each answer in menuItems
		"""
		for  i,item in enumerate(self.__menuItems__):
				self.printAnswer(item, i)

	def printScreen(self):
		"""
		Provides the main functionality of AnswerListMenu
		Calls various methods to print answers to the screen and
		provides the user with the ability to select one of them

		Returns:
			A Dictionary object representing an answer to the question
		"""
		invalidInput = True
		while invalidInput:
			Terminal.clear()
			PostPrinter.printTitle(self.__question__)
			print("\n")
			self.printMenu()
			userInput = input("Enter Selection: ")
			if userInput.upper() == "EXIT" or userInput.upper() == "QUIT":
				return None
			try:
					userInput = int(userInput)
					if userInput < 1 or userInput > len(self.__menuItems__):
						print("Input is out of range")
					else:
						invalidInput = False
			except Exception:
					print("Entered input is invalid!")
			finally:
					input("Press Enter to Continue: ")
		userInput += -1
		return self.__menuItems__[userInput].Post


class AnswerList:
	"""
	AnswerList provides an interface between AnswerListScreen and the database

	AnswerList queries the database to get answers for AnswerListScreen
	"""
	client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
	db = client[Terminal.getDBName()]

	def getAnswers(question):
		"""
		Grabs answers if their parent ID matches the selected questions ID

		Parameters:
			question:
				A Dictionary object representing a question from the database
		Returns:
			A Dictionary of dictionaries representing various answers to the question
		"""
		answers = {}
		collection = AnswerList.db['Posts']
		query = {'$and' : 
					[ {'ParentId' : question['Id']},
					{ 'PostTypeId' : '2'} ]
				}
		results = collection.find(query)
		for result in results:
			answers[result['Id']] = result
		return answers

if __name__ == "__main__":
	from  SearchForQuestionsScreen import SearchForQuestionsScreen
	from SelectedQuestionScreen import SelectedQuestionScreen
	search = SearchForQuestionsScreen
	select = SelectedQuestionScreen

	post = search.printScreen()
	if select.printScreen(post) == 2:
		print(AnswerListScreen.printScreen(post))
