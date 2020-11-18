import sqlite3
import string
import random

class Post:
	
	def __init__(self, dbName, uid):
		"""
		Creates an object that can be used to post a question to the forum.
		
		Parameters:
			dbName: String. The name of the database, needed to connect to said database.
			uid: User ID of the poster. Needed for adding question to database. 
			
		Returns: N/A
		"""
		self.__db__ = dbName
		self.__uid__ = uid
		
	def add_post(self, title, body, tags, qpid=None):
		"""
		Adds a question to the database, using a private function __get_pid__ to generate a unique PID.
		
		Parameters:
			Title: String. The title of the question.
			Body: String. The content of the question.
			Qpid: optional argument. If included, it's a 4 char string of a question, and the post is an answer.
				 Otherwise, pid is None and the post is a question.
		
		Additional information:
			UID: 4 char string. Unique to each user, created from registerUser.py.
			self.__pid__: 4 char string. Unique to each post and created in __get_pid__.
			
		Returns:
			N/A
		"""
		#pid is handled inside, as well as pdate
		db = sqlite3.connect(self.__db__)
		
		#Gets unique PID for a post
		pid = self.__get_pid__()
		
		"""
		The next statements enter the question into the database as a post, and then enters it as a question.
		After doing so, it commits the additions and closes the database.
		"""
		
		if qpid is None:
			#db entry visualization               pid   pdate    title body poster
			db.execute("INSERT INTO posts VALUES (?, DATE('now'), ?, ?, ?)", (pid, title, body, self.__uid__))
			#db entry visualization                  pid  theaid
			db.execute("INSERT INTO questions VALUES (?, ?)", (pid, None))
		else:
			#db entry visualization               pid   pdate    title body poster
			db.execute("INSERT INTO posts VALUES (?, DATE('now'), ?, ?, ?)", (pid, title, body, self.__uid__))
			#db entry visualization
			db.execute("INSERT INTO answers VALUES (?, ?)", (pid, qpid))
			
		db.commit()
		db.close()
		
	def get_info(self, pid):
		"""
		Given a pid, returns the title and body of a question.
		
		Parameters: 
			Pid: 4 char string. The post ID of the post to get info from
		
		Returns:
			Tuple of title and body of post, both of which are strings.
		"""
		db = sqlite3.connect(self.__db__)
		cur = db.cursor()
		cur.execute("SELECT title, body FROM posts WHERE pid = ?", (pid,))
		return cur.fetchone()
		
		
	def __get_pid__(self):
		"""
		Generates a unique post ID, which is checked in the database to verify uniqueness.
		
		Parameters: N/A
		
		Returns: 
			pid: 4 character string
		"""
		db = sqlite3.connect(self.__db__)
		cur = db.cursor()
		chars = string.ascii_letters + string.digits
		while True:
			pid = ""
			for i in range(4):
				pid += chars[random.randrange(0, len(chars))]
			
			cur.execute("SELECT pid FROM posts WHERE pid = ?", (pid,))
			
			if cur.fetchone() is None:
				break
		return pid
				
if __name__ == "__main__":
	question = Post('Miniproject_1.db')
	question.add_post("This is a test.", "I really hope this works.")
		
