from Components.Terminal import Terminal
import pymongo
class WelcomeScreen:
	"""
	A Screen which is used to welcome the user.

	This module is used to welcome the user and asks
	the user for their status which is either registered
	or not registered.
	"""
	def __init__(self):
		"""
		Creates an instance of WelcomeScreen, which is the UI interface for welcoming users to the
		program.
		Parameters:
			N/A
		Returns:
			An instance of WelcomeScreen
		"""
		Terminal.clear()

	def printTitle(self):
		"""
		Prints main elements of the UI
		"""
		Terminal.printCenter("--- Welcome User ---")
		Terminal.printCenter("(Type exit to quit at any time)")
		
	def printScreen(self):
		"""
		The main loop of the module. Prints the title and get's users input on whether they
		are registering or logging in
		"""
		while True:
			self.printTitle()
			userInput = input("If you're an existing user, please enter your id. Otherwise, press enter: ").strip()
			
			#if the user presses enter
			if userInput == "":
				return -1
			#if the user enters an id
			elif userInput.upper() != "EXIT":
				#TODO: User report		
				print("Loading...")
				report = self.report(userInput)	
				print("Number of questions posted: {}. Average score: {}.".format(report["num_questions"], report["qavg_score"]))
				print("Number of answers posted: {}. Average score: {}.".format(report["num_answers"], report["aavg_score"]))
				print("Number of votes: {}".format(report["num_votes"]))
				input("Press enter to continue...")
				return userInput
				
			elif userInput.upper().strip() == "EXIT":
				return None
			else:
				input("Invalid input, press enter to continue: ")
				Terminal.clear()

	def report(self, uid):
		#TODO: print the user report out
		"""
		(1) the number of questions owned and the average score for those questions
		(2) the number of answers owned and the average score for those answers
		(3) the number of votes registered for the user.
		"""
		client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
		db = client[Terminal.getDBName()]
		
		posts = db.Posts
		votes = db.Votes
		
		#PART 1
		
		#all of the questions
		num_questions = 0
		total_score = 0
		
		questions = posts.find({"OwnerUserId": uid, "PostTypeId": "1"})
		
		for dictionary in questions:
			num_questions += 1
			total_score += dictionary["Score"]
		
		try:
			qavg_score = total_score/num_questions
		except ZeroDivisionError:
			qavg_score = 0
		#print("Number of questions: {}. Average score: {}.".format(num_questions, qavg_score))
		
		#PART 2
		num_answers = 0
		total_score = 0
		
		answers = posts.find({"OwnerUserId": uid, "PostTypeId": "2"})
		
		for dictionary in answers:
			num_answers += 1
			total_score += dictionary["Score"]
			
		try:
			aavg_score = total_score/num_answers
		except ZeroDivisionError:
			aavg_score = 0
		#PART 3
		
		num_votes = votes.count_documents({"UserId": uid})
		
		return {"num_questions": num_questions, "num_answers": num_answers, "qavg_score": qavg_score, "aavg_score": aavg_score, "num_votes": num_votes}
		
		
		
if __name__ == "__main__":
	from Interface.Terminal import Terminal
	welcomeScreen = WelcomeScreen()
	welcomeScreen.printScreen()


