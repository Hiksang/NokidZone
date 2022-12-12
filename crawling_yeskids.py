from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


driver = webdriver.Chrome(ChromeDriverManager().install())
names = []
adrs = []
for i in range(3, 441):  # 441
    try:
        driver.get(
            'https://www.google.com/maps/d/viewer?mid=1XNvlhjVsrQFtelWfLapc76MiJ9c&ll=33.5087074%2C126.88813720000009&z=8')
        driver.implicitly_wait(10)
        right = driver.find_element(By.XPATH,
                                    "//*[@id='legendPanel']/div/div/div[2]/div/div/div[2]/div[1]/div/div[3]/div[441]/span")
        right.click()  ## 전체보기
        driver.implicitly_wait(10)
        right = driver.find_element(By.XPATH,
                                    f"//*[@id='legendPanel']/div/div/div[2]/div/div/div[2]/div[1]/div/div[3]/div[{i}]")
        right.click()  ## 첫번째
        #     adr = driver.find_element(By.XPATH, "featurecardPanel > div > div > div.qqvbed-bN97Pc > div.qqvbed-VTkLkc.fO2voc-jRmmHf-LJTIlf > div.fO2voc-jRmmHf-MZArnb-Q7Zjwb")
        driver.implicitly_wait(10)
        name = driver.find_element(By.XPATH, "//*[@id='featurecardPanel']/div/div/div[4]/div[1]/div/div[2]")
        #     adr = driver.find_element(By.XPATH, "//*[@id='featurecardPanel']/div/div/div[4]/div[2]/div/div[2]")
        driver.implicitly_wait(10)
        adr = driver.find_element(By.CSS_SELECTOR,
                                  "#featurecardPanel > div > div > div.qqvbed-bN97Pc > div.qqvbed-VTkLkc.fO2voc-jRmmHf-LJTIlf > div.fO2voc-jRmmHf-MZArnb-Q7Zjwb")
        names.append(name.text)
        adrs.append(adr.text)
        print(i)
        driver.implicitly_wait(10)
    except:
        print("not")



df = pd.DataFrame((zip(names, adrs)), columns=['place', 'adr'])
print(df)
df.to_excel("nokids.xlsx")