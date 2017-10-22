import math
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
                         user_agent="News Article Summary Bot Test",
                         username=os.environ.get('BOT_USERNAME'),
                         password=os.environ.get('BOT_PASSWORD'))
            self.approved_sites = set(['nytimes'])
            self.subreddit_list = ['Test']
            self.subreddits = self.reddit.subreddit("+".join(self.subreddit_list))


        def run(self):
            for submission in self.subreddits.hot(limit=30):
                url_check = tldextract.extract(submission.url).domain
                proceed = False
                for site in self.approved_sites:
                    if url_check in self.approved_sites:
                        proceed = True
                        break
                if proceed:
                    summary = self.create_summary(submission.url)
                    if summary != "":
                        print(summary)
                        submission.reply(summary)

        """
        Summarizes the article contained within the given url
        """
        def create_summary(self, url, shrinker=5):
            #1. parse conents of link - don't do anything if the link is bad/the contents can't be parsed
            #2. create instance of Summarizer
            #3. return output of Summarizer, or empty string if any step fails
            text = Bot.get_article_text(url)
            summarizer = Summarizer(text)
            if text == "" or len(summarizer.sentences)<16:
                return ""
            summary = summarizer.summarize(min(int(3+len(summarizer.sentences)/shrinker), 5))
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
