from Interface.Terminal import Terminal
from WelcomeScreen import WelcomeScreen
from MainMenuScreen import MainMenuScreen
from PostScreen import PostScreen
from SearchForQuestionsScreen import SearchForQuestionsScreen
#from SearchforQuestionsScreen import SearchForQuestionsScreen
#from Vote import Vote

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
			#prints the menue and returns the choice the user makes as an int. error handling and processing takes place in menu.py, so
			#there's no need to worry about it here
			menu = MainMenuScreen().printScreen()
			
			#post question
			if menu == 0:
				#TODO: alter posting a question so it takes tags
				try:
					PostScreen(uid).printQuestionScreen()
				except:
					PostScreen().printQuestionScreen()
				
			#search for posts
			elif menu == 1:				
				#TODO: alter searching for questions.
				sScreen = SearchForQuestionsScreen
				post = sScreen.printScreen()			

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