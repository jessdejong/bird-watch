from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('user/<username>')
def get_user(username):
    # get the users tweets


# STUFF WE NEED TO DO:
#potential tweets that are negative
#potential users that are negative
