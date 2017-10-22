import os
import praw
import tldextract
from newspaper import Article
from summary import Summarizer

class Bot:
        """
        A single instance of the bot
        """
        def __init__(self):
            self.reddit = praw.Reddit(client_id=os.environ.get('CLIENT_ID'),
                         client_secret=os.environ.get('CLIENT_SECRET'),
                         user_agent="News Article Summary Bot Test"
                         username=os.environ.get('BOT_USERNAME'),
                         password=os.environ.get('BOT_PASSWORD'))
            self.subreddits_list = []
            self.approved_sites = set()
            self.subreddit_list = ['Test']
            self.subreddits = reddit.subreddit("+".join(self.subreddits))


        def run(self):
            for submission in subreddits.stream.submissions():
                url_check = tldextract.extract(submission.extract).domain
                proceed = False
                for site in self.approved_sites:
                    if url_check in self.approved_sites: proceed = True
                if proceed:
                    self.create_summary(submission.url)

        """
        Summarizes the article contained within the given url
        """
        def create_summary(self, url, shrinker=5):
            #1. parse conents of link - don't do anything if the link is bad/the contents can't be parsed
            #2. create instance of Summarizer
            #3. return output of Summarizer, or empty string if any step fails
            text = Bot.get_article_text(url)
            summarizer = Summarizer(text)
            if text=="" or len(summarizer.sentences)<16:
                return ""
            summary = summarizer.summarize(len(summarizer.sentences)/shrinker)
            return summary

        @staticmethod
        def get_article_text(url):
            """
            Gets the article text of a given url
            """
            try:
                article = Article(url)
                article.download()
                article.parse()
                return article.text
            except:
                return ""

        """
        Writes a reddit post with the summary

        """
        def post(self, summary):
                pass
                #maybe we should have a MD template

"""
TODO:
Figure out how to use Reddit API to check for updates on some selected set of subreddits
Figure out how to comment properly
Maybe thank people for saying Good Bot
Maybe track the total number of upvotes/comments for the bot
"""
