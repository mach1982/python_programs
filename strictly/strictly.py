#Author Ailin Mac Hugh
#Version 0.9

'''
Dependencys: Texblob for NLP
             tweepy for  twitter AIP Authentication


'''

from textblob import TextBlob
import tweepy

consumer_key = 'YOUR CONSUMER KEY'
consumer_secret = 'YOUR SECERT KEY'
access_token = 'YOUR ACCESS TOKEN '
accces_secert = 'YOUR ACCCES SERECT'

#Authenticate with twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, accces_secert)

api = tweepy.API(auth)

#Open file with celbs names 
with open('celbs.txt', 'r') as myfile2:
        data2 = myfile2.read()
        celbs = data2.split(",")
f = open("output.txt", "w")

#Loop through Celbs
for c in celbs:


   #Count is set at 100 as twitter only allow a max number of 100 connection to it API per app 

    tweets = api.search(c, count=100) 
     #Negative  semtiment counter
    countn = 0 
    #Positive semtimnet counter
    countp = 0 
    #Neutal  semtimnet counter
    countne = 0
    for tweet in tweets:
        # print(tweet.text)
        analysis = TextBlob(tweet.text)
        # print(analysis.sentiment)
        if analysis.sentiment.polarity > 0:
            countp += 1
        elif analysis.sentiment.polarity == 0:
            countn += 1
        else:
            countne += 1

#Write to the output file, and prints to console for error checking 
    print(c)
    f.write('Name {}\n'.format(c))
    print('Positive {}'.format(countp))
    f.write('Positive {}\n'.format(countp))
    print('Negative {}'.format(countn))
    f.write('Negative {}\n'.format(countn))
    print('Neutral {}'.format(countne))
    f.write('Neutral {}\n'.format(countne))
    print('Total tweets scanned : {}'.format(countn + countp + countne))

