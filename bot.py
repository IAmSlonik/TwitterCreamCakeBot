import tweepy
import schedule
import time

keys = open("keys.txt", 'r')
CONSUMER_KEY = keys.readline().strip()
CONSUMER_SECRET = keys.readline().strip()
ACCESS_TOKEN = keys.readline().strip()
ACCESS_TOKEN_SECRET = keys.readline().strip()
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
def post():
    api.update_status("eaten 🍰")
#def hello():
#    print('hello')
schedule.every().day.at("20:37").do(post)
#schedule.every(2).minutes.do(hello)
while True:
    schedule.run_pending()
    time.sleep(1)