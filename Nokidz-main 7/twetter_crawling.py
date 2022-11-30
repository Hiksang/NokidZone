twitter_consumer_key = ""
twitter_consumer_secret = ""  
twitter_access_token = ""
twitter_access_secret = ""

import twitter
twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)

from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# main code start
import twitter, time

# twitter api connect
twitter_consumer_key = env('twitter_consumer_key')
twitter_consumer_secret = env('twitter_consumer_secret')
twitter_access_token = env('twitter_access_token')
twitter_access_secret = env('twitter_access_secret')

twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                          consumer_secret=twitter_consumer_secret, 
                          access_token_key=twitter_access_token, 
                          access_token_secret=twitter_access_secret)
#검색하기
query = "노키즈존"
search = twitter_api.GetSearch(term=query, count=100)

for i in search:
    print(i.text) # 텍스트만 출력하기

#실시간 스트리밍
query = ["노키즈존"]
stream = twitter_api.GetStreamFilter(track=query)
        
for tweet in stream:
    print(tweet['text'])
