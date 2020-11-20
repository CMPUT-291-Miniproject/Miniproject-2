import pymongo
import string
import random
import datetime

class Post:
	
	def __init__(self, dbName, uid=None):
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
			Tags: List. List of all tags to add
			Qpid: optional argument. If included, it's a 4 char string of a question, and the post is an answer.
				 Otherwise, pid is None and the post is a question.
		
		Additional information:
			UID: 4 char string. Unique to each user, created from registerUser.py.
			self.__pid__: 4 char string. Unique to each post and created in __get_pid__.
			
		Returns:
			N/A
		"""
		#pid is handled inside, as well as pdate
		client = pymongo.MongoClient()

		db = client['291db']

		posts = db.Posts
		
		#TODO: fix unique uid generator
		pid = self.get_pid()
		
		#TODO:The provided tags are either inserted to (if they don't exist) or updated (if they do exists) in Tags collection.
		all_tags = ""
		for tag in tags:
			all_tags += "<{}>".format(tag)
		
		"""
		A unique id should be assigned to the post by your system, the post type id should be set to 1 (to indicate that the post is a question).
		The post creation date should be set to the current date and the owner user id should be set to the user posting it (if a user id is provided). 
		The quantities Score, ViewCount, AnswerCount, CommentCount, and FavoriteCount are all set to zero and the content license is set to "CC BY-SA 2.5".
		"""
		
		if qpid is None:
			post = {"Id": str(pid), "PostTypeId": "1", "CreationDate": str(datetime.datetime.utcnow().isoformat()), 
			"Score": 0, "ViewCount": 0, "Body": body, "OwnerUserId": self.__uid__, "Title": title,
			"Tags": all_tags, "AnswerCount": 0, "CommentCount": 0, "FavoriteCount": 0, "ContentLicense": "CC BY-SA 4.0"}
			
			posts.insert_one(post)
			self.__check_tag__(tags)
			'''
			"Id": "400728",
			"PostTypeId": "1",
			"CreationDate": "2020-09-06T03:15:37.153",
			"Score": 0,
			"ViewCount": 5,
			"Body": "<p>I have two Google Chrome windows, Window A, and Window B. I have full-screened Window B with <kbd>Cmd+Shift+F</kbd>. But, Window A also becomes fullscreen. When I un-fullscreen Window A with  <kbd>Cmd+Shift+F</kbd>, Window B becomes un-full-screened.</p>\n<p>Is there any way to have one Chrome windows fullscreen and the other one normal?</p>\n",
			"OwnerUserId": "373815",
			"LastActivityDate": "2020-09-06T03:15:37.153",
			"Title": "Chrome fullscreen windows",
			"Tags": "<macos><google-chrome><fullscreen>",
			"AnswerCount": 0,
			"CommentCount": 0,
			"ContentLicense": "CC BY-SA 4.0"
			'''
			
		else:
			post = {"ID": str(pid), "PostTypeId": "1", "CreationDate": "TODO", "Score": 0, "ViewCount": 0, "Body": body, "Title": title,
			"Tags": all_tags, "AnswerCount": 0, "CommentCount": 0, "ContentLicense": "CC BY-SA 4.0"}
			
			posts.insert_one(post)
		
	def get_info(self, pid):
		"""
		Given a pid, returns the title and body of a question.
		
		Parameters: 
			Pid: 4 char string. The post ID of the post to get info from
		
		Returns:
			Tuple of title and body of post, both of which are strings.
		"""
		#TODO
		pass
		
		
	def get_pid(self):
		"""
		Generates a unique post ID, which is checked in the database to verify uniqueness.
		
		Parameters: N/A
		
		Returns: 
			pid: 4 character string
		"""
		#TODO: get a unique pid.
		pid = ''
		
		client = pymongo.MongoClient()

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
		print(minNum, maxNum)
		print(type(minNum), type(maxNum))
		print("+++++++++++\n")

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
			
			print("Min", minNum)
			print(maxNum)
			print(num)
				
			if minNum == maxNum or minNum+1 == maxNum:
				num = maxNum
				break
				
		print(num)
		
		#something something something
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
		client = pymongo.MongoClient()
		db = client['291db']
		tags = db.Tags
		
		for tag in user_tags:
			
			result = tags.find_one({"TagName": tag})
			
			if result:
				count = result["Count"]
				tags.update_one({"TagName": tag}, {'$set':{"Count": count + 1}})
			else:
				#TODO: get the unique tag id
				tig = "123123"
				tags.insert_one({"Id": tig, "TagName": tag, "Count": 1})
		
		pass
				
if __name__ == "__main__":
	question = Post('Miniproject_1.db')
	question.add_post("This is a test.", "I really hope this works.")
		
