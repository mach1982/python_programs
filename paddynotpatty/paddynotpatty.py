#!/user/bin/env/pytthon

#Disclaimer: This is for  education use only , how you use it up to you.

import sys
import tweepy

consumer_key = 'YOUR_COMSUMER_KEY'
consumer_secret = 'YOUR _COMSUMER_SECRET'
access_token = 'YOUR_TYOKEN'
access_token_secret = 'YOUR_TOKEN_SECERT'


auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
all_tags = []

for t in tweepy.Cursor(api.search, q='Pattys Day').items(5):
   all_tags.append(t)
for t in tweepy.Cursor(api.search, q='#pattysday').items(5):
   all_tags.append(t)

for tweet in all_tags:
   s_name=tweet.author.screen_name
   print  tweet.author.screen_name
   api.update_status('@'+s_name +" It is St Patricks or Paddys Day not Patty see this link http://paddynotpatty.com/ #paddynotpatty" )


