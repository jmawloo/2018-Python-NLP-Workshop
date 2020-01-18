import nltk
import json
from nltk.stem.porter import *
import twitter

twitter_api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='',
                      tweet_mode='extended')


stemmer = PorterStemmer()

words = {}

def get_words(input_string):
    return nltk.word_tokenize(input_string)

def get_value(list_of_words, dict_of_values):
    value=0.0
    for w in list_of_words:
        if stemmer.stem(w) in dict_of_values:
            value += dict_of_values[stemmer.stem(w)]
    return value

def analyse_tweet(tweet_string, words):
    tweet_words  = get_words(tweet_string)
    avg = get_value(tweet_words, words) / len(tweet_words)
    print("The average weight is : " + str(avg))

def read_files(json_file, tweet_file):
    words = {}
    with open(json_file) as f:
        s = f.read()
        words=json.loads(s)

    tweets = twitter_api.GetUserTimeline(screen_name="realDonaldTrump", count=10)
    for tweet in tweets:
        print(tweet)
        #analyse_tweet(tweet, words)
        print("\n------------------------------------\n")

read_files("word_weights.json", "tweet.txt")
