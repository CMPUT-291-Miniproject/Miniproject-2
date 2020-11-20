import pymongo
import collections

from Terminal import Terminal

class AnswerListScreen:
	MenuOption = collections.namedtuple('Post', 'PostID Post' )

	def printScreen(question):
		answers = AnswerList.getAnswers(question)
		menu = AnswerListMenu(answers, question)
		menu.printMenu()



class AnswerListMenu:
	def __init__(self, answers, question):
		self.__menuItems__ = []
		if ('AcceptedAnswerId' in question):
			acceptedAnswerId = question['AcceptedAnswerId']
			self.__menuItems__.append(AnswerListScreen.MenuOption(PostID=acceptedAnswerId, Post=answers.pop(acceptedAnswerId)))
		self.fillMenu(answers)

	def fillMenu(self, posts):
		for key in posts:
			if key is not None:
				self.__menuItems__.append(AnswerListScreen.MenuOption(PostID=key, Post=posts[key]))

	def printAnswer(self, item, index, accepted = False):
		string = ""
		string += str(index) + ". \n"

		if accepted:
			string += "Title: *" + item.Post['Title'] + " *" + "\n"
		else:
			string += "Title: " + item.Post['Title'] + "\n"

		if len(answer['Body']) > 80:
			string += item.Post['Body'][:80] + "\n"
		else:
			string += item.Post['Body'] + "\n"

		string += "CreationDate: " + item.Post['CreationDate'] + "\n"
		stringToPrint += "Score: " + str(item.Post['Score'])

		print(stringToPrint)

	def printMenu(self):
		for  i,item in enumerate(self.__menuItems__):
				self.printAnswer(item, i)



class AnswerList:
	client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
	db = client[Terminal.getDBName()]

	def getAnswers(question):
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
		AnswerListScreen.printScreen(post)
