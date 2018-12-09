import smtplib
import tweepy
from email.mime.text import MIMEText

'''
Function to send the e-mail from a kist of e-mail address

Reads in the the e-mail address from email_address.txt

Reads in the message to be sent from msg.txt

'''


def email_msg():
    """
       Reads in the the file
    """
    with open('msg.txt', 'r') as myfile:
        body = myfile.read() #body of the e-mail

    """
           Reads in the the  e-mail address and splits when a space is encountered
    """

    with open('email_address.txt', 'r') as myfile2:
        data2 = myfile2.read()
        email = data2.split(" ")

    # E-mail Authentication
    fromaddr = "YOUR E-AML"
    username = "YOU USERNAME"
    passwd = "YOU PASSWORD"

    #Loops through each e-mail  and sends it

    for e in email:
        fromaddy = fromaddr
        msg = MIMEText(body)
        msg['Subject'] = 'Follow UP'
        msg['From'] = fromaddy
        msg['To'] =e

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, passwd)
        server.sendmail(fromaddr, e, msg.as_string())
        server.quit()
        print("Mail sent")


'''
Function to send tweets to a list of twitter accounts 
'''


def tweet_msg():
    #Twitter Autencation
    consumer_key = 'YOUR_COMSUMER_KEY'
    consumer_secret = 'YOUR _COMSUMER_SECRET'
    access_token = 'YOUR_TYOKEN'
    access_token_secert = 'YOUR_TOKEN_SECERT'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secert)

    api = tweepy.API(auth)

    with open('twitter_name.txt', 'r') as myfile3:
        data3 = myfile3.read()
        handel = data3.split(" ")

        with open('test2.txt', 'r') as myfile4:
            tweet = myfile4.read()

        for h in handel:
            # print(x)
            api.update_status('@' + h + tweet)
    print("Tweet sent")

'''Mani fuction '''
def main():
    email_msg()
    tweet_msg()


main()