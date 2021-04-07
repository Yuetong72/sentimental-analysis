import praw
import pandas as pd
from newsapi.newsapi_client import NewsApiClient
from pytz import timezone
import datetime
import tweepy 
from tweepy import OAuthHandler 
from tweepy import Stream
import json
from os import environ

class scraping:
    def __init__(self):
        # initialize Reddit
        self.reddit = praw.Reddit(client_id='ajQLAIuBK8H12A',
                     client_secret='iTyNJ9f8hF6a1t8uMIl8IEHCDHM',
                     user_agent='CryptoEQ')

        # initialize Google News
        self.newsapi = NewsApiClient(api_key='783c2e695dd249459721cbad4a6fd589')

        # initialize Twitter
        self.consumer_key = environ[consumer_key]
        # 'Bikr0kqkiYTEOLlTWhP2RNeae'
        self.consumer_secret = environ[consumer_secret]
        # 't1wigeMGDBl6hFSkQEeNwE0urn3ZxMk0M4GqnAWXbOvyriouw8'
        self.access_token = environ[access_token]
        # '986411194234888193-M23IJfTQgr81GrkwTIbOFR474A0pRby'
        self.access_token_secret = environ[access_token_secret]
        # 'sUq52for7eU4qegLhBqoPXaTF7DwGkwKhtJnUoSiUePMx'
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret) 
        self.auth.set_access_token(self.access_token, self.access_token_secret) 
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True) 

        


    def get_reddit(self, keyword):
        subreddit = self.reddit.subreddit('all')
        scrapedReddit = subreddit.search(keyword, 
                                        sort='new', 
                                        syntax='lucene', 
                                        time_filter='hour',
                                        limit = 1)         
                                        # 100    
        
        scrapedData = { "title":[]}                  

        for data in scrapedReddit:
            scrapedData["title"].append(data.title)
                        
        return pd.DataFrame(scrapedData)



    def get_news(self,keyword):
        scrapedNews = self.newsapi.get_everything(q = keyword,
    #                                       sources='google-news',
                                        language='en',
                                        sort_by='publishedAt',
                                        page_size = 1) 
                                        # 100
                                        ################

        scrapedData = { "title":[]}  
        for i in scrapedNews['articles']:
            scrapedData["title"].append(i['title'])
                        
        return pd.DataFrame(scrapedData)



    def get_twitter(self, keyword):
        try: 
            dictionary = {"id":[], "title":[]}
            for tweet in tweepy.Cursor(self.api.search, q=keyword, lang="en", result='recent').items(1):
                # 250
                dictionary["title"].append(tweet.text)
            for status in self.api.user_timeline():
                dictionary["id"].append(status.id)
                
            df = pd.DataFrame.from_dict(dictionary, orient='index')
            df = df.transpose()
            return df

        except tweepy.TweepError as e: 
            print(keyword + " Error : " + str(e)) 



#     def get_twitter(self,keyword):
#         # Create you Stream object with authentication
#         stream = tweepy.Stream(self.auth, MyStreamListener())
#         stream.filter(follow = "1337780902680809474", track = keyword)
#         tweets_data = []

#         # Open connection to file
#         h=open('tweets.txt','r')

#         # Read in tweets and store in list: tweets_data
#         for i in h:
#             try:
#                 tmp=json.loads(i)
#                 tweets_data.append(tmp)
#             except:
#                 print(" ")
#         h.close()

#         df = pd.DataFrame(tweets_data, columns=['text'])
#         return df
    


# class MyStreamListener(tweepy.StreamListener):  
#     def __init__(self, api=None):
#         # inherit class attributes
#         super(MyStreamListener, self).__init__()
#         self.num_tweets = 0
#         self.file = open("tweets.txt", "w+")

#     def on_status(self, status):
#         tweet = status._json
        
#         self.file.write( json.dumps(tweet) + '\n' )
        
#         self.num_tweets += 1
#         if self.num_tweets < 10:
#             return True
#         else:
#             return False
#         self.file.close()

#     def on_error(self, status):
#         if status == 420:
#             #returning False in on_data disconnects the stream
#             return False

