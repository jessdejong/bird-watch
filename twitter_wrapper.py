from twitter import *
import json, string

# twitter keys
ACCESS_TOKEN = "967202509990322176-WoUrv9EqLk6cdkFjkXfuZhvufdA6ysb"
ACCESS_SECRET = "65xf901IAzmi8xjOUEf2Vr8oinPBp51J25Bt4PbtFAfnE"
CONSUMER_KEY = "CS0DjdYG1kOP5XmSP9cVudJdX"
CONSUMER_SECRET = "DoVIxtMN4wETttNCfjiAnRyRMK9EL1CrLLtUXi5SroqjTGUAnx"
printable = set(string.printable)

# get all of user tweets
def getUserTweets(username):
    t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
    data = json.loads(json.dumps(t.statuses.user_timeline(screen_name=username, count=200)))
    tweets = [];
    for i in range(len(data)):
        tweets.append(data[i]["text"].encode('ascii',errors='ignore').decode())
    return tweets
    
# get list of followers
def getUserFollowers(username):
    t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
    data = json.loads(json.dumps(t.friends.list(screen_name=username, count=200)))
    friends = [];
    for i in range(len(data["users"])):
        friends.append(data["users"][i]["screen_name"])
    return friends