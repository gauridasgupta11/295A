import pandas as pd
import json
import re
from nltk.corpus import stopwords


tweets_data_path = 'C:/Users/Muffadal/Desktop/dummy.txt'
tweets_text_data = []
tweets_lang_data = []
tweets_place_data = []
tweets_file = open(tweets_data_path, "r")
tweets = pd.DataFrame()
#cachedStopWords = stopwords.words("english")
for line in tweets_file:
    try:
        #python dictionary loading json data
        tweet = json.loads(line)
        
        #getting string text of tweet
        tweet_text = tweet.get('text', '')
        #convert to lower case
        tweet_text = tweet_text.lower()
        #removing special characters
        tweet_text = re.sub('[^A-Za-z0-9]+', ' ', tweet_text)
        #removing additional white spaces
        tweet_text = re.sub('[\s]+', ' ', tweet_text)
        print tweet_text
        #remove stop words(not working for now)
        #tweet_text = ' '.join([word for word in tweet_text.split() if word not in cachedStopWords])
#         
        #print tweet_text
        #getting language of tweet

        tweets_text_data.append(tweet_text)
    except:
        continue


