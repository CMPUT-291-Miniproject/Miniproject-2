from Interface.Terminal import Terminal
from Interface.Post import Post

class PostScreen:
	"""
	User interface for generating and posting a question.
	
	Uses the framework from PostQuestion.py to enter the question into the database, and Terminal for extra UI commands.
	"""
	
	def __init__(self, uid=None):
		"""
		Creates an instance of PostQuestionScreen, which is used in Main.py (subject to change)
		
		Parameters:
			uid: User ID of the poster. Needed for adding question to database. 
			
		Additional Init. Variables:
			__body__: Post Object. Instance of the posting framework, used to add questions and answers to the database.
			
		Returns: N/A
		"""
		
		self.__body__ = Post(uid)
	

	def printQuestionScreen(self):
		"""
		User interface for adding a question to the database. This method validates all user input before passing it to PostQuestion.py, which actually adds the entry to the database.
		
		Parameters: N/A
		
		Returns: N/A
		"""
		repeat = True
		
		#Main input loop, runs until user input is valid, or they quit out of the menue.
		while repeat:
			Terminal.clear()
			Terminal.printCenter("---POSTING QUESTION---")
			Terminal.printCenter("To go back without posting a question, input BACK during any prompt.")
			print('\n')
			
			#get title of post
			title = input("Please enter the title of the question: ")
			if title.lower().strip() == "back":
				return
			
			print('\n')
			
			#Get body of post
			body = input("Please enter the description of the question: ")
			if body.lower().strip() == "back":
				return
				
			print('\n')
			
			#get tags of the post
			tag_input = input("Please enter the tags for this post, delimited by commas: ")
			
			#Formats the tag input for addition to the db. tags is the edited version of tag_input.
			tags = tag_input.lower().strip()
			if tags == "back":
				return
			tags = tags.split(',')
			if len(tag_input) == 0:
				tags = None
			else:
				final_tags = []
				for i in range(len(tags)):
					
					prev_tag = tags[i].strip()
					new_tag = ""
					for character in prev_tag:
						if character.isspace():
							new_tag += "-"
						else:
							new_tag += character

					if len(new_tag) > 0:
						final_tags.append(new_tag)			
				
			#input validation loop. breaks if input is Y or N.
			while True:
				Terminal.clear()
				#prints the title and body
				Terminal.printCenter("Title: "+title)
				Terminal.printCenter("Body: "+body)
				#prints the tags if applicable
				if tags:
					Terminal.printCenter("Tags: "+tag_input)
				else:
					Terminal.printCenter("Tags: N/A")
				print("\n")
			
				choice = input("Is this what you want to post? (Y or N): ")
				
				#if the user gives the ok to post, break out of all loops and add the post
				if choice.upper() == "Y":
					repeat = False
					break
				#if the user wants to change their post, repeat main loop but break this input loop
				elif choice.upper() == 'N':
					input("Press enter to continue:")
					return None
				#Any other input repeats the input loop
				else:
					input("Invalid input. Press enter to continue.")
				
		#adds the question to the database and alerts the user that the operation was a success.
		self.__body__.add_post(title, body, final_tags)
		input("Your question has been posted. Press enter to return back to the main menue.")
		return
					
	def printAnswerScreen(self, pid):
		"""
		User interface for adding an answer to the database. This method validates all user input before passing it to Post.py, which actually adds the entry to the database.
		
		Parameters: N/A
		
		Returns: N/A
		"""
		#TODO:
		
		repeat = True
		
		#Main input loop, runs until user input is valid, or they quit out of the menue.
		while repeat:
			self.__terminal__.printCenter("---POSTING ANSWER---")
			self.__terminal__.printCenter("To go back without posting a question, input BACK during any prompt.")
			print('\n')
			
			#gets the title and body of the post in a tuple
			info = self.__body__.get_info(pid)
			
			print("---ORIGINAL QUESTION---")
			print(info[0])
			print(info[1])
			print('\n')
			
					
			#get title of post
			title = input("Please enter the title of the answer: ")
			if title.lower().strip() == "back":
				return
			
			print('\n')
			
			#Get body of post
			body = input("Please enter the description of the answer: ")
			if body.lower().strip() == "back":
				return
				
			#input validation loop. breaks if input is Y or N.
			while True:
				self.__terminal__.clear()
				self.__terminal__.printCenter(title)
				self.__terminal__.printCenter(body)
				print("\n")
				
			
				choice = input("Is this what you want to post? (Y or N): ")
				
				#if the user gives the ok to post, break out of all loops and add the post
				if choice.upper() == "Y":
					repeat = False
					break
				#if the user wants to change their post, repeat main loop but break this input loop
				elif choice.upper() == 'N':
					input("Press enter to continue: ")
					return None
				#Any other input repeats the input loop
				else:
					input("Invalid input. Press enter to continue.")
				
			#adds the answer to the database and alerts the user that the operation was a success.
			self.__body__.add_post(title, body, pid)
			input("Your answer has been posted. Press enter to return back to the main menue.")
			return
		
		
		

if __name__ == "__main__":
	
	postQuestionScreen = PostScreen()
	postQuestionScreen.printQuestionScreen()
