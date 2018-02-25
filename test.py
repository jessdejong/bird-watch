from flask import Flask, url_for, request, render_template, Markup, redirect
import twitter_wrapper
import sentiment_analysis

app = Flask(__name__)

@app.route('/')
def hello_world():
	return redirect('home')

@app.route('/home')
def show_user_profile(username=None):
	return render_template('Home.html', username=username)

@app.route('/home/<username>', methods=['GET', 'POST'])
def login(username):
	if request.method == 'GET':
		return ' ||| '.join(twitter_wrapper.getUserTweets(username))
	else:
		return hello()


@app.route('/analysis/<username>', methods=['GET'])
def ana(username):
	if request.method == 'GET':
		ret = ""
		data = sentiment_analysis.find_negative_tweets(username)[0]
		ret = " ".join(data) + "|||"

		users = twitter_wrapper.getUserFollowers(username)
		bad_tweets = []
		for i in users:
			bet = sentiment_analysis.find_negative_tweets(i)[0]
			if(len(bet) >= 1):
				bad_tweets.append(' '.join(bet))
		ret = ret +  ' '.join(bad_tweets)
		return ret
	else:
		return hello()

'''with app.test_request_context():
	print url_for('hello_world')
	print url_for('projects')
	print url_for('about', next='/')
	print url_for('hello', username='SyedA')
	print url_for('static', filename='home.css') '''
