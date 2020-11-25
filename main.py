import pymongo
from Components.Terminal import Terminal
from Components.WelcomeScreen import WelcomeScreen
from Components.MainMenuScreen import MainMenuScreen
from Components.PostScreen import PostScreen
from Components.SearchForQuestionsScreen import SearchForQuestionsScreen
from Components.SelectedQuestionScreen import SelectedQuestionScreen
from Components.SelectedAnswerScreen import SelectedAnswerScreen
from Components.AnswerListScreen import AnswerListScreen
from Components.Vote import Vote

if __name__ == "__main__":
	

	#Main program loop, includes the welcome screen and login sequence. This loop handles cases such as users logging out and back into another account.
	exit = False
	while not exit:
			
		#prints the welcome screen, which lets users login, register, or exit the program 
		welcomeScreen = WelcomeScreen()
		
		#Gets the user id if they provide one, checks are done in Welcomescreen.
		isUser = welcomeScreen.printScreen()
		
		#if the user doesn't enter an id
		if isUser == 1:
			uid = None
			pass
		#if the user enters an id
		elif isUser:
			uid = isUser
			pass
		else:
			#Quitting the program, leads to a goodbye message outside of loop.
			break
		
		#Input loop for command choice.
		while True:
			#indexing
			client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
			db = client["291db"]
			posts = db["Posts"]
			tags = db['Tags']
			votes = db["Votes"]
			
			posts.create_index([("Id", 1)])
			"""
			posts.create_index([("Title", 1), ("Body", 1), ("Tags", 1)])
			posts.create_index([("Title", 1)])
			posts.create_index([("Body", 1)])
			posts.create_index([("Tags", 1)])
			"""
			
			votes.create_index([("UserId", 1)])
			votes.create_index([("Id", -1)])

			tags.create_index([("TagName", 1)])
			tags.create_index([("Id", 1)])
			
			
			#prints the menue and returns the choice the user makes as an int.
			menu = MainMenuScreen().printScreen()
			
			#post question
			if menu == 0:
				#Post a question, with or without a uid.
				PostScreen(uid).printQuestionScreen()
				
			#search for posts
			elif menu == 1:				
				#TODO: alter searching for questions.
				sScreen = SearchForQuestionsScreen
				post = sScreen.printScreen()
			
				#User choice for options
				choice = SelectedQuestionScreen.printScreen(post)	
				
				if choice == 1:
					#Post an answer to the question
					PostScreen(uid).printAnswerScreen(post["Id"])
					
				elif choice == 2:
					#List all of the answers and offer the user a choice of answers
					choice = SelectedAnswerScreen.printScreen(AnswerListScreen.printScreen(post))
					
					if choice == 1:
						#user votes for the post
						Vote.makeVote(post, uid)
					else:
						pass
					
				elif choice == 3:
					#User votes for the post
					Vote.makeVote(post, uid)
					
				elif choice == 4:
					#Exit back to main menue
					pass

			#log out of account
			elif menu == 2:
				break
				
			#exit program
			elif menu == 3:
				exit = True
				break
			
			#end of input loop
	#end of main program loop

#When the user quits the program.
print("Goodbye!")