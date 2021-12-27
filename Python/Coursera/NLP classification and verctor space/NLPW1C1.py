import nltk
import re
import string
import random
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

#1. clean data (remove # and https)
#2. tokenize
#3. remove stopwords
#4. stemming (happy ==> happ)


nltk.download('twitter_samples')
nltk.download('stopwords')

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')
print(len(all_positive_tweets))
tweet = all_positive_tweets[2277]
print(tweet)

tweet2 = re.sub(r'^RT[\s]+','', tweet)
tweet2 = re.sub(r'https?:\/\/.*[\r\n]*','', tweet2)
tweet2 = re.sub(r'#','', tweet2)
print(tweet2)

tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
tweet_tokens = tokenizer.tokenize(tweet2)
print(tweet_tokens)

stopwords_english = stopwords.words('english')

tweets_clean = []

for word in tweet_tokens:
    if(word not in stopwords_english and word not in string.punctuation):
        tweets_clean.append(word)

print(tweets_clean)


stemmer = PorterStemmer()
tweets_stem = []

for word in tweets_clean:
    tweets_stem.append(stemmer.stem(word))

print(tweets_stem)




