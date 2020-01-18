
"""
To evaluate the good or bad score of a tweet, we count the number of good and bad words in it.

If a word is good, increase the value of good_words by one.
If a word is bad, increase the value of bad_words by one.
If good_words > bad_words then it's a good tweet otherwise it's a bad tweet.
"""


import json
import twitter
import nltk
from nltk.stem.porter import *

# sets up twitter API:
twitter_api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='',tweet_mode = "extended")
screen_name = "realDonaldTrump"
stemmer = PorterStemmer()
words = {}


# get the words from the tweet
def get_words(input_string):
    return nltk.word_tokenize(input_string)


# Get value from strings
def get_value(list_of_words,dict_of_values):
    value = 0.0
    for w in list_of_words:
        if stemmer.stem(w) in list_of_words: #Stemmer.stem returns the foundational stem of the word being analyzed (e.g. wolves = wolf)
            value += dict_of_values[stemmer.stem(w)]
        return value


# Analyze the tweet:
def analyze_tweet(tweet_string, words):
    tweet_words = get_words(tweet_string)
    avg = get_value(tweet_words,words) / len(tweet_words)
    print("The average weight is: "+ str(avg))


# Read tweets from outside source using json:
def read_from_files(screenname,json_file,tweet_file):
    word_weights = {}
    with open(json_file) as f:
        s = f.read()
        word_weights = json.loads(s)

    tweets = twitter_api.GetUserTimeline(screen_name = screenname, count = 1)
    for tweet in tweets:
        print(tweet.full_text)
        analyze_tweet(tweet.full_text,word_weights)
        print("\n------------------\n")


read_from_files(screen_name,"word_weights.json","tweet.txt")
"""
#Start of tweet analysis
tweet_string = "Thanks to the historic TAX CUTS that I signed into law, your paychecks are going way UP, your taxes are going way DOWN, and America is once again OPEN FOR BUSINESS!".lower()

tweet_words = tweet_string.split()
num_of_words = len(tweet_words)
print("Number of words in the tweet is: "+ str(num_of_words))
"""

"""This will iterate thru the list and print stuff
for i in tweet_words:
    print("Number of letters in '%s' is: %i" % (i,len(i)))
print("End of words in tweet")
"""

"""
good_list = ["thanks", "business!", "paychecks", "your", "up", "way", "paychecks","historic"]
bad_list = ["taxes","down,","cuts"]
good_words,bad_words = 0,0

for w in tweet_words:
    if w.lower() in good_list:
        good_words += 1
    elif w.lower() in bad_list:
        bad_words += 1

print("This tweet has {0} good word(s) and {1} bad word(s)".format(good_words,bad_words))

if good_words > bad_words:
    print("Good tweet")
elif bad_words > good_words:
    print("BAD tweet")
else:
    print("Neutral tweet")

"""

"""
good_list = ["thanks", "business!", "paychecks", "your", "up", "way", "paychecks","historic"]
bad_list = ["taxes","down,","cuts","i","law",""] #Add however many words you want into this list.

def get_avg_weight(good,bad):
    num_words = len(good) + len(bad)
    sum_of_weights = 0.0

    good_dict,bad_dict = {},{}

    good_dict = dict(zip(good,[len(i)*10 for i in good]))
    bad_dict = dict(zip(bad,[-len(i)*10 for i in bad]))

    for w in tweet_words:
        if w in good_dict:
            sum_of_weights += good_dict[w]
        elif w in bad_dict:
            sum_of_weights += bad_dict[w]

    print(good_dict)
    print(bad_dict)

    final_score = sum_of_weights / num_words
    return final_score

final = get_avg_weight(good_list,bad_list)
print("The weight of the words is %.3f" % final)
"""

""" Windows commands to run virtual environment
python m venv . <--- Virtual environment module; installs libraries and stuff in current directory.
Scripts\activate <--- Navigates to scripts folder and runs activate.bat
pip install nltk <--- Natural Language Toolkit package. Natural language processing.
import nltk <---- REALLY HUGE library.

workshop author: github.com/alialavia/python-workshop1
"""
