#Ʈ���� ũ�Ѹ�

twr<-c('twitteR','base64enc','ROAuth')
install.packages(twr,dependencies=T)
library(twitteR)
library(base64enc)

#Ű �߱� �� ''�ȿ� �����ϱ�
options(httr_oauth_cache=T)
setup_twitter_oauth(consumer_key='',
                    consumer_secret='',
                    access_token='',
                    access_secret='')
                    
                    
#������ �� �Ǿ����� Ȯ��
getCurRateLimitInfo()

string<-'��Ű����'
string<-iconv(string,'cp949','UTF8')
tweets<-searchTwitter(searchString=string,n=100)
tweets
text_extracted<-sapply(tweets,function(t) t$getText())
text_extracted