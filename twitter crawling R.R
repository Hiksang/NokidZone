#트위터 크롤링

twr<-c('twitteR','base64enc','ROAuth')
install.packages(twr,dependencies=T)
library(twitteR)
library(base64enc)

#키 발급 후 ''안에 복붙하기
options(httr_oauth_cache=T)
setup_twitter_oauth(consumer_key='',
                    consumer_secret='',
                    access_token='',
                    access_secret='')
                    
                    
#인증이 잘 되었는지 확인
getCurRateLimitInfo()

string<-'노키즈존'
string<-iconv(string,'cp949','UTF8')
tweets<-searchTwitter(searchString=string,n=100)
tweets
text_extracted<-sapply(tweets,function(t) t$getText())
text_extracted
