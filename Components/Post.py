import pymongo
import string
import datetime
from Terminal import Terminal

class Post:
	
	def __init__(self, uid=None):
		"""
		Creates an object that can be used to post a question to the forum.
		
		Parameters:
			uid: User ID of the poster. Needed for adding question to database. 
			
		Returns: N/A
		"""
		self.__uid__ = uid
		
	def add_post(self, title, body, tags, qpid=None):
		"""
		Adds a question to the database, using a private function __get_pid__ to generate a unique PID.
		
		Parameters:
			Title: String. The title of the question.
			Body: String. The content of the question.
			Tags: List. List of all tags to add
			Qpid: optional argument. If included, the post is an answer.
				 Otherwise, qpid is None and the post is a question.
			
		Returns:
			N/A
		"""
		#log into db
		client = pymongo.MongoClient('localhost', int(Terminal.getPort()))

		db = client['291db']

		posts = db.Posts
		
		#Generates unique pid
		pid = self.get_pid()
		
		#Formats the tags for entry into db
		if tags:
			all_tags = ""
			for tag in tags:
				all_tags += "<{}>".format(tag)
		
		"""
		A unique id should be assigned to the post by your system, the post type id should be set to 1 (to indicate that the post is a question).
		The post creation date should be set to the current date and the owner user id should be set to the user posting it (if a user id is provided). 
		The quantities Score, ViewCount, AnswerCount, CommentCount, and FavoriteCount are all set to zero and the content license is set to "CC BY-SA 2.5".
		"""
		
		#if the post is a question, insert the question
		if qpid is None:
			
			#If the uid is given
			if self.__uid__ is not None:
				
				#If the user gives tags
				if tags is not None:
					post = {"Id": str(pid), "PostTypeId": "1", "CreationDate": str(datetime.datetime.utcnow().isoformat()), 
					"Score": 0, "ViewCount": 0, "Body": body, "OwnerUserId": self.__uid__, "Title": title,
					"Tags": all_tags, "AnswerCount": 0, "CommentCount": 0, "FavoriteCount": 0, "ContentLicense": "CC BY-SA 4.0"}
					
					posts.insert_one(post)
					self.__check_tag__(tags)
					
				#User gives no tags
				else:
					post = {"Id": str(pid), "PostTypeId": "1", "CreationDate": str(datetime.datetime.utcnow().isoformat()), 
					"Score": 0, "ViewCount": 0, "Body": body, "OwnerUserId": self.__uid__, "Title": title,
					 "AnswerCount": 0, "CommentCount": 0, "FavoriteCount": 0, "ContentLicense": "CC BY-SA 4.0"}
					
					posts.insert_one(post)
					
			#No uid is given	
			else:
				#Tags are given
				if tags is not None:
					post = {"Id": str(pid), "PostTypeId": "1", "CreationDate": str(datetime.datetime.utcnow().isoformat()),
					 "Score": 0, "ViewCount": 0, "Body": body, "Title": title,
					"Tags": all_tags, "AnswerCount": 0, "CommentCount": 0, "FavoriteCount": 0, "ContentLicense": "CC BY-SA 4.0"}
					#print(post)
					
					posts.insert_one(post)
					self.__check_tag__(tags)
					
				#Tags are not given
				else:
					post = {"Id": str(pid), "PostTypeId": "1", "CreationDate": str(datetime.datetime.utcnow().isoformat()),
					 "Score": 0, "ViewCount": 0, "Body": body, "Title": title,
					 "AnswerCount": 0, "CommentCount": 0, "FavoriteCount": 0, "ContentLicense": "CC BY-SA 4.0"}
					#print(post)
					
					posts.insert_one(post)
					
		#Post is an answer
		else:
			"""
			Question action-Answer. The user should be able to answer the question by providing a text. An answer record should be inserted into the database, with body field set to the provided text. A unique id should be assigned to the post by your system, the post type id should be set to 2 (to indicate that the post is an answer), the post creation date should be set to the current date and the owner user id should be set to the user posting it (if a user id is provided). The parent id should be set to the id of the question. The quantities Score and CommentCount are all set to zero and the content license is set to "CC BY-SA 2.5".
			"""
			if self.__uid__ is not None:
				post = {"Id": str(pid), "PostTypeId": "2", "ParentId": qpid, "CreationDate": str(datetime.datetime.utcnow().isoformat()), 
				"Score": 0, "ViewCount": 0, "Body": body, "OwnerUserId": self.__uid__, 
				"CommentCount": 0, "ContentLicense": "CC BY-SA 4.0"}
				posts.insert_one(post)
				
			else:
				post = {"Id": str(pid), "PostTypeId": "2", "ParentId": qpid, "CreationDate": str(datetime.datetime.utcnow().isoformat()), 
				"Score": 0, "ViewCount": 0, "Body": body, "CommentCount": 0, "ContentLicense": "CC BY-SA 4.0"}
				posts.insert_one(post)
			
	def get_info(self, pid):
		"""
		Given a pid, returns the title and body of a question.
		
		Parameters: 
			Pid: 4 char string. The post ID of the post to get info from
		
		Returns:
			Tuple of title and body of post, both of which are strings.
		"""
		client = pymongo.MongoClient('localhost', int(Terminal.getPort()))

		db = client['291db']

		posts = db.Posts
		
		post = posts.find_one({"Id": pid})
		
		return [post["Title"], post["Body"]]
		
		
	def get_pid(self):
		"""
		Generates a unique post ID
		
		Parameters: N/A
		
		Returns: 
			pid: Integer. The unique ID
		"""
		
		client = pymongo.MongoClient('localhost', int(Terminal.getPort()))

		db = client['291db']

		posts = db.Posts
		
		def findMaxAndMin(collection):
			maxNum = 1
			minNum = 1
			while  collection.find_one({'Id': str(maxNum)}) is not None:
				minNum = maxNum
				maxNum *= 2
			
			return [minNum, maxNum]


		nums = findMaxAndMin(posts)
		minNum = nums[0]
		maxNum = nums[1]
		
		"""TESTING
		print(minNum, maxNum)
		print(type(minNum), type(maxNum))
		print("+++++++++++\n")
		"""

		while True:
			num = (minNum + maxNum) // 2
			
			search = posts.find_one({'Id': str(num)})
			
			try:
				if int(search["Id"]) >= minNum:
					minNum = num
				else:
					maxNum = num
			except:
				maxNum = num
				
			"""TESTING
			print("Min:", minNum)
			print("Max:", maxNum)
			print("Middle:", num)
			"""
				
			if minNum == maxNum or minNum+1 == maxNum:
				num = maxNum
				
				break
				
		#print("Final:", num)
		return num
	
	def get_tagID(self):
		"""
		Generates a unique TagID.
		
		Parameters: N/A
		
		Returns: 
			tagID: Integer. Unique ID for the tag
		"""
		
		client = pymongo.MongoClient('localhost', int(Terminal.getPort()))

		db = client['291db']

		tags = db.Tags
		
		def findMaxAndMin(collection):
			maxNum = 1
			minNum = 1
			while  collection.find_one({'Id': str(maxNum)}) is not None:
				minNum = maxNum
				maxNum *= 2
			
			return [minNum, maxNum]


		nums = findMaxAndMin(tags)
		minNum = nums[0]
		maxNum = nums[1]
		"""TESTING
		print(minNum, maxNum)
		print(type(minNum), type(maxNum))
		print("+++++++++++\n")
		"""

		while True:
			num = (minNum + maxNum) // 2
			
			search = tags.find_one({'Id': str(num)})
			
			try:
				if int(search["Id"]) >= minNum:
					minNum = num
				else:
					maxNum = num
			except:
				maxNum = num
			
			"""TESTING
			print("Min", minNum)
			print(maxNum)
			print(num)
			"""
				
			if minNum == maxNum or minNum+1 == maxNum:
				num = maxNum
				break
				
		#print("Final tagID:", num)
		return num
	
	def __check_tag__(self, user_tags):
		"""
		Looks up the tag in the document of tags. If it's there, increase the count by 1. If not, add the tag and set the count to 1.
		
		Parameters:
			user_tags: list of strings. All of the tags to alter/enter in the tags collection
			
		Returns: N/A
		"""
		
		#TODO:Insert some wizard shit right here to add the tags
		
		#opens the tags collection
		client = pymongo.MongoClient('localhost', int(Terminal.getPort()))
		db = client['291db']
		tags = db.Tags
		
		for tag in user_tags:
			
			result = tags.find_one({"TagName": tag})
			
			if result:
				count = result["Count"]
				tags.update_one({"TagName": tag}, {'$set':{"Count": count + 1}})
			else:
				
				tid = self.get_tagID()
				tags.insert_one({"Id": str(tid), "TagName": tag, "Count": 1})
		
		
				
if __name__ == "__main__":
	
	question = Post("rtzy")
	question.add_post("Hockey players should be allowed to cross-check.", "I really hope this works.", ["Hockey"])
		
