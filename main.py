from UI.Interface.Terminal import Terminal
from UI.WelcomeScreen import WelcomeScreen
#from UI.MainMenuScreen import MainMenuScreen
from UI.PostScreen import PostScreen
from UI.SearchForQuestionsScreen import SearchForQuestionsScreen
#from Vote import Vote

if __name__ == "__main__":
	terminal = Terminal()

	#Main program loop, includes the welcome screen and login sequence. This loop handles cases such as users logging out and back into another account.
	exit = False
	while not exit:
			
		#prints the welcome screen, which lets users login, register, or exit the program 
		welcomeScreen = WelcomeScreen(terminal)
		
		#Gets the user id if they provide one, checks are done in Welcomescreen.
		isUser = welcomeScreen.printScreen()
		
		#if the user doesn't enter an id
		if isUser == 1:
			pass
		#if the user enters an id
		elif isUser:
			#TODO: display the stuff we need to display if a uid is provided
			pass
		else:
			#Quitting the program, leads to a goodbye message outside of loop.
			break
		
		#Input loop for command choice.
		while True:
			#prints the menue and returns the choice the user makes as an int. error handling and processing takes place in menu.py, so
			#there's no need to worry about it here
			menu = MainMenuScreen(terminal).printScreen()
			
			#post question
			if menu == 0:
				#TODO: alter posting a question so it takes tags
				PostScreen(terminal, uid).printQuestionScreen()
				
			#search for posts
			elif menu == 1:				
				#TODO: alter searching for questions.
				post = SearchForPostsScreen(terminal).printScreen()				

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