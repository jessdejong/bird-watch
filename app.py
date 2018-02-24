from flask import Flask
import twitter_wrapper

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

# get user names
@app.route('/user/<username>')
def get_usernames(username): 
    return ' '.join(twitter_wrapper.getUserFollowers(username))

# get urls
@app.route('/urls/<username>')
def get_urls(username):
    return ' '.join(twitter_wrapper.getUserLinks(username))


# STUFF WE NEED TO DO:
#potential tweets that are negative
#potential users that are negative
