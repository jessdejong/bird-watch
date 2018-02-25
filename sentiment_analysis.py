import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
import twitter_wrapper

natural_language_understanding = NaturalLanguageUnderstandingV1(
        username='a058b551-a067-48ad-9c08-3d57cb331a12',
        password='nW4Q8XpczFc4',
        version='2017-02-27')

# find if it has a tag
def hasTag (text):
    if (text.find("@") != -1):
        return True
    return False

def remove_retweet(text):
    if (text.find("RT @") != -1):
        return text[(text.find(":")+1):]
    return text


# find negative tweets
def find_negative_tweets(username):
    # get tweets
    tweets = twitter_wrapper.getUserTweets(username)
    urls = twitter_wrapper.getUserLinks(username)

    # averages
    average_sentiment = 0.0
    sadness = 0.0
    joy = 0.0
    fear = 0.0
    disgust = 0.0
    anger = 0.0

    divisor = 0.0


    # negative tweets
    neg_tweets = []

    # go through every tweet
    for i in range(0, len(tweets)):
        #print(tweets[i])
        

        # remove characters other than space and letters
        tweet = ''.join(i for i in tweets[i] if i.isalpha() or i.isspace())
        # tweet = tweet * 4
        # print(tweet)

        if (len(tweet) < 10):
            continue

        response = natural_language_understanding.analyze(

                text = tweet,

                features = Features(
                    keywords=KeywordsOptions(
                        emotion=True,
                        sentiment=True,
                        limit=1)),
                    
                language = 'en')

        try:
            # getting the data
            data = json.loads(json.dumps(response, indent=2))

            # print(data)

            # data['keywords'][0]['emotion']['anger']
            # print(data['keywords'][0]['emotion']['anger'])

            # if (data['keywords'][0]['sentiment']['score'] < -.5):
            #    neg_tweets.append(urls[i])
            # print(data)



            # CURRENT GETTING
            # if (hasTag(tweets[i]) and data['keywords'][0]['emotion']['anger'] > .15):
            #    neg_tweets.append(urls[i])
            if (hasTag(remove_retweet(tweets[i])) and data['keywords'][0]['sentiment']['score'] < -.5 and data['keywords'][0]['emotion']['anger'] > .15):
                #print(tweets[i])
                neg_tweets.append(urls[i])
                #print("#################################appended")




                # print(remove_retweet(tweets[i]))
            #elif (hasTag(tweets[i]) and data['keywords'][0]['sentiment']['score'] < -.4):
                # neg_tweets.append(urls[i])

            # print(data['keywords'][0]['sentiment']['score'])
            # print(data['keywords'][0]['emotion']['anger'])

            
            # Getting averages
            average_sentiment += data['keywords'][0]['sentiment']['score']
            sadness += data['keywords'][0]['emotion']['sadness']
            joy += data['keywords'][0]['emotion']['joy']
            fear += data['keywords'][0]['emotion']['fear']
            disgust += data['keywords'][0]['emotion']['disgust']
            anger += data['keywords'][0]['emotion']['anger']
            
            divisor += 1.0
            # print(divisor)


        # except IndexError:
        except:
            pass

#    print(average_sentiment/divisor)
    if (divisor != 0):
        return neg_tweets, average_sentiment/divisor, sadness/divisor, joy/divisor, fear/divisor, disgust/divisor, anger/divisor
    else:
        return neg_tweets, 0, 0, 0, 0, 0, 0

