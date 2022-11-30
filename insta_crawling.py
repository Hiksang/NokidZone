from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#https://www.instagram.com/explore/tags/%EB%85%B8%ED%82%A4%EC%A6%88%EC%A1%B4/

baseUrl='https://www.instagram.com/explore/tags/'
plusUrl=input('검색할 태그를 입력하세요:')
url=baseUrl+quote_plus(plusUrl)

driver=webdriver.Chrome()
driver.get(url)

time.sleep(3)

html=driver.page_source
soup=BeautifulSoup(html)

insta=soup.select('._aabd._aa8k._aanf')

n=1
for i in insta:
    print('https://www.instagram.com'+i.a['href'])
    imgUrl=i.select_one('._aagv').img['src']
    with urlopen(imgUrl) as f:
        with open('./img/'+plusUrl+str(n)+'.jpg','wb') as h:
            img=f.read()
            h.write(img)
    n+=1
    print(imgUrl)
    print()

driver.close()

