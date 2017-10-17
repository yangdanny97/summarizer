import praw
import os
from summary import Summarizer

class Bot:
	"""
	A single instance of the bot
	"""
	def __init__(self):
		self.reddit = praw.Reddit(client_id='my client id',
	                     client_secret='my client secret',
	                     user_agent='my user agent',
	                     username=os.environ.get('BOT_USERNAME'),
	                     password=os.environ.get('BOT_PASSWORD'))



	"""
	Summarizes the article contained within the given link

	"""
	def create_summary(self,link):
		pass
		#1. parse conents of link - don't do anything if the link is bad/the contents can't be parsed
		#2. create instance of Summarizer
		#3. return output of Summarizer

	"""
	Writes a reddit post with the summary

	"""
	def post(self,summary):
		pass
		#maybe we should have a MD template

"""
TODO:
Figure out how to use Reddit API to check for updates on some selected set of subreddits
Figure out how to comment properly
Maybe thank people for saying Good Bot
Maybe track the total number of upvotes/comments for the bot
"""
